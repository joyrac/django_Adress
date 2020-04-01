from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render  
  
# Create your views here.  
# from django.http import HttpResponse  
  
# def hello(request):  
#     return HttpResponse("<h2>Hello, Welcome to Django-Adress Book created by joy!</h2>")  
# from django.shortcuts import render  
from AddressBook.form import UseForm  
#*for normal viewing  
# def index(request):  
#     Use = UseForm()  
#     return render(request,"index.html",{'form':Use})  


#**for validations
# def index(request):  
#     if request.method == "POST":  
#         form = UseForm(request.POST)  
#         if form.is_valid():  
#             try:  
#                 return redirect('/')  
#             except:  
#                 pass  
#     else:  
#         form = UseForm()  
#     return render(request,'index.html',{'form':UseForm})  

from django.shortcuts import render, redirect  
from AddressBook.form import UseForm  
from AddressBook.models import Users  
# Create your views here.  
def index(request):  
    if request.method == "POST":  
        form = UseForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = UseForm()  
    return render(request,'index.html',{'form':UseForm})  
def show(request):  
    users = Users.objects.all()  
    return render(request,"show.html",{'users':users})  
def edit(request, id):  
    users = Users.objects.get(id=id)  
    return render(request,'edit.html', {'users':users})    
def update(request, id):  
    users = Users.objects.get(id=id)  
    form = UseForm(request.POST, instance = users)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'users':users})  
def destroy(request, id):  
    users = Users.objects.get(id=id)  
    users.delete()  
    return redirect("/show")  