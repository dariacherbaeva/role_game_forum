from django.contrib import admin

from characters.models import Character, Faculty, Subject


class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)
    ordering = ('name',)


class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'age')


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Character, CharacterAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Subject, SubjectAdmin)
