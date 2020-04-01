from django import forms  
from AddressBook.models import Users 
  
class UseForm(forms.ModelForm):  
    class Meta:  
        model = Users  
        fields = "__all__"