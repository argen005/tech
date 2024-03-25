from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_active')
    list_display_links = list_display
    search_fields = ('email',)
    exclude = ('password', 'groups', 'user_permissions')

