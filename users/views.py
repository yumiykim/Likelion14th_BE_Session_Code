from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render

from accounts.models import Profile


# Create your views here.
def mypage(request, id):
    profile_user = get_object_or_404(User, pk=id)
    profile = get_object_or_404(Profile, user=profile_user)

    # profile_user라는 객체를 context로 넘겨주는 이유 설명
    context = {
        'profile_user': profile_user,
        'profile': profile,
    }

    return render(request, 'users/mypage.html', context)
