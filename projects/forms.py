from django.forms import forms, ModelForm
from projects.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "description",
            "owner",
        ]
