from django.shortcuts import render, get_object_or_404, HttpResponse
from . import models
from django.template.loader import get_template


def product(request):
    search_query = request.GET.get('search')

    products = models.Product.objects.all()

    if search_query:
        products = products.filter(
            name__contains=search_query,
        )

    context = {
        'products': products,
    }

    return render(
        request,
        'products/product-list.html',
        context,
    )


def categories(request):
    categories = models.Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(
        request,
        'products/category.html',
        context=context,
    )


def product_view(request, product_id):
    # try:
    #     p = Product.objects.get(id=product_id)
    #     template = get_template('products/products.html')
    #     return HttpResponse(template.render())
    # except Product.DoesNotExist:
    #     return HttpResponse('404 Products not found')

    product = get_object_or_404(
        models.Product,
        id=product_id,
    )
    context = {
        'product': product,
    }
    return render(
        request,
        'products/product-single.html',
        context=context,
    )
