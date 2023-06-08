from .models import Category


def navbar(request):
    return {
        "navbar": Category.objects.all(),
    }
