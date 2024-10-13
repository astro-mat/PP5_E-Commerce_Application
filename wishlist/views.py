from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Wishlist
from .forms import WishlistForm

from django.http import JsonResponse

from products.models import Product

# Create your views here.
@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user, item=product)
    if created:
        messages.success(request, "Product added to wishlist")
        return JsonResponse(data={'created': 'ok'})
    else:
        messages.warning(request, "Product already in wishlist")
    # return redirect("product_detail", product_id=product_id)
        return JsonResponse(data={'exists': 'ok'})

@login_required
def remove_from_wishlist(request, wishlist_id):
    wishlist = get_object_or_404(Wishlist, pk=wishlist_id)
    wishlist.delete()
    messages.success(request, "Product removed from wishlist")
    # return redirect("view_wishlist")
    # return JsonResponse(updated_data)
    return JsonResponse(data={'deleted': 'ok'})


@login_required
def view_wishlist(request):
    wishlists = Wishlist.objects.filter(user=request.user).order_by('-added_date')
    return render(request, "wishlist.html", {"wishlists": wishlists})
