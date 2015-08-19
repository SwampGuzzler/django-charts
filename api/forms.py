from django.forms import ModelForm
from api.models import Character

class CharacterForm(ModelForm):

    class Meta:
        model = Character
        fields = ['name', 'img_url']