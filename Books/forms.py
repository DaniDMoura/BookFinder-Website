from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

help_text_email = """
<ul>
  <li>Required field</li>
  <li>Must be a valid email address</li>
  <li>Will be used for account recovery</li>
</ul>
"""

help_text_first_name = """
<ul>
  <li>Required field</li>
  <li>Maximum 30 characters</li>
</ul>
"""

help_text_last_name = """
<ul>
  <li>Required field</li>
  <li>Maximum 30 characters</li>
</ul>
"""

class SignUpForm(UserCreationForm):
  email = forms.EmailField(max_length=254, required=True, help_text=help_text_email)
  first_name = forms.CharField(max_length=30, required=True, help_text=help_text_first_name)
  last_name = forms.CharField(max_length=30, required=True, help_text=help_text_last_name)

  class Meta:
    model = User
    fields = ('username','first_name','last_name','email','password1','password2')