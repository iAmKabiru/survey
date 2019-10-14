from django import template
register = template.Library()

@register.filter
def pec(value, arg):
	try:
		value = int(value)
		arg = int(arg)
		if arg: return value / arg * 100
	except: pass
	return ''
		