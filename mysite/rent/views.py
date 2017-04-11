from django.shortcuts import render, redirect
from .models import InventoryItem


# Create your views here.
def index(request):
    items = InventoryItem.objects.all()
    for item in items:
        name = item.name
        quantity = item.quantity
        price = item.price
    return render(request, 'site/webdev.html', {'items': items})


def rent(request, item_id):
    """ This view function removes 1 item from the inventory when the minus button is clicked
    """
    # read Item with id item_id from the database
    rental = InventoryItem.objects.get(pk=item_id)
    if rental.quantity > 0:
        rental.quantity -= 1
        rental.save()
    return redirect('index')


def returns(request, item_id):
    """ This view function removes 1 item from the inventory when the minus button is clicked
    """
    # read Item with id item_id from the database
    rental = InventoryItem.objects.get(pk=item_id)
    if rental.quantity >= 0:
        rental.quantity += 1
        rental.save()
    return redirect('index')
