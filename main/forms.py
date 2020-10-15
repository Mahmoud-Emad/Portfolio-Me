from django import forms 
from main.models import TestMe,Comments,ContactModel


class TestmeForm(forms.ModelForm):
    class Meta:
        model = TestMe
        fields = '__all__'
        exclude = ('slug',)

        widgets = {
            'Name': forms.TextInput(attrs={'style':'outline: none;box-sizing: border-box;height: 60px; width: 100%;margin-bottom: 20px;padding: 20px;border: 1px solid #404040; background-color: #282828; resize: none;color: #c18f59;','Placeholder':'Name Of Tester'}),
            'text': forms.Textarea(attrs={'style':'outline: none;box-sizing: border-box;height: 250px; width: 100%;margin-bottom: 20px;padding: 20px;border: 1px solid #404040; background-color: #282828; resize: none;color: #c18f59;','Placeholder':'Code Of Issue'}),
            'email': forms.TextInput(attrs={'style':'outline: none;box-sizing: border-box;height: 60px; width: 100%;margin-bottom: 20px;padding: 20px;border: 1px solid #404040; background-color: #282828; resize: none;color: #c18f59;','Placeholder':'Email Of Tester'}),
                  
        }
class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = '__all__'
        exclude = ('date',)

        widgets = {
            'Name': forms.TextInput(attrs={'style':'outline: none;box-sizing: border-box;height: 60px; width: 100%;margin-bottom: 20px;padding: 20px;border: 1px solid #404040; background-color: #282828; resize: none;color: #c18f59;','Placeholder':'Name ?'}),
            'Comment': forms.Textarea(attrs={'style':'outline: none;box-sizing: border-box;height: 100px; width: 100%;margin-bottom: 20px;padding: 20px;border: 1px solid #404040; background-color: #282828; resize: none;color: #c18f59;','Placeholder':'Comment ?'}),                  
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'
        exclude = ('date',)

        widgets = {
            'Name': forms.TextInput(attrs={'style':'outline: none;box-sizing: border-box;height: 60px; width: 50%;margin-bottom: 20px;padding: 20px;border: 1px solid #404040; background-color: #282828; resize: none;color: #c18f59;','Placeholder':'Name ?'}),
            'Message': forms.Textarea(attrs={'style':'outline: none;box-sizing: border-box;height: 100px; width: 100%;margin-bottom: 20px;padding: 20px;border: 1px solid #404040; background-color: #282828; resize: none;color: #c18f59;','Placeholder':'Message ?'}),
            'Email': forms.TextInput(attrs={'style':'outline: none;box-sizing: border-box;height: 60px; width: 49%;margin-bottom: 20px;padding: 20px;border: 1px solid #404040; background-color: #282828; resize: none;color: #c18f59;','Placeholder':'Email ?'}),                  
        }