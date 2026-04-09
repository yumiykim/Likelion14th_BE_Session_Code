from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from main.models import Blog


# Create your views here.
def mypage(request, id):
    user = get_object_or_404(User, pk=id)

    # user가 쓴 블로그 글만 가져오기 할지 말지 고민 중
    # 다음 주 은호 세션에서 하는 게 더 나을 것 같기도
    # wrote_blog = Blog.objects.filter(user=user)

    # user라는 객체를 context로 넘겨주는 이유도 설명해주세요
    context = {
        'user': user,
        # 'wrote_blog': wrote_blog,
    }

    return render(request, 'users/mypage.html', context)