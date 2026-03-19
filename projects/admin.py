from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _


from projects.models import (Tag,
                             Task,
                             Project, User)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("name", )

    list_display = ("name", "project__name", "status", "priority", "due_date", "created_at")

    list_filter = ("status", "priority", "project__name", "due_date", "created_at")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    search_fields = ("name", )

    list_display = ("name", "created_at")

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ...


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'birth_date', 'gender', 'phone', 'age')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
        (_('Projects And Tasks'), {'fields': ('role', 'project')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'role', 'project')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'project__name')
    list_filter = ('role', 'gender')
    ordering = ('username',)


admin.site.unregister(Group)
admin.site.register(Group)
