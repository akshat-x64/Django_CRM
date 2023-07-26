from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import sighUpForm,AddRecordForm
from .models import record

# Create your views here.
def home(request):
    record_1 = record.objects.all()


    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"you have been logged in")
            return redirect('home')
        else :
            messages.success(request,'There was a error logging you in,please try again')
            return redirect('home')
    else:
        return render(request,'home.html',{'records':record_1})





def logout_user(request):
    logout(request)
    messages.success(request,'You have been logged out')
    return redirect('home')



def register_user(request):
    if request.method == 'POST':
        form = sighUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authinticate and login 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"you have been successfully registered ")
            return redirect('home')
    else:
        form = sighUpForm
        return render(request,'register.html',{'form':form})
    
    return render(request,'register.html',{'form':form})



def customer_record(request,pk):
    print(pk)
    if request.user.is_authenticated:
        #Look up record
        customer_record_1 = record.objects.get(id=pk)
        return render(request,'record.html',{'record':customer_record_1})
    else:
        messages.success(request,"you must be logged in to view that page")
        return redirect('home')
    



def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it = record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,'Record Deleted Successfully....!!!')
        return redirect('home')
    
    else:
        messages.success(request,'You must be logged In.........!!!')
        return redirect('home')



def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')


def update_record(request,pk):
     if request.user.is_authenticated:
          current_record = record.objects.get(id=pk)
          form = AddRecordForm(request.POST or None,instance=current_record)
          if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated...")
            return redirect('home')
          return render(request, 'update_record.html', {'form':form})
     else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')

     