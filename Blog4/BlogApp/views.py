from django.shortcuts import render,HttpResponse
from BlogApp import models
from django.http import JsonResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from PIL import Image
import time
import random



FLAG = False



def home(req):
    """
        首页
    """
    global FLAG
    print("T_STR1",time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time())))

    obj_list = models.Blog.objects.all()  # <class 'django.db.models.query.QuerySet'>
    print(obj_list)
    if FLAG == False:
        """"
        只进来一次
        功能:重新给博文赋id,从1开始,正序给(因为会出现删除博文的情况,所以要重新给id)
        """
        FLAG = True
        for i,obj in enumerate(obj_list):
            models.Blog.objects.filter(id = obj.id).update(id = i+1)  # 正序给id
        obj_list = models.Blog.objects.all()
    "倒序"
    temp = []
    for obj in reversed(obj_list):  # 倒序
        temp.append(obj)
    obj_list = temp
    print(obj_list)

    "分页"
    p = Paginator(obj_list, 3)  # 每页显示3个数据
    page_X = req.GET.get('page')
    try:
        obj_list = p.page(page_X)
    except PageNotAnInteger:
        obj_list = p.page(1)
    except EmptyPage:   # 空
        obj_list = p.page(1)


    print("T_STR2",time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time())))
    return render(req, "home.html", {"obj_list": obj_list})






def content(req,title_id):
    """
    博文
    """
    len_obj = len(models.Blog.objects.all())

    if (int(title_id) != len_obj) and (title_id != "1"):    # 既不是最后一个,也不是第一个
        id_last = int(title_id) + 1
        id_last = str(id_last)
        id_pre = int(title_id) - 1
        id_pre = str(id_pre)
    elif int(title_id) == len_obj:
        id_last = "1"
        id_pre = int(title_id) - 1
        id_pre = str(id_pre)
    else:
        id_pre = str(len_obj)
        id_last = int(title_id) + 1
        id_last = str(id_last)

    obj = models.Blog.objects.filter(id = title_id).first()
    obj_last = models.Blog.objects.filter(id = id_last).first()
    obj_pre = models.Blog.objects.filter(id = id_pre).first()

    obj_list = []
    obj_list.append(obj_pre)
    obj_list.append(obj)
    obj_list.append(obj_last)
    return render(req,"content.html",{"obj_list":obj_list})


def timeline(request):
    obj_list = models.Blog.objects.all()
    "倒序"
    temp = []
    for obj in reversed(obj_list):  # 倒序
        temp.append(obj)
    obj_list = temp
    print(obj_list)
    return render(request,"timeline.html",{"obj_list":obj_list})


def messageboard(request):
    obj_list = models.MessageContent.objects.all()
    "倒序"
    temp = []
    for obj in reversed(obj_list):  # 倒序
        temp.append(obj)
    obj_list = temp
    return render(request,"msgboard.html",{"obj_list":obj_list})

def msgajax(request):
    print("request:", request.GET)
    print("userNamename:", request.GET["userNamename"])
    print("conBoxname:", request.GET["conBoxname"])
    msgBoardDict = {}
    imgNum = random.randint(1, 13)
    msgBoardDict["imgNum"] = imgNum
    models.MessageContent.objects.create(
        username=request.GET["userNamename"],
        content=request.GET["conBoxname"],
        userimg=imgNum,
    )
    msgBoardDict["userName"] = request.GET["userNamename"]
    msgBoardDict["userContent"] = request.GET["conBoxname"]
    return JsonResponse(msgBoardDict)

def FIRST(request):

    return render(request,"home.html")



