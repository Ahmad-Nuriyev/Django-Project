from django.contrib import admin

from authentication.models import BlockedIPAdresses

admin.site.register(BlockedIPAdresses)