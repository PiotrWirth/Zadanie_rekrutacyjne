from django.shortcuts import render, redirect
from .forms import UploadPictureForm
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from .models import Picture

# Create your views here.

@login_required
def picture_upload(request):
    current_user = request.user
    account = Profile.objects.get(user=current_user)
    if request.method == 'POST':
        form = UploadPictureForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            return redirect('picture:tier')
    else:
        form = UploadPictureForm(data=request.GET)
    return render(request, 'picture/upload.html',{'form':form,'account':account})

def tier(request):
    current_user = request.user
    account = Profile.objects.get(user=current_user)
    photo = Picture.objects.filter(user=current_user).order_by('-id')[0]
    return render(request, 'picture/tier.html',{'account':account, 'photo':photo})