from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

# Create your views here.
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products_queryset = Product.objects.all()

    query = request.GET.get('query', '').strip()
    if query:
        products_queryset = products_queryset.filter(Q(name__icontains=query)).distinct()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products_queryset = products_queryset.filter(category=category)

    paginator = Paginator(products_queryset, 4)
    page_number = request.GET.get('page')

    try:
        products_page = paginator.page(page_number)
    except PageNotAnInteger:
        products_page = paginator.page(1)
    except EmptyPage:
        products_page = paginator.page(paginator.num_pages)

    context = {
        'category': category,
        'categories': categories,
        'products': products_page,
        'query': query,
    }

    return render(request, 'shop/product_list.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product_detail.html', {'product': product})