from django.forms import ModelForm
from .models import Projects


class ProjectForm(ModelForm):
    class Meta:
        model = Projects
        fields = ["title","thumbnail","body","project_description","github_link"]

    def __init__(self, *args, **kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)

        self.fields["title"].widget.attrs.update({'class':'input'})
        self.fields["body"].widget.attrs.update({'class':'input'})
        self.fields["thumbnail"].widget.attrs.update({'class':'input'})
        self.fields["project_description"].widget.attrs.update({'class':'textarea'})
        self.fields["github_link"].widget.attrs.update({'class':'input'})