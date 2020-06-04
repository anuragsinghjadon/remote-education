from django import forms
from .models import Profile, Education, Experience


GENDER_CHOICES = [
  ('Male', 'Male'),
  ('Female', 'Female')
]

PROFESSION_CHOICES = [
  ('Student or Learning', 'Student or Learning'),
  ('Instructor or Teacher', 'Instructor or Teacher'),
  ('Other', 'Other')
]

DEGREE_CHOICES = [
  ('IT', 'Information Technologies'),
  ('Bussiness Managment', 'Bussiness Managment'),
  ('Digital Marketing', 'Digital Marketing'),
  ('Computer Science', 'Computer Science'),
  ('Civil Engineering', 'Civil Engineering'),
  ('AI', 'Artificial & Inteligence'),
  ('Other', 'Other')
]


class ProfileForm(forms.ModelForm):
  name = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter Name'
      }
    )
  )

  contact_number = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter Contact Number'
      }
    )
  )

  gender = forms.ChoiceField(
    choices=GENDER_CHOICES,
    widget=forms.Select(
      attrs={
        'class': 'form-control form-control-lg',
      }
    )
  )


  linkedin = forms.URLField(
    required=False,
    widget=forms.URLInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter linkedin Url'
      }
    )
  )


  profession = forms.ChoiceField(
    choices=PROFESSION_CHOICES,
    widget=forms.Select(
      attrs={
        'class': 'form-control form-control-lg',
      }
    )
  )

  
  country = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter Country'
      }
    )
  )

  skills = forms.CharField(
    required=False,
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter Skills'
      }
    )
  )

  image = forms.ImageField(
    required=False,
    widget=forms.FileInput(
      attrs={
        'class': 'form-control form-control-lg',
      }
    )
  )


  class Meta:
    model = Profile
    fields = ('name', 'contact_number', 'gender', 'linkedin', 'profession', 'country', 'skills', 'image')



class EducationForm(forms.ModelForm):
  college = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter College'
      }
    )
  )

  degree = forms.ChoiceField(
    choices=DEGREE_CHOICES,
    widget=forms.Select(
      attrs={
        'class': 'form-control form-control-lg',
      }
    )
  )

  started_at = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-lg',
      }
    )
  )

  ended_at = forms.CharField(
    required=False,
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-lg',
      }
    )
  )

  bio = forms.CharField(
    widget=forms.Textarea(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter bio',
        'rows': 4
      }
    )
  )

  is_currently_studying = forms.BooleanField(
    required=False,
    label='currently studying',
    widget=forms.CheckboxInput(
      attrs={
        'class': 'form-check',
      }
    )
  )
  class Meta:
    model = Education
    fields = ('college', 'degree', 'started_at', 'ended_at','bio', 'is_currently_studying',)


class ExperienceForm(forms.ModelForm):
  college = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter college'
      }
    )
  )

  profession = forms.ChoiceField(
    choices=PROFESSION_CHOICES,
    widget=forms.Select(
      attrs={
        'class': 'form-control form-control-lg',
      }
    )
  )


  research = forms.CharField(
    widget=forms.Textarea(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter research',
        'rows': 4
      }
    )
  )

  is_currently_teacher = forms.BooleanField(
    required=False,
    label='currently working',
    widget=forms.CheckboxInput(
      attrs={
        'class': 'form-check',
      }
    )
  )
  class Meta:
    model = Experience
    fields = ('college', 'profession','research' ,'is_currently_teacher',)


