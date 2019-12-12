from django.forms import ModelForm
from tweets.models import Reply


class NewReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['content']