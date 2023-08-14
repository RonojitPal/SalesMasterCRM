from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from management.forms import RegistrationForm, AddRecordForm
from management.models import CustomerRecord


# Create your views here.

def home(request):
    return render(request, 'homepage.html',{})



    

def login_user(request):

    records=CustomerRecord.objects.all()

    #Check to see if user is Logging In
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        #Authenticate the user
        user=authenticate(request, username= username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have Logged In!")
            return redirect('loginuser')
        else:
            messages.error(request, "Error Logging In, Please Try Again!")
            return redirect('loginuser')
    else:
        return render(request, 'login.html', {'records':records})
    


    
    
def logout_user(request):

    logout(request)
    messages.success(request, "You have been Logged Out!")
    return redirect('home')




def register_user(request):
    if request.method == 'POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user =authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have been registered")
            return redirect('home')
        
    else:
        form=RegistrationForm()
        return render(request,'register.html', {'form':form})    
    
    return render(request,'register.html', {'form':form})





def record(request, pk):
    if request.user.is_authenticated:
        customer_record = CustomerRecord.objects.get(id=pk)
        return render(request, 'customerrecord.html', {'customer_record':customer_record})
    
    else:
        messages.success(request, "You Must Be Logged In To View That Page")
        return redirect('loginuser')
    

    

def delete(request, pk):
    if request.user.is_authenticated:   
        delete_record=CustomerRecord.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, "Record Successfully Deleted")
        return redirect('loginuser')
    
    else:
        messages.success(request, "You Must Be Logged In To View That Page")
        return redirect('loginuser')
    


		    
def add_record(request):
    form=AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record=form.save()
                messages.success(request, "Record Has Been Added")
                return redirect('loginuser')

        return render(request,'add_record.html', {'form':form})


    else:
        messages.error(request, "You Must Be Logged In To View That Page")
        return redirect('loginuser')
    



def update_record(request, pk):
    if request.user.is_authenticated:
        record=CustomerRecord.objects.get(id=pk)
        form=AddRecordForm(request.POST or None, instance = record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated")
            return redirect('loginuser')
        return render(request,'update_record.html', {'form':form})
    else:
        messages.error(request, "You Must Be Logged In To View That Page")
        return redirect('loginuser')
   


def sort_by_order(request):
    if request.user.is_authenticated:
        sorted_records=CustomerRecord.objects.all().order_by('order_count')
        return render(request, 'sort_by_order.html', {'sorted_records':sorted_records})
    
def sort_by_firstname(request):
    if request.user.is_authenticated:
        sorted_records=CustomerRecord.objects.all().order_by('first_name')
        return render(request, 'sort_by_firstname.html', {'sorted_records':sorted_records})
    


def sort_by_lastname(request):
    if request.user.is_authenticated:
        sorted_records=CustomerRecord.objects.all().order_by('last_name')
        return render(request, 'sort_by_lastname.html', {'sorted_records':sorted_records})    
    


def sort_by_city(request):
    if request.user.is_authenticated:
        sorted_records=CustomerRecord.objects.all().order_by('city')
        return render(request, 'sort_by_city.html', {'sorted_records':sorted_records})
    

def sort_by_state(request):
    if request.user.is_authenticated:
        sorted_records=CustomerRecord.objects.all().order_by('state')
        return render(request, 'sort_by_state.html', {'sorted_records':sorted_records})    







           
	
            




    
