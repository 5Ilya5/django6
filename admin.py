from django.contrib import admin
from core.models import Person, Course, Grade
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass
@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    pass