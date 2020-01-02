import xadmin

from apps.courses.models import Course, Lesson, Video, CourseResource


# xadmin 全局设置：后台名称，主题，底部名称
class GlobalSetting(object):
    site_title = "慕学后台管理系统"
    site_footer = "慕学在线网"
    # menu_style = "accordion"


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class CourseAdmin(object):
    list_display = ['id', 'name', 'teacher', 'desc', 'category', 'students', 'fav_nums', 'click_nums']
    search_fields = ['name', 'teacher', 'desc']
    list_filter = ['name', 'teacher__name', 'category', 'students', 'fav_nums', 'click_nums']
    list_editable = ['name', 'teacher', 'desc', 'category']


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'url', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'url', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'file', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course', 'name', 'file', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(xadmin.views.CommAdminView, GlobalSetting)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSetting)

