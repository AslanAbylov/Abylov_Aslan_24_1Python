from django.shortcuts import render, redirect
from products.models import Product, Review, Category
from products.forms import ProductCreateForm, ReviewCreateForm


PAGINATION_LIMIT = 3

def index(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')



def all_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if search is not None:
            products = Product.objects.filter(title__icontains=search)

        max_page = products.__len__() / PAGINATION_LIMIT

        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        products = products[PAGINATION_LIMIT * (page-1) : PAGINATION_LIMIT * page]

        return render(request, 'products/products.html',
                      context={'products': products,
                               'user': request.user,
                               'max_page': range(1, max_page+1)})



def one_product(request, id):
    if request.method == 'GET':
        products = Product.objects.get(id=id)
        reviews = Review.objects.filter(products=products)
        return render(request, 'products/detail.html', context={'reviews': reviews,
                                                                'products': products,})

    if request.method == 'POST':
        products = Product.objects.get(id=id)
        review = Review.objects.filter(products=products)
        forms = ReviewCreateForm(data=request.POST)

        if forms.is_valid():
            review.create(
                author_id=request.user.id,
                text=forms.cleaned_data.get('text'),
                products=products
            )

            return redirect(f'/products/{products.id}')
        return render(request, 'products/detail.html', context={'forms': forms, 'products': products, 'review': review})



def all_categories(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'categories/index.html', context={'categories': categories, 'products': products})


def one_category(request, category_id):
    category = Category.objects.filter(id=category_id)
    product = Product.objects.get(category=category)
    return render(request, 'categories/category.html', context={'category': category, 'product': product})


def product_create_view(request):
    if request.method == 'GET' and not request.user.is_anonymous:
        context = {
            'forms': ProductCreateForm
        }
        return render(request, 'products/product_create.html', context=context)
    elif request.user.is_anonymous:
        return redirect('/products/')

    if request.method == 'POST':
        forms = ProductCreateForm(data=request.POST)

        if forms.is_valid():
            Product.objects.create(
                title=forms.cleaned_data.get('title'),
                description=forms.cleaned_data.get('description'),
                rate=forms.cleaned_data.get('rate'),
                author_id=request.user.id
            )

            return redirect('/products')

        return render(request, 'products/product_create.html/', context={'forms'})

