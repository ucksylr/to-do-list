from todo.views import register
from django.template.defaultfilters import stringfilter
from django import template
import random
register = template.Library()

@register.filter(name='getdictvalues')
def getdictvalues(dict,x):
    return dict.get(x)

@register.filter()
@stringfilter
def upto(value):
    return "expired" if value == "0\xa0minutes" else f"{value.split(',')[0]} left"
upto.is_safe = True

@register.filter()
@stringfilter
def timeformat(value):
    return f"{value.split(' ')[0]}"

@register.filter()
@stringfilter
def coloredlist(value):
    rnd = random.randint(0,7) 
    colors = ["primary", "secondary", "success", "danger", "warning", "info", "light", "dark"]
    return colors[rnd]

@register.filter()
@stringfilter
def expiredbadge(value):
    return "danger" if value == "expired" else "secondary"