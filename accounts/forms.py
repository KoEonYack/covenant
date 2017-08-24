from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class SignupForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        label="ID",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '아이디를 입력해 주세요'}),
    )

    email = forms.EmailField(
        required=True,
        label="이메일",
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': '이메일 주소를 입력해주세요'}),
    )

    password1 = forms.CharField(
        required=True,
        label="비밀번호",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '숫자와 문자를 포함해 8자리 이상을 입력해주세요'}),
    )
    
    password2 = forms.CharField(
        required=True,
        label="비밀번호 확인",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '같은 비밀번호를 다시 입력해주세요.'}),
    )

    realname = forms.CharField(
        required=True,
        label="실명",
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': '실명을 입력해주세요'}),
    )

    # address = forms.CharField()
    student_number = forms.CharField(
        required=True,
        label="학번",
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': '학번을 입력해 주새요'}),
    )

    class_name=forms.CharField(
        required=True,
        label="분반 명",
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': '분반이름을 입력해 주세요'}),
   )

    class Meta:
        model = Profile
        fields=['username', 'realname', 'student_number', 'class_name']


