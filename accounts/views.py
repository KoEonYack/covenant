# accounts/views.py
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import SignupForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL)  # default : "/accounts/login/" 회원 가입에 성공하면 로그인 페이지로 이동
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

