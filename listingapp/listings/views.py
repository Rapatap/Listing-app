
from django.shortcuts import render, get_object_or_404, redirect
from .models import ListingItem
from django.contrib.auth.decorators import login_required
from .forms import ListingForm

@login_required
def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.user = request.user  # Assign the logged-in user to the listing
            listing.save()
            return redirect('listing_list')
    else:
        form = ListingForm()
    return render(request, 'create_listing.html', {'form': form})

def listing_list(request):
    listings = ListingItem.objects.all()
    return render(request, 'listings/listing_list.html', {'listings': listings})

def listing_detail(request, pk):
    listing = get_object_or_404(ListingItem, pk=pk)
    return render(request, 'listings/listing_detail.html', {'listing': listing})


# Create your views here.
