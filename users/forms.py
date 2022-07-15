from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name'
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        
        # update a specific attribute
        # self.fields['title'].widget.attrs.update({
        #     'class': 'input',
        #     'placeholder': 'add Title'
        # })
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})