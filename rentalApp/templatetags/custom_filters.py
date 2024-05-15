from django import template
from django.template.defaultfilters import stringfilter
import re

register = template.Library()

@register.filter
def generate_range(value):
    return range(value)


# @register.filter(is_safe=True)
# @stringfilter
# def split_paragraphs(value):
#     paragraphs = re.split(r'\r?\n\r?\n', value)
#     return '\n\n'.join(paragraphs)

# @register.filter(is_safe=True)
# @stringfilter
# def split_paragraphs(value):
#     value = value.replace('\r\n\r\n', '\n\n')
#     value = value.replace('\n\r\n', '\n\n')
#     value = value.replace('\r\r', '\n\n')
#     return value

@register.filter(is_safe=True)
@stringfilter
def split_paragraphs(value):
    paragraphs = []
    paragraph = ''
    for line in value.splitlines():
        if line.strip() == '':
            paragraphs.append(paragraph)
            paragraph = ''
        else:
            paragraph += line + '\n'
    if paragraph:
        paragraphs.append(paragraph)
    return '\n\n'.join(paragraphs)