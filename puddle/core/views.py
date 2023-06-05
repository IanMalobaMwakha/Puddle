from django.shortcuts import render

from items.models import Cartegory, Item

from .forms import SignupForm

def index(request):
    item = Item.objects.filter(is_sold=False) [0:10]
    categories = Cartegory.objects.all()

    return render(request, 'core/index.html',{
        'categories': categories,
        'item': item
    })


def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

