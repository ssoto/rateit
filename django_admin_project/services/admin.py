from django.contrib import admin
from .models import Bar


class BarAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created_at',
        'updated_at',
    )

    fieldsets = (
        (None, {
            'fields': (
                'name',
                'bar_type',
                'zip_code'
            )
        }),
        ('Audit info:', {
            'fields': readonly_fields
        })
    )


admin.site.register(Bar, BarAdmin)
