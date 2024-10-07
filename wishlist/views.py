from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Wishlist
from .forms import WishlistForm

# Create your views here.
@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user, item=product)
    if created:
        messages.success(request, "Product added to wishlist")
    else:
        messages.warning(request, "Product already in wishlist")
    return redirect("product_detail", product_id=product_id)

@login_required
def remove_from_wishlist(request, wishlist_id):
    wishlist = get_object_or_404(Wishlist, pk=wishlist_id)
    wishlist.delete()
    messages.success(request, "Product removed from wishlist")
    return redirect("view_wishlist")

@login_required
def view_wishlist(request):
    wishlists = Wishlist.objects.filter(user=request.user).order_by('-added_date')
    return render(request, "wishlist.html", {"wishlists": wishlists})