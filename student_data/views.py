from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger 
from django.db.models import Sum
from django.contrib.auth.models import User
from django.contrib import messages  
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.decorators import login_required


def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "User already exist")
            return redirect('/register')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username =  username,
                 
            
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Successfully! Account created.")
        return redirect('/register')
    return render (request,'register.html')



def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request , "Invalid Username")
            return redirect('/login/')
        
        user = authenticate(username = username , password = password)
        if user is None:
            messages.error(request , "Invalid Password")
            return redirect('/login/')
        else:
            login(request ,user)
            return redirect('/studentdata/')
        
    return render(request,'login.html') 


def logout_page(request):
    logout(request)
    return redirect('/login/')





@login_required(login_url = '/login/')
def index(request):
   return render(request,"index.html")



# Create your views here.
@login_required(login_url = '/login/')
def get_student(request):
    queryset = Student.objects.all()

    if request.GET.get('search'):
       search =  request.GET.get('search')
       queryset = queryset.filter(student_name__istartswith = search)

    paginator = Paginator(queryset,12)  # Show 15 contacts per page.
    page_number = request.GET.get("page",1)

    try:
      page = paginator.page(page_number)
    except EmptyPage:
    # Handle the case where the page number is greater than the last page.
    # You might want to redirect to the last valid page.
      page = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
    # Handle the case where the page number is not a valid integer.
      page = paginator.page(1)
    # page_obj = paginator.get_page(page_number)
    # print(page_obj.count)
    # print(page_obj.object_list)
    # print(page_obj.has_next())
    # print(page_obj.has_previous())
    # print(page_obj.has_other_pages())
    # print(page_obj.next_page_number())
    # print(page_obj.start_index())
    # print(page_obj.end_index())
    return render(request,'student.html',{'queryset' : page})


@login_required(login_url = '/login/')
def student_marks(request,student_id):
   queryset = SubjectMarks.objects.filter(student__student_id__student_id= student_id)
   total_marks = queryset.aggregate(total = Sum('marks'))
   key = total_marks['total'] 
   percentage = (key/500)*100

   return render(request,'student_marks.html',{'queryset' : queryset,'total_marks' : total_marks, 'percentage': percentage})