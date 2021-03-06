from django.db import models

from apps.users.models import BaseModel
from apps.organizations.models import Teacher

# 1.设计表结构有几个重点
"""
实体1 <关系> 实体2
课程 章节 视频 课程资源
"""
# 2.实体的具体字段
# 3.每个字段的类型、是否必填等
# 4.分层设计，解决循环引用问题


class Course(BaseModel):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="授课讲师")
    name = models.CharField(verbose_name="课程名", max_length=50)
    desc = models.CharField(verbose_name="课程描述", max_length=300)
    learn_times = models.IntegerField(verbose_name="学习时长(分钟数)", default=0)
    degree = models.CharField(verbose_name="学习难度", choices=(('cj', '初级'), ('zj', '中级'), ('gj', '高级')), max_length=2)
    students = models.IntegerField(verbose_name="学习人数", default=0)
    fav_nums = models.IntegerField(verbose_name="收藏人数", default=0)
    click_nums = models.IntegerField(verbose_name="点击数", default=0)
    category = models.CharField(verbose_name="课程类别", max_length=20, default=u"后端开发")
    tag = models.CharField(verbose_name="课程标签", max_length=10, default="")
    youneed_know = models.CharField(verbose_name="课程须知", max_length=300, default="")
    teacher_tell = models.CharField(verbose_name="老师告诉你", max_length=300, default="")

    detail = models.TextField(verbose_name="课程详情")
    image = models.ImageField(verbose_name="封面图", upload_to="courses/%Y/%M", max_length=100)

    class Meta:
        verbose_name = "课程信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # on_delete表示级联删除
    name = models.CharField(verbose_name=u"章节名", max_length=100)
    learn_times = models.IntegerField(verbose_name="学习时长(分钟数)", default=0)

    class Meta:
        verbose_name = "课程章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(BaseModel):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name=u"章节")
    name = models.CharField(verbose_name=u"视频名称", max_length=100)
    url = models.CharField(verbose_name=u"视频地址", max_length=200)
    learn_times = models.IntegerField(verbose_name="学习时长(分钟数)", default=0)

    class Meta:
        verbose_name = "课程视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u"课程")
    name = models.CharField(verbose_name=u"资源名称", max_length=50)
    file = models.FileField(upload_to="course/resource/%Y/%M", verbose_name=u"下载地址", max_length=200)

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
