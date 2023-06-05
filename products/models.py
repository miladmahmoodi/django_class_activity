from django.db import models
from django.utils.translation import gettext as _


class Product:
    name = models.CharField(
        verbose_name=_('persian name'),
        max_length=200,
    )
    en_name = models.CharField(
        verbose_name=_('english name'),
        max_length=200,
    )
    description = models.TextField(
        verbose_name=_('description'),
    )
    category = models.ForeignKey(
        'Category',
        verbose_name=_('category'),
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.name


class Category:
    name = models.CharField(
        verbose_name=_('name'),
        max_length=50,
    )
    slug = models.SlugField(
        verbose_name=_('slug'),
        unique=True,
        db_index=True,
    )
    description = models.TextField(
        verbose_name=_('description')
    )
    icon = models.ImageField(
        verbose_name=_('icon'),
        upload_to='./media/category/icons/',
        null=True,
        blank=True,
    )
    image = models.ImageField(
        verbose_name=_('icon'),
        upload_to='./media/category/images/',
        null=True,
        blank=True,
    )
    parent = models.ForeignKey(
        'self',
        verbose_name=_('category parent'),
        on_delete=models.SET_NULL,
        default=None,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.slug


class Image:
    name = models.CharField(
        verbose_name=_('name'),
        max_length=50,
    )
    alt = models.CharField(
        verbose_name=_('alternative text'),
        max_length=50,
    )
    image = models.ImageField(
        verbose_name=_('image'),
        upload_to='./media/products/images/',
    )
    product = models.ForeignKey(
        'Product',
        verbose_name=_('product'),
        on_delete=models.CASCADE,
    )
    is_default = models.BooleanField(
        verbose_name=_('is default image'),
        default=False,
    )

    def __str__(self):
        return self.name


class Comment:
    title = models.CharField(
        verbose_name=_('title'),
        max_length=150,
    )
    text = models.TextField(
        verbose_name=_('comment'),
    )
    rate = models.PositiveSmallIntegerField(
        verbose_name=_('rate'),
    )
    user_email = models.EmailField(
        verbose_name=_('user email'),
        max_length=254,
    )
    product = models.ForeignKey(
        'Product',
        verbose_name=_('product'),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title


class Question:
    text = models.TextField(
        verbose_name='title',
    )
    user_email = models.EmailField(
        verbose_name=_('user email'),
        max_length=254,
    )
    product = models.ForeignKey(
        'Product',
        verbose_name=_('product'),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.text


class Answer:
    text = models.TextField(
        verbose_name=_('answer'),
    )
    user_email = models.EmailField(
        verbose_name=_('user email'),
        max_length=254,
    )
    question = models.ForeignKey(
        'Question',
        verbose_name=_('question'),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.text


class ProductOption:
    title = models.CharField(
        verbose_name=_('title'),
        max_length=200,
    )
    value = models.CharField(
        verbose_name=_('value'),
        max_length=200,
    )
    product = models.ForeignKey(
        'Product',
        verbose_name=_('product'),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.title} - {self.product}'


class SellerProductPrice:
    product = models.ForeignKey(
        'Product',
        verbose_name=_('product'),
        on_delete=models.CASCADE,
    )
    # seller
    price = models.PositiveIntegerField(
        verbose_name=_('price'),
    )
    created_at = models.DateTimeField(
        verbose_name=_('created at'),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_('updated at'),
        auto_now=True,
    )

    def __str__(self):
        return self.price
