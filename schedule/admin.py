from django.contrib import admin
from .models import Event


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'name', 'comment_repr',)

    def comment_repr(self, obj):
        if not obj.comment:
            return
        if len(obj.comment) > 200:
            append = " [ . . . ] "
        else:
            append = ""
        return "%s%s" % (obj.comment[:200], append)

admin.site.register(Event, EventAdmin)