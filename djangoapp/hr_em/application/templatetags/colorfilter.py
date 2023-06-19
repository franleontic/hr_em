from django import template

register = template.Library()

@register.filter
def calculate_color_bb(value):
    l = int(10 + (value / 10) * 80) 
    return f'hsl(220, 100%, {l}%)'

@register.filter
def calculate_color_bo(value):
    l = int(10 + (value / 10) * 80) 
    return f'hsl(32, 100%, {l}%)'

@register.filter
def calculate_color_bp(value):
    l = int(10 + (value / 10) * 80) 
    return f'hsl(290, 100%, {l}%)'

@register.filter
def calculate_color_bg(value):
    if value == 1:
        return f'hsl(114, 100%, 50%)'
    return f'hsl(114, 100%, 0%)'