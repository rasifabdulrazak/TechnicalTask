from django.shortcuts import render,redirect,HttpResponse
from .forms import *
from django.contrib.auth import authenticate
# Create your views here.
def home(request):
    return render(request,'staff_module/index.html')

def registration(request):
    form = RegisterForm()
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')

    context = {
        'form' : form
    }
    return render(request,'staff_module/registerform.html',context)

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                new_user = CustomUser.objects.get(email=request.POST.get('email'))
                
                user = authenticate(
                    username=new_user.username ,
                    password=request.POST['password'])

                if user is not None:
                    request.session['staff'] = user.username
                    return redirect('/listing')
                else:
                    error = '*Please enter a correct username and password.Note that both fields may be case-sensitive'
                return render(request, 'staff_module/login.html', {'form': form, 'error': error})
            except:
                error = '*Please enter a correct username and password.Note that both fields may be case-sensitive'
            return render(request, 'staff_module/login.html', {'form': form, 'error': error})

        else:
          
            return render(request, 'staff_module/login.html', {'form': form})
    else:
        return render(request,'staff_module/login.html',{'form':form})


def staff_listing(request):
    if request.session.has_key('staff'):
        staffs = CustomUser.objects.filter(is_superuser=0)
        form = AddStaff()
        context = {
            'staffs':staffs,
            'form':form
        }
        return render(request,'staff_module/listing.html',context)
    else:
        return HttpResponse("Page not found")


def add_staff(request):
    form = AddStaff()
    if request.method == 'POST':
        form=AddStaff(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listing')

def edit_staff(request,pk):
    if request.session.has_key('staff'):

        staff = CustomUser.objects.get(id = pk)
        form = EditStaff(instance=staff)
        if request.method =="POST":
            form = EditStaff(request.POST,instance=staff)
            if form.is_valid():
                if CustomUser.objects.filter(email = request.POST['email']).exclude(id = pk).exists():
                    error = "Already exist"
                    return render(request,'staff_module/edit_staff.html',{'form':form,'error':error})
                else:
                    form.save()
                    return redirect('/listing')
                
        return render(request,'staff_module/edit_staff.html',{'form':form})
    else:
        return redirect('/login')
        