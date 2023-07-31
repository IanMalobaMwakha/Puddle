from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from items.models import Cartegory, Item

from .models import Profile

from .forms import SignupForm, EditProfile

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

def profile_not_found(request):
    return render(request, 'profile_not_found.html')

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


def profile(request, pk):
    try:
        user = Profile.objects.all()
        avatar = Profile.objects.all()
        location = Profile.objects.all()
        bio = Profile.objects.all()
        profile = get_object_or_404(Profile, pk=pk)
        items = Item.objects.filter(created_by=profile.user)
    except Profile.DoesNotExist:
        # Handle the case when the profile with the given pk doesn't exist
        return redirect(request, 'core/profile_not_found.html')




    return render(request, 'core/profile.html', {
        'profile': profile,
        'user': user,
        'pk': pk,
        'avatar': avatar,
        'location': location,
        'bio': bio,
        'items': items,
    })


@login_required
def editprofile(request):
    user_profile = request.user.profile  # Rename the variable to avoid conflict

    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            # Save the form with the associated user
            myprofile = form.save(commit=False)
            profile.user = request.user
            myprofile.save()

            return redirect('core:profile', pk=request.user.profile.pk)
    else:
        form = EditProfile(instance=user_profile)

        return render(request, 'core/edit_profile.html', {
                'form': form,
            })
    