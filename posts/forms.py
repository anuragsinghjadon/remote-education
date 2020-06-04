from django import forms
from .models import Post

class PostForm(forms.ModelForm):
  descriptions = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter Title'
      }
    )
  )

  documents = forms.FileField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'form-control form-control-lg',
      }
    )
  )

  class Meta:
    model = Post
    fields = ('descriptions', 'documents', )


  def clean_description(self, *args, **kwargs):
    descriptions = self.cleaned_data.get('descriptions')
    if not descriptions.strip():
      raise forms.ValidationError('Invalid description!')
    else:
      return descriptions

