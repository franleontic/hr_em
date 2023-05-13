import classla
import stopwordsiso as stopwords
import os
  

def tokenize(text):
    text = nlp(text)
    words = []
    for sentence in text.sentences:
        for word in sentence.words:
            if word.upos != "PUNCT" and word.text.lower() not in sw:
                words.append(word.text.lower())
    return words

nlp = classla.Pipeline("hr", processors='tokenize, pos', tokenize_no_ssplit=True)
sw = stopwords.stopwords("hr")
script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
years = ["2020"]
months = ["01", "02"]

for y in years:
    for m in months:
        try:
            path = f"./charreplace/{y}-{m}"
            path_result = f"./tokenized/{y}-{m}"
            path = os.path.join(script_dir, path)
            os.chdir(path)
            path_result = os.path.join(script_dir, path_result)

            for date in os.listdir():
                curr_path = os.path.join(path, date)
                os.makedirs(path_result, exist_ok=True)
                curr_path_result = os.path.join(path_result, date)
                os.chdir(curr_path)

                file_path = f"{curr_path}"
                dest_path = f"{curr_path_result}.txt"
                with open(dest_path, 'w') as f1:
                    for file in os.listdir():
                        file_path = f"{curr_path}/{file}"
                        with open(file_path, 'r') as f2:
                            text = f2.read().rstrip()
                            text = tokenize(text)
                            f1.write(','.join(text))
                            f1.write('\n')
        except FileNotFoundError:
            print(f"{y}-{m} not found")
