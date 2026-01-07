from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
from .forms import PersonForm


def hello_world_view(request):
    return HttpResponse("Hello, World!")

def hello_python_view(request):
    return HttpResponse("Hello, Python!")

def hello_html_view(request):
    return render(request, 'hello.html')

def hello_name(request, name):
    return HttpResponse(f"Hello, {name}!")

def hello_add(request, number1, number2):
    return HttpResponse(f"Sum is {number1  + number2}")

def hello_search(request):
    query = request.GET.get('q', '')
    database = request.GET.get('db', 'default')
    return HttpResponse(f"Search: {query} in {database} database")

def redirect_to_html(request):
    return redirect('hello_html')

def post_example(request):
    if request.method == 'POST':
        # name = request.POST.get('name', 'x')
        # age = request.POST.get('age', 'x')
        # job = request.POST.get('job', 'x')
        
        form = PersonForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            job = form.cleaned_data['job']
        
            return HttpResponse(f"Name: {name}, Age: {age}, Job: {job}")
    return HttpResponseNotAllowed(['POST'])

def basic_form(request):
    return render(request, 'form.html')

def django_form(request):
    form = PersonForm()
    return render(request, 'django_form.html', {'form': form})
