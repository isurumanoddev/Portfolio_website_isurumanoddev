from django.forms import ModelForm
from .models import Projects,Messages,Skills


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

class ContactForm(ModelForm):
    class Meta:
        model = Messages
        fields = "__all__"
        exclude = ["is_read"]

    def __init__(self, *args, **kwargs):
        super(ContactForm,self).__init__(*args,**kwargs)

        self.fields["name"].widget.attrs.update({'class':'input'})
        self.fields["email"].widget.attrs.update({'class':'input'})
        self.fields["subject"].widget.attrs.update({'class':'input'})
        self.fields["body"].widget.attrs.update({'class':'textarea'})

class SkillForm(ModelForm):
    class Meta:
        model = Skills
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(SkillForm,self).__init__(*args,**kwargs)

        self.fields["title"].widget.attrs.update({'class':'form-control'})
        self.fields["body"].widget.attrs.update({'class':'form-control'})