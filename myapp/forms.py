from django import forms


class loginform(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)


class DealerSignupForm(forms.Form):
    firstname=forms.CharField(max_length =30)
    lastname=forms.CharField(max_length=30)
    email=forms.EmailField()
    contact=forms.IntegerField()


class UserSignupForm(forms.Form):
    firstname=forms.CharField(max_length =30)
    lastname=forms.CharField(max_length=30)
    email=forms.EmailField()
    contact=forms.IntegerField()