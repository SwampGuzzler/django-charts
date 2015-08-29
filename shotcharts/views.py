 # Place these imports at the top of the file
from django.shortcuts import get_object_or_404
from api.models import Chart

import matplotlib.pyplot as plt, mpld3

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

def chart_template(request, disease_id, state_id):

    return HttpResponse(request_url)


    # 1. Get Data back via requests or HttpResponse or get_object_or_404
    # 2. Arrange data, create pandas dataframe, get player picture
    # 3. Draw Court
    # 4. Create shotchart (via seaborn/mpld3/matplotlib.pyplot)
    # 5. Combine court, pic, chart and show() it
    # 6. mpld3 toHtml the fig, pass that into chart_template somehow

    # 6b. We could also do mpld3.save_html(figure, newFile.html)

    # plt.plot([3,1,4,1,5], 'ks-', mec='w', mew=5, ms=20)
    # html_chart = mpld3.fig_to_html(fig)
    # mpld3.show()

    season_data = get_object_or_404(Chart)
    #season_data = get_object_or_404(Chart, relevantdisease__pk=disease_id)


    context = {
        'name' : season_data.playerName, # (or whatever the name property is called)
        'img_url': season_data.img_url,
        'chart_type': 'hex' # necessary?
    }
    return render(request, "chart_template.html", context)

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