from django.template import Library
from django.utils.safestring import mark_safe
register = Library()





@register.simple_tag
def Pag_ele(querySet):
    ele = """
        <ul class="pagination">
        <li><a href="?page=1">首页</a></li>
    """
    if querySet.has_previous(): # 还有上一页
        previous_ele = querySet.number - 1
        ele += """<li><a href="?page=%s">&laquo;</a></li>""" % previous_ele
    else:   # 没有上一页,当前在第一页
        ele += """<li><a href="?page=%s">&laquo;</a></li>""" % querySet.number

    for row in querySet.paginator.page_range:
        maxPag = row
        if abs(row - querySet.number) <= 2: # 显示页码的个数
            if row == querySet.number:  #在当前页,高亮
                p_ele = """<li class="active"><a href="?page=%s">%s</a></li>""" %(row,row)
            else:
                p_ele = """<li><a href="?page=%s">%s</a></li>""" %(row,row)

            ele += p_ele

    if querySet.has_next():
        previous_ele = querySet.number + 1
        ele += """<li><a href="?page=%s">&raquo;</a></li>"""%previous_ele
    else:
        ele += """<li><a href="?page=%s">&raquo;</a></li>"""%querySet.number
    ele += """
    <li><a href="?page=%s">末页</a></li>
    """ %maxPag
    return mark_safe(ele)