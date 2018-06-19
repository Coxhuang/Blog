from django.template import Library
from django.utils.safestring import mark_safe
register = Library()





@register.simple_tag
def Pag_ele(obj_list):

    ele = """
        <div class="row">
    """

    for obj in obj_list:
        pass



    return mark_safe(ele)