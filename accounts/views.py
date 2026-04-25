from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect, render
from .models import Profile

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('main:blogpage')

        else:
            return render(request, 'accounts/login.html')

    elif request.method == 'GET':
        return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('main:blogpage')

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            newuser = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
            )
            # 1:1 필드 다음에 실습 진행
            nickname = request.POST['nickname']
            major = request.POST['major']
            profile_image = request.FILES.get('profile_image')

            profile = Profile(
                user=newuser,
                nickname=nickname,
                major=major,
                profile_image=profile_image,
            )
            profile.save()

            auth.login(request, newuser)
            return redirect('main:blogpage')

    return render(request, 'accounts/signup.html')
