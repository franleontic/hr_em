import os
import pickle

import classla
import numpy as np
import stopwordsiso as stopwords
from application.models import *
from django import forms
from django.contrib.auth import *
from django.contrib.auth.forms import *
from django.shortcuts import redirect, render
from django.views import View
from django.conf import settings

nlp = classla.Pipeline("hr", processors='tokenize, pos, lemma', tokenize_no_ssplit=True)
sw = stopwords.stopwords("hr")

with open(os.path.join(settings.STATIC_ROOT, "disc_model.pickle"), 'rb') as file:
    ds = pickle.load(file)
with open(os.path.join(settings.STATIC_ROOT, "dim_model_MS.pickle"), 'rb') as file:
    dmb = pickle.load(file)
with open(os.path.join(settings.STATIC_ROOT, "dim_model_Google.pickle"), 'rb') as file:
    dmg = pickle.load(file)

def index(request):
    if request.method == 'POST':
        text = request.POST.get('textbox')
        model = request.POST.get('select')

        text = nlp(text)
        words = []
        for sentence in text.sentences:
            for word in sentence.words:
                if word.upos != "PUNCT" and word.text.lower() not in sw:
                    words.append(word.lemma.lower())

        if model == "ds":
            model_obj = ds
        elif model == "dmb":
            model_obj = dmb
        elif model == "dmg":
            model_obj = dmg
        ratings, final_rating, confidence = model_obj.score_all(",".join(words))

        if request.user.is_authenticated:
            text = ",".join(words)
            ratings_bytes = ratings.tobytes()
            fr_bytes = final_rating.tobytes()
            text_obj = Text()
            text_obj.text = text
            text_obj.rating = fr_bytes
            text_obj.rating_list = ratings_bytes
            text_obj.dim = True if model != "ds" else False
            text_obj.confidence = confidence
            text_obj.user = User.objects.get(id=request.user.id)
            text_obj.save()
        return render(request, "index.html", {"textval": request.POST.get('textbox'), "ratings": zip(words, ratings), "confidence": confidence, "final_rating": final_rating, "model" : model})
    else:
        return render(request, "index.html")

def logout_custom(request):
    logout(request)
    return redirect("/")


class RegisterForm(UserCreationForm):
    email = forms.EmailField(help_text="Required.")

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class RegisterView(View):
    def get(self, request):
        context = {}
        form = RegisterForm(request.POST or None)
        context['form'] = form
        return render(request, 'register.html', context)

    def post(self, request):
        context = {}
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        context['form'] = form
        return render(request, 'register.html', context)

class LoginView(View):
    def get(self, request):
        context = {}
        form = AuthenticationForm(request.POST or None)
        context['form'] = form
        return render(request, 'login.html', context)

    def post(self, request):
        context = {}
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        context['form'] = form
        return render(request, 'login.html', context)
    
class ListView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("/login")
        id = request.user.id
        user = User.objects.get(id=id)
        texts = Text.objects.filter(user=user)
        dim_text_words = []
        dim_text_ratings = []
        disc_text_words = []
        disc_text_ratings = []
        dim_cfs = []
        disc_cfs = []

        for text in texts:
            if text.dim == True:
                dim_text_words.append(text.text)
                dim_text_ratings.append(np.frombuffer(text.rating))
                dim_cfs.append(text.confidence)
            else:
                disc_text_words.append(text.text)
                disc_text_ratings.append(np.frombuffer(text.rating))
                disc_cfs.append(text.confidence)
        return render(request, 'list.html', {"dim": zip(dim_text_ratings, dim_text_words, dim_cfs),
                                            "disc": zip(disc_text_ratings, disc_text_words, disc_cfs)})


