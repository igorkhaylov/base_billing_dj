from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.utils.translation import gettext_lazy as _
from users.models import User


class UserAdmin(AuthUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info2"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )
    list_display = ("username", "is_active", "is_staff", "is_superuser", "last_login", "date_joined",)
    list_filter = ("is_active", "is_staff", "is_superuser", "groups")
    search_fields = ("username", "first_name", "last_name")


admin.site.register(User, UserAdmin)


class LogEntryUserFilter(admin.SimpleListFilter):
    title = 'Пользователь'
    parameter_name = 'logentry_user'

    def lookups(self, request, model_admin):
        out = []
        # sqlite3
        for i in admin.models.LogEntry.objects.values('user_id', 'user__username').distinct():
            out += [(f"{i['user_id']}", f"{i['user__username']}")]
        # postgres
        # for i in admin.models.LogEntry.objects.all().order_by('user_id').distinct('user_id'):
        #     out += [(f'{i.user_id}', f'{i.user.username}')]
        return out

    def queryset(self, request, queryset):
        value = self.value()
        if value is None:
            return queryset
        return queryset.filter(user_id=int(value))


@admin.register(admin.models.LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = "__str__", "action_flag", "content_type", "object_id", "user", "action_time",
    list_filter = LogEntryUserFilter, "action_flag", "content_type",
    # has_add_permission = lambda self, request: False
    # has_change_permission = lambda self, request, obj=None: False
    # has_delete_permission = lambda self, request, obj=None: False
    # has_view_permission = lambda self, request, obj=None: request.user.is_superuser
    def get_model_perms(self, request):
        return {
            'add': False,
            'change': False,
            'delete': False,
            'view': self.has_view_permission(request),
        }


def create_rosetta_group():
    from django.db.utils import OperationalError, ProgrammingError
    try:
        # Создаем группу для Rosetta
        rosetta_group, created = Group.objects.get_or_create(name='Rosetta Users')
        # Получаем разрешение для изменения сообщений
        content_type = ContentType.objects.get_for_model(Permission)
        permission, created = Permission.objects.get_or_create(
            codename='can_change_rosetta_messages',
            name='Can change rosetta messages',
            content_type=content_type,
        )
        # Добавляем разрешение к группе
        rosetta_group.permissions.add(permission)
    except (OperationalError, ProgrammingError) as exp:
        print(exp)

create_rosetta_group()


# Text to put at the end of each page's <title>.
admin.site.site_title = _("Django Template site admin")

# Text to put in each page's <h1>.
admin.site.site_header = _("Django Template administration")

# Text to put at the top of the admin index page.
admin.site.index_title = _("Site administration")

admin.site.enable_nav_sidebar = True

admin.site.empty_value_display = "-"
