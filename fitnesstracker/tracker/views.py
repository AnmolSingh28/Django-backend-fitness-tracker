from django.shortcuts import render,redirect
from .models import Activity, Workout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.utils import timezone
from collections import defaultdict


def activity_list(request):
    activities=Activity.objects.all()
    return render(request,'tracker/activity_list.html',{'activities':activities})


@login_required
def add_workout(request):
    completed=request.session.get('completed_exercises',[])
    try:
        if request.method == 'POST':
           
            workout = Workout.objects.create(user=request.user)

            count = int(request.POST.get('exercise_count', 0))
            today=timezone.now().date()
            workout,_ = Workout.objects.get_or_create(user=request.user, created_at__date=today)   
            for i in range(1, count + 1):
                name = request.POST.get(f'name_{i}')
                sets = request.POST.get(f'sets_{i}')
                reps = request.POST.get(f'reps_{i}')
                weight = request.POST.get(f'weight_{i}')
                timer = request.POST.get(f'timer_{i}')

                if name:
                    Activity.objects.create(
                        workout=workout,
                        name=name,
                        sets=sets,
                        reps=reps,
                        weight=weight,
                        timer=timer,
            
                    )
                    if i not in completed:
                        completed.append(i) #if exercise completed wali list me nhi h toh usko cmpleted wali list me daaldo
            request.session["completed_exercises"]=completed
            return redirect('display_today_workout')

    except Exception as e:
            print("Error saving workout:", e)

    return render(request, 'tracker/add_workout.html', {
        'completed_exercises': completed
        })

   
def display_today_workout(request):
    today = timezone.now().date()
    try:
        workout = Workout.objects.get(user=request.user, created_at=today)
        activities = Activity.objects.filter(workout=workout)
    except Workout.DoesNotExist:
        workout = None
        activities = []

    return render(request, 'tracker/today_workout.html', {
        'workout': workout,
        'activities': activities
    })
def history_view(request):
    today = timezone.now().date()
    old_workouts = Workout.objects.filter(user=request.user, created_at=today)

    # Grouping by date
    grouped = defaultdict(list)
    for workout in old_workouts:
        date = workout.created_at.date()
        grouped[date].append(workout)

    return render(request, 'tracker/history.html', {
        'grouped_workouts': dict(grouped)
    })
@login_required
def display_timer(request):
    if request.method=='POST':
        return redirect('workout_list')
    return render(request,'tracker/display_timer.html')

        
# Create your views here.
@login_required
def workout_list(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    workouts=Workout.objects.filter(user=request.user)
    return render(request,'tracker/workout_list.html',{'workouts':workouts})

def user_login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect("dash_board")
        else:
            return render(request,'tracker/login.html',{'error':'Invalid username or password'})
    return render(request,'tracker/login.html')
def dash_board(request):
    return render(request, 'tracker/dashboard.html')

def home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    return render(request,'tracker/home.html')