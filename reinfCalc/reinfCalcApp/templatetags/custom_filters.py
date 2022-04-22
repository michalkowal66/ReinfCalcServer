from django import template


register = template.Library()

@register.filter(name='m2TOcm2')
def m2TOcm2(value):
    return round(value*10_000, 4)

@register.filter(name='mTOcm')
def mTOcm(value):
    return round(value*100, 2)

@register.filter(name='mTOmm')
def mTOmm(value):
    return int(value*1000)

@register.filter(name='kiloTOmega')
def kiloTOmega(value):
    return round(value/1000, 4)

@register.filter(name='round_four')
def round_four(value):
    return round(value, 4)
