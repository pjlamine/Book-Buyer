from django import forms

class isbnForm(forms.Form):
    isbn = forms.CharField(max_length = 13)

# class buyForm(forms.Form):
#     submit_button = SubmitButtonField(label="", initial=u"Buy")
