from django import forms
from .models import Course

class CourseModelForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = [
			'title',
		]

	#this validation on on form level
	def clean_title(self):  #pattern is clean_<field_name>
		title = self.cleaned_data.get('title')
		if title.lower() == 'abc':
			raise forms.ValidationError('This is not a valid title')
		return title