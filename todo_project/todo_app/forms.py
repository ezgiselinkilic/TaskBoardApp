from django import forms
from .models import Todos,Project

class ListForm(forms.ModelForm):
    class Meta:
        model = Todos
        fields = ["title","description","actual_time","project_name"]
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["project_name"]

def clean_title(self):
    project_name = self.cleaned_data["project_name"]
    if not project_name:
        return project_name
    if not project_name[0].isupper():
        self.add_error("project_name", "Should start with an uppercase letter")

    if project_name.endswith("."):
        self.add_error("project_name", "Should not end with a full stop")

    if "&" in project_name:
        self.add_error("project_name", "Use 'and' instead of '&'")

    return project_name
