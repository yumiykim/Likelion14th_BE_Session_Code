from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render

from accounts.models import Profile


# Create your views here.
def mypage(request, id):
    profile_user = get_object_or_404(User, pk=id)
    profile = get_object_or_404(Profile, user=profile_user)

    # profile_user는 조회한 유저 객체이고,
    # profile은 그 유저와 1:1로 연결된 추가 정보 객체이다.
    context = {
        'profile_user': profile_user,
        'profile': profile,
    }

    return render(request, 'users/mypage.html', context)
