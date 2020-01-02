import xadmin

from apps.organizations.models import Teacher, CourseOrg, City


class TeacherAdmin(object):
    list_display = ['name', 'org', 'work_company', 'work_position', 'work_years', 'fav_nums']
    search_fields = ['name', 'org']
    list_filter = ['name', 'org', 'work_company', 'work_position', 'work_years', 'fav_nums']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'category', 'city', 'address', 'course_nums', 'fav_nums', 'students']
    search_fields = ['name', 'desc', 'city', 'address']
    list_filter = ['name', 'desc', 'category', 'city', 'address', 'course_nums', 'fav_nums', 'students']


class CityAdmin(object):
    list_display = ['id', 'name', 'desc']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']
    list_editable = ['name', 'desc']


xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(City, CityAdmin)
