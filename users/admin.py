from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.html import format_html

from users.models import Login

User = get_user_model()


class ReadOnlyModelMixin:
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class LoginAdmin(ReadOnlyModelMixin, admin.ModelAdmin):
    list_display = (
        'id',
        'user_link_with_name',
        'user_email',
        'user_company',
        'domain',
        'date',
        'ip',
        'remote_host',
        'http_host',
        'server_name',
        'user_agent',
    )

    @admin.display(description='Name', ordering='user__first_name')
    def user_link_with_name(self, obj):
        url = reverse("admin:users_user_change", args=[obj.user.id])
        return format_html(f'<a href="{url}">{obj.user}</a>')

    @admin.display(description='Email', ordering='user__email')
    def user_email(self, obj):
        return format_html(
            f'<a href="mailto:{obj.user.email}">{obj.user.email}</a>'
        )

    @admin.display(description='Company', ordering="user__company")
    def user_company(self, obj):
        return obj.user.company


class LoginInline(ReadOnlyModelMixin, admin.TabularInline):
    model = Login
    extra = 0

    fields = (
        'date',
        'domain',
        'ip',
        'remote_host',
        'http_host',
        'server_name',
        'user_agent',
    )

    readonly_fields = fields
    can_delete = False
    show_change_link = False
    ordering = ('-date',)


class UserAdmin(auth_admin.UserAdmin):
    inlines = [LoginInline]

    ...


admin.site.register(User, UserAdmin)
admin.site.register(Login, LoginAdmin)
