from django.shortcuts import render,redirect

from django.views import View

from .forms import RegisterForm , LoginForm 

from django.contrib.auth import authenticate,login,logout

from .models import Instructor,Course,Lecture

# Create your views here.

def signout_view(request):
    logout(request)
    return redirect('home')


class home_view(View):

    def get(self , request):
       

        if request.user.is_authenticated:
            return redirect('admin_panel')

        forms = LoginForm()
        context = {'forms':forms}
        return render(request , 'home.html' , context)

    def post(self , request):

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username , password = password)

        if user is not None:
            login(request , user)

            return redirect('admin_panel')

        return redirect('home')


class register_view(View):
    def get(self , request):

        if request.user.is_authenticated:
            return redirect('admin_panel')

        forms = RegisterForm()
        context = {'forms':forms}

        return render(request , 'register.html' , context)

    def post(self , request):

        forms = RegisterForm(request.POST)
        if forms.is_valid():
            forms.save()

            return redirect('home')

        context = {'forms':forms}
        return render(request , 'register.html' , context)













def assign_lecture(request):
    if request.method == 'POST':
        instructor_id = request.POST['instructor']
        lecture_date = request.POST['date']
        course_id = request.POST['course']
        instructor = Instructor.objects.get(id=instructor_id)
        lecture = Lecture.objects.filter(instructor=instructor, date=lecture_date).first()
        if lecture:
            return render(request, 'assign_lecture.html', {'error': 'Schedule clash. Please choose a different date.'})
        else:
            course = Course.objects.get(id=course_id)
            Lecture.objects.create(date=lecture_date, instructor=instructor, course=course)
            return redirect('admin_panel')
    instructors = Instructor.objects.all()
    courses = Course.objects.all()
    return render(request, 'assign_lecture.html', {'instructors': instructors, 'courses': courses})

def admin_panel(request):
    instructors = Instructor.objects.all()
    courses = Course.objects.all()
    lectures = Lecture.objects.all()
    return render(request, 'admin_panel.html', {'instructors': instructors, 'courses': courses, 'lectures': lectures})

def instructor(request):
    instructors = Instructor.objects.all()
    courses = Course.objects.all()
    lectures = Lecture.objects.all()
    
    return render(request, 'instructor.html', {'instructors': instructors,'courses': courses,'lectures': lectures})


def add_course(request):
    if request.method == 'POST':
        name = request.POST['name']
        level = request.POST['level']
        description = request.POST['description']
        image = request.FILES['image']
        course = Course.objects.create(name=name, level=level, description=description, image=image)
        return redirect('admin_panel')
    return render(request, 'add_course.html')

def add_instructor(request):
    if request.method == 'POST':
        name = request.POST['name']
        department = request.POST['department']
        
        instructor = Instructor.objects.create(name=name ,department=department)
        return redirect('admin_panel')
    return render(request, 'add_instructor.html')