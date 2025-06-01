from django.shortcuts import render
from .forms import MyForm

def home(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            url = form.cleaned_data['url']
            print(f"Name: {name}, Age: {age}")
    else:
        form = MyForm()
    return render(request, 'home.html', {'form': form})