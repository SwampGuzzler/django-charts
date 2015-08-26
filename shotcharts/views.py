 # Place these imports at the top of the file
from django.shortcuts import get_object_or_404
from api.models import Chart

# Put the imports at the top of views.py
from django.http import HttpResponseRedirect
from api.forms import ChartForm

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse # Put this at the top of the file
def hello_world_view(request):
   return HttpResponse("Hello, world!")

def spock_view(request, input_phrase):
    last_char = input_phrase[-1]
    # The context defines the variables used in the template. Our template
    # expects 'img_url' and 'phrase' variables to be provided.
    context = {
        'img_url': 'catPic.png',
        'phrase': input_phrase + (last_char * 5)
    }

# def get_chart_view(request, input_chart, input_phrase):
#     # Get the chart from the database by 'name' ('__iexact' means case insensitive)
#     # If a match is not found, return a 404 page
#     chart_obj = get_object_or_404(Chart, name__iexact=input_chart)

#     last_char = input_phrase[-1]
#     context = {
#         # Tweak the input phrase by repeating the last character
#         'phrase' : input_phrase + (last_char * 5),
#         'img_url': chart_obj.img_url,
#     }

#     return render(request, 'api/khanaas_template.html', context)

def create_chart_view(request):
    if request.method == 'POST':
        # Parse the POST data into a ChartForm object
        form =ChartForm(request.POST)
    else:
        # Not a POST, so it's a GET. Create a new form to render
        form = ChartForm()

    # Render the 'create.html' template page with the ChartForm instance
    return render(request, 'api/create.html', {'form': form})