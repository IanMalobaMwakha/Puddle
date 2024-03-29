from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewItemForm, EditItemForm
from .models import Cartegory, Item

def items(request):
    query = request.GET.get('query', '')
    cartegory_id = request.GET.get('cartegory', 0)
    categories = Cartegory.objects.all()
    items = Item.objects.filter(is_sold=False)


    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    if cartegory_id:
        items = items.filter(cartegory_id=cartegory_id)


    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'cartegory_id': int(cartegory_id),
    })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(cartegory=item.cartegory, is_sold=False).exclude(pk=pk)[0:3]
    profile = item.created_by.profile

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items,
        'profile': profile,
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('items:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html',{
        'form':form,
        'title': 'Add New item',
    })


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('items:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html',{
        'form':form,
        'title': 'Edit item',
    })


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')
