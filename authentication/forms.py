from django import forms

# Create your forms

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)

class AdminLoginForm(forms.Form):
    url='adminLogin'
    username=forms.CharField(max_length=100, 
                             label='Username')

    password=forms.CharField(max_length=100,label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    # test=forms.CharField(max_length=100,label='Test',widget=forms.TextInput(attrs={'class':'form-control'}))

    def clean_username(self):
        username=self.cleaned_data['username']
        if username=='admin':
            return username
        else:
            raise forms.ValidationError('username is incorrect')
        
class imageForm(forms.Form):
    username=forms.CharField(max_length=100, label='Username')
    # name=forms.CharField(max_length=100, label='Username')
    image = forms.ImageField()



