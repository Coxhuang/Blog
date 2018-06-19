from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Blog(models.Model):

    title = models.TextField(max_length=17,verbose_name="标题")
    comment = models.TextField(verbose_name="评论",default="我是评论")
    details = models.OneToOneField("Details",verbose_name="更多")
    primary = models.TextField(verbose_name="快照",default="默认快照",max_length=42)
    date = models.DateField(auto_now_add=True)
    img = models.FileField(verbose_name="照片",default="",upload_to="static/blog/home/imgs/upload/")
    img_name = models.CharField(max_length=16,verbose_name="图片名称",default='')
    # authority = models.IntegerField(verbose_name="博文权限",default=0)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "博客"




class Details(models.Model):

    # content = models.TextField(verbose_name="内容")
    content = RichTextUploadingField(verbose_name='正文')  # 使用ckeditor中的RichTextField

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name_plural = "详细内容"



class MessageContent(models.Model):
    username = models.CharField(max_length=32, verbose_name="好友姓名")
    content = models.CharField(max_length=160,verbose_name="留言内容")
    userimg = models.CharField(max_length=32,verbose_name="头像")
    date = models.DateTimeField(auto_now=True,blank=True,null=True)



