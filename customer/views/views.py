from django.shortcuts import render
from customer.models import Customer


# Create your views here.

def customer_list(request):
    return render(request, 'customer/customer-list.html')


def customer_detail(request, product_id):
    comments = Comment.objects.filter(product=product_id, is_private=True).order_by('-id')
    categories = Category.objects.all()
    product = Product.objects.get(id=product_id)
    min_price  = product.price * 0.2
    max_price = product.price * 1.8
    similar_product = Product.objects.filter(category=product.category, price__range=[min_price,max_price]).exclude(id=product.id)
    context = {
        'product' : product,
        'comments' : comments,
        'categories' : categories,
        'similar_product' : similar_product
    }
    return render(request, 'customer/customer-details.html', context)
