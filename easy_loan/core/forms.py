from django import forms
from easy_loan.users.models import Profile
from .models import Employment, Guarantor


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'first_name', 'last_name', 'birth_date', 'gender',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget = forms.HiddenInput()


class EmploymentForm(forms.ModelForm):
    class Meta:
        model = Employment
        fields = ('profile', 'company', 'start', 'end', 'salary', 'currently_working')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile'].widget = forms.HiddenInput()
        self.fields['currently_working'].required = False

    def clean(self):
        data = self.cleaned_data
        if not self.cleaned_data['end']:
            data['currently_working'] = True

        return data


class GuarantorForm(forms.ModelForm):
    class Meta:
        model = Guarantor
        fields = ('profile', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile'].widget = forms.HiddenInput()
