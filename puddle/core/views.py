from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from items.models import Cartegory, Item

from .forms import SignupForm

from django.contrib.auth import logout

def index(request):
    items = Item.objects.filter(is_sold=False) [0:20]
    categories = Cartegory.objects.all()

    return render(request, 'core/index.html',{
        'categories': categories,
        'items': items,
    }) 

def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')

def privacy_policy(request):
    return render(request, 'core/privacy_policy.html')

def terms_of_use(request):
    return render(request, 'core/terms_of_use.html')

def faq(request):
    return render(request, 'core/faq.html')

def product_listing_policy(request):
    return render(request, 'core/product_listing_policy.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

@login_required
def logout_view(request):
    logout(request)
    return render(request, 'core/logout_success.html')
