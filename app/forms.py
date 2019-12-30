from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:#model form bat buoc phai co meta
        model=Student
        fields='__all__'# lay tat ca truong o model
        # fields=['studentNo','name'] lay cac truong can thiet






class MailForm(forms.Form):
    to_email=forms.CharField()
    subject=forms.CharField()
    content=forms.CharField(required=False,widget=forms.Textarea)

    def clean_to_email(self):
        to_email=self.cleaned_data.get('to_email')
        if '@' not in to_email or '.com' not in to_email:
            raise forms.ValidationError('invalid email')
            return to_email
