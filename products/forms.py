from django import forms
from .models import Chair

class ChairForm(forms.ModelForm): #ModelForm means same display from model.py
	title		= forms.CharField(label='', 
					widget=forms.TextInput(attrs={"placeholder": "Your title"}))
	#email 		= forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Your email"}))
	description = forms.CharField(
						required=False, 
						widget=forms.Textarea(
							attrs={
								"class": "new-class-name two",
								"id": "my-id-for-textarea",
								"placeholder": "Your description",
								"rows": 10,
								"column": 120
							}
						)
					)
	class Meta:
		model = Chair
		fields = [
			'title',
			'description',
			'price'
		]

	# def clean_title(self, *args, **kwargs):
	# 	title = self.cleaned_data.get("title")
	# 	if not "CFE" in title:
	# 		raise forms.ValidationError("This is not a valid title")
	# 	if not "chair" in title:
	# 		raise forms.ValidationError("This is not a valid title")
	# 	return title

	# def clean_email(self, *args, **kwargs):
	# 	email = self.cleaned_data.get("email")
	# 	if not email.endswith("edu"):
	# 		raise forms.ValidationError("This is not a valid email")
	# 	return email

class RawProductForm(forms.Form): #standard django form
	title		= forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
	description = forms.CharField(
						required=False, 
						widget=forms.Textarea(
							attrs={
								"class": "new-class-name two",
								"id": "my-id-for-textarea",
								"placeholder": "Your description",
								"rows": 10,
								"column": 120
							}
						)
					)
	price 		= forms.DecimalField(initial=199.99)