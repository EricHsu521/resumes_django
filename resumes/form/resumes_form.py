from django.forms import ModelForm
from django.forms.widgets import Textarea, TextInput
from resumes.models import Resume

class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = ["title", "price", "desc"]
        widgets = {
            "title": TextInput(),
            "price": TextInput(),
            "desc": Textarea(attrs={"row": 5}),
        }
        labels = {
            "title": "Title",
            "price": "Priec",
            "desc": "Desc",
        }