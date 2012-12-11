from django.contrib import admin

from broadcast.models import Kinship


class KinshipAdmin(admin.ModelAdmin):
    list_display = ["patient", "familymember"]


admin.site.register(Kinship, KinshipAdmin)