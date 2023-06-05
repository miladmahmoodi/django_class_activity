from django.contrib import admin
from . import models


class ImageInline(admin.TabularInline):
    model = models.Image


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'en_name',
        'name',
        'category',
    ]
    list_filter = [
        'category',
    ]
    search_fields = [
        'en_name',
        'name',
    ]

    inlines = [
        ImageInline,
    ]


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
        'slug',
        'parent',
    ]
    list_filter = [
        'parent',
    ]
    search_fields = [
        'name',
        'description',
    ]
    fieldsets = (
        ('Details', {
            'fields': (
                'name',
                'slug',
                'description',
                'parent',
            ),
        }),
        ('Images', {
            'fields': (
                'icon',
                'image',
            ),
        }),
    )


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass


class AnswerInline(admin.TabularInline):
    model = models.Answer


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
    ]


@admin.register(models.ProductOption)
class ProductOptionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SellerProductPrice)
class SellerProductPriceAdmin(admin.ModelAdmin):
    pass
