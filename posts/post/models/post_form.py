from django.forms import ModelForm
from django.core.exceptions import NON_FIELD_ERRORS

from .post import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        error_messages = {
            NON_FIELD_ERRORS: {
                "unique_together": "%(model_name)s's %(field_labels)s are not unique.",
            }
        }