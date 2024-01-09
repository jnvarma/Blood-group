from django.shortcuts import render,redirect
from .models import UserProfile,GetDonor
from .forms import DonorSearchForm
def register (request):
    if request.method == "POST":
        registration = UserProfile(
            name =request.POST["name"],
            phone=request.POST["phone"],
            blood= request.POST["blood"],
            address=request.POST["address"],
            willing_to_donate=request.POST["availability"]
        )
        registration.save()
        return redirect("donor_search")
    return render (request,"blood_register.html")
    


def donor_search(request):
    if request.method == 'GET':
        form = DonorSearchForm(request.GET)
        if form.is_valid():
            blood = form.cleaned_data['blood']
            address = form.cleaned_data['address']
            print(f"Blood: {blood}, Address: {address}")
            donors = GetDonor.objects.filter(blood=blood, address=address)
            
            return render(request, 'donor_list.html', {'donors': donors})
    else:
        form = DonorSearchForm()
    return render(request, 'donor_search.html', {'form': form})      
    
    
def donor_list(request):
    donors = GetDonor.objects.all()  
    return render(request, 'donor_list.html', {'donors': donors})
