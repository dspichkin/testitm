from django.contrib import admin

from slides.models import Slide, Variant, Attempt


class VariantInline(admin.StackedInline):
    model = Variant
    extra = 1


class SlideAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    search_fields = ['text']
    inlines = (VariantInline, )


class VariantAdmin(admin.ModelAdmin):
    list_display = ('id', 'variantId', 'text')
    search_fields = ['text']


class AttemptAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'points')


admin.site.register(Slide, SlideAdmin)
admin.site.register(Variant, VariantAdmin)
admin.site.register(Attempt, AttemptAdmin)

