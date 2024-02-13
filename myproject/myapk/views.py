# views.py
from django.shortcuts import render, redirect
from .forms import InformationForm
from .models import Information

def information_form_view(request):
    if request.method == 'POST':
        form = InformationForm(request.POST, request.FILES)
        if form.is_valid():
            #create object to store the data that you get from the form input  
            name=form.cleaned_data.get("name")
            date_of_birth=form.cleaned_data.get("date_of_birth")
            salary=form.cleaned_data.get("salary")
            img=form.cleaned_data.get("img")
            obj=Information.objects.create(
                name=name,
                date_of_birth=date_of_birth,
                salary=salary,
                img=img
            )
            #save the object data
            obj.save()
            return redirect('success')  # Replace 'success' with the actual success page URL
    else:
        form = InformationForm()

    return render(request, 'index.html', {'form': form})

#redirect on the next page 
def success_view(request):
    return render(request, 'success.html')

    