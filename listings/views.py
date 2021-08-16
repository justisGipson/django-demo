from listings.form import ListingForm
from django.shortcuts import redirect, render
from .models import Listings

# Create your views here.

def index(req):
  return render(req, 'listings/index.html')

def all_listings(req):
  all_listings = Listings.objects.order_by('-list_date')

  context = {"all_listings": all_listings}
  return render(req, 'listings/all_listings.html', context)

def new_listing(req):
  # use != to get empty form
  if req.method != 'POST':
    form = ListingForm()
  else:
    # form w/ data from user
    form = ListingForm(req.POST, req.FILES)
     # check if is_valid against params in model
    if form.is_valid():
      form.save()
      # go back to listings page after submition
      return redirect('listings:all_listings')

  context = {'form': form}
  return render(req, 'listings/new_listing.html', context)

