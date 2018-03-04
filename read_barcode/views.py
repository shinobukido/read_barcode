from django.template.response import TemplateResponse
from read_barcode.models import Product
from .forms import AmountForm


def product_list(request):
    products = Product.objects.all()
    form = AmountForm(request.GET)
    if form.is_valid():
        amount = form.cleaned_data.get('amount')
        if amount is None:
            amount = 1
    for product in products:
        data = product.price * amount

    return TemplateResponse(request, 'read_barcode/product_list.html',
                            {'products': products,
                             'form': form,
                             'amount': amount,
                             'data': data})
