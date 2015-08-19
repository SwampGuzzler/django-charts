 # Place these imports at the top of the file
from django.shortcuts import get_object_or_404
from api.models import Character

# Put the imports at the top of views.py
from django.http import HttpResponseRedirect
from api.forms import CharacterForm

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse # Put this at the top of the file
def hello_world_view(request):
   return HttpResponse("Hello, world!")

def kirk_view(request, input_phrase):
    last_char = input_phrase[-1]
    # The context defines the variables used in the template. Our template
    # expects 'img_url' and 'phrase' variables to be provided.
    context = {
        'img_url': 'http://38.media.tumblr.com/2855c901c95471cef17f8985db402e44/tumblr_nlmrk6dzCC1qbxi45o1_250.gif',
        'phrase': input_phrase + (last_char * 5)
    }

def spock_view(request, input_phrase):
    last_char = input_phrase[-1]
    # The context defines the variables used in the template. Our template
    # expects 'img_url' and 'phrase' variables to be provided.
    context = {
        'img_url': 'http://khanaas.com/images/spock.jpgf',
        'phrase': input_phrase + (last_char * 5)
    }
    # render() creates an HTTP Response using the template (2nd argument)
    # and the variables provided by the context (3rd argument)



# This should look similar to kirk_view(), but it also takes the parameter 'input_character'
def get_character_view(request, input_character, input_phrase):
    # Get the character from the database by 'name' ('__iexact' means case insensitive)
    # If a match is not found, return a 404 page
    character_obj = get_object_or_404(Character, name__iexact=input_character)

    last_char = input_phrase[-1]
    context = {
        # Tweak the input phrase by repeating the last character
        'phrase' : input_phrase + (last_char * 5),
        'img_url': character_obj.img_url,
    }

    return render(request, 'api/khanaas_template.html', context)

def create_character_view(request):
    if request.method == 'POST':
        # Parse the POST data into a CharacterForm object
        form = CharacterForm(request.POST)

        # If the form is valid, save it.  If not valid, skip to
        # the render() at the bottom to render the form page again.
        # For example, since 'name' must be unique, submitting a
        # name that already exists results in is_valid() == False
        if form.is_valid():
            form.save()

            # After saving the submission, redirect to a page
            # with the new character image, with the phrase 'thanks'
            character_name = form.cleaned_data['name']
            return HttpResponseRedirect(character_name + '/thanks')
    else:
        # Not a POST, so it's a GET. Create a new form to render
        form = CharacterForm()

    # Render the 'create.html' template page with the CharacterForm instance
    return render(request, 'api/create.html', {'form': form})