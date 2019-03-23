from django import forms

from .models import Student


# class StudentForm(forms.Form):
#     name = forms.CharField(label='name', max_length=128)
#     sex = forms.ChoiceField(label='sex', choices=Student.SEX_ITEMS)
#     profession = forms.CharField(label='Profession', max_length=128)
#     email = froms.EmailField(label='Email', max_length=128)
#     qq = froms.CharField(label='QQ', max_length=128)
#     phone = forms.CharField(label='Phone', max_length=128)

class StudentForm(forms.ModelForm):
    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('Must Be Integer!')
        return int(cleaned_data)

    class Meta:
        model = Student
        fields = (
            'name', 'sex', 'profession', 'email', 'qq', 'phone'
        )



