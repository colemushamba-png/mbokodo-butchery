from django.shortcuts import render, get_object_or_404
from .models import Enquiry, Product, Order


def home(request):
    try:
        products = Product.objects.all()
    except:
        products = []
    return render(request, 'index.html', {'products': products})



def products_page(request):
    return render(request, 'products.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        Enquiry.objects.create(
            name=name,
            phone=phone,
            message=message
        )

        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')


def order(request):
    products = Product.objects.all()

    if request.method == 'POST':
        product_id = request.POST.get('product')
        product = get_object_or_404(Product, id=product_id)

        qty = float(request.POST.get('quantity'))
        currency = request.POST.get('currency')

        if currency == 'USD':
            price = product.price_usd
        elif currency == 'ZWL':
            price = product.price_zwl
        else:
            price = product.price_rand

        total = qty * float(price)

        Order.objects.create(
            customer_name=request.POST.get('name'),
            phone=request.POST.get('phone'),
            product=product,
            quantity_kg=qty,
            currency=currency,
            total_price=total
        )

        return render(
            request,
            'order.html',
            {
                'success': True,
                'products': products,
                'total': total
            }
        )

    return render(request, 'order.html', {'products': products})
