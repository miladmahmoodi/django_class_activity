from django.contrib import admin
from . import models


class ProductImageInline(admin.TabularInline):
    model = models.Image


class ProductOptionInline(admin.TabularInline):
    model = models.ProductOption


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
        ProductImageInline,
        ProductOptionInline,
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
    list_display = [
        'id',
        'name',
        'alt',
    ]


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'text',
        'rate',
        'user_email',
        'product',
    ]
    list_filter = [
        'rate',
        'product'
    ]
    search_fields = [
        'product',
        'rate',
    ]


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'text',
        'user_email',
        'question',
    ]
    list_filter = [
        'question',
    ]
    search_fields = [
        'question',
        'user_email',
    ]


class AnswerInline(admin.TabularInline):
    model = models.Answer


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'text',
        'user_email',
        'product'
    ]
    list_filter = [
        'product',
    ]
    search_fields = [
        'product',
        'user_email',
    ]
    inlines = [
        AnswerInline,
    ]


@admin.register(models.ProductOption)
class ProductOptionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'value',
        'product',
    ]


@admin.register(models.SellerProductPrice)
class SellerProductPriceAdmin(admin.ModelAdmin):
    pass
