from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class SignupForm(UserCreationForm):
    phone_number = forms.CharField()
    address = forms.CharField()
    student_number = forms.CharField()
    class_name=forms.CharField()

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', )

    def save(self):
        user = super().save()
        profile = Profile.objects.create(
            user = user,
            phone_number = self.cleaned_data['phone_number'],
            address = self.cleaned_data['address'], # 이것을 이름으로 바꾸면 되지 않을까?
            student_number = self.cleaned_data['student_number'],
            class_name = self.cleaned_data['class_name'],
        )
        return user


