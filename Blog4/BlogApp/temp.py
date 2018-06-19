"""
    图片格式转化 + 裁剪图片

"""
# for picture in obj_list:
    #     print("111")
    #     imag = Image.open(picture.img)  # 从数据库获取图片路径
    #
    #     if len(imag.split()) == 4:  # 判断图片格式是几通道,JPEG是3通道 ,需要特殊处理,忽略a通道
    #         r, g, b, a = imag.split()
    #         imag = Image.merge("RGB", (r, g, b))
    #
    #     double_size = (800, 533)
    #     image_resized = imag.resize(double_size, Image.ANTIALIAS)   # 生成指定大小的图片
    #     image_resized.save("static/blog/home/imgs/zipimgs/"+ picture.img_name +".jpeg", 'JPEG')  # 保存到指定路径
    #     imag.save("static/blog/home/imgs/changeimgs/"+ picture.img_name +".jpeg", 'JPEG')  # 保存到指定路径


"""
取出当前页
"""

# "没有页码,默认为当前页"
# page_X = req.GET.get('page')
# if page_X == None:  page_X = "1"

# if (page_X not in PAGE_FLAG_LIST) or (UPDATE_FLAG != len(obj_list)):  # 该页面没有加载,更细博客
#     PAGE_FLAG_LIST.append(page_X)  # 添加页码标记
#     pag_int = int(page_X)
#     cup_list = obj_list[(pag_int - 1) * 3:((pag_int - 1) * 3) + 3]  # 只切当前页
#     for foo in cup_list:
#         primary = foo.details.content.replace(' ', '').replace('\n', '')[:36]
#         models.Blog.objects.filter(id=foo.id).update(primary=primary)
#
#     obj_list = models.Blog.objects.all()
#     temp = []
#     for obj in reversed(obj_list):  # 倒序
#         temp.append(obj)
#     obj_list = temp
#
# UPDATE_FLAG = len(obj_list)
