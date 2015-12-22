from django.shortcuts import render
from django.conf import settings

import requests
# Create your views here.
from .forms import SubmitEmbed
from .serializer import EmbedSerializer

def save_embed(request):

    if request.method == "POST":
        form = SubmitEmbed(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            print(url)
            r = requests.get('http://api.embed.ly/1/oembed?key=' + settings.EMBEDLY_KEY + '&url=' + url)
            json = r.json()
            serializer = EmbedSerializer(data=json)
            if serializer.is_valid():
                embed = serializer.save()
                return render(request, 'embedly/embeds.html', {'embed': embed})
    else:
        form = SubmitEmbed()

    return render(request, 'embedly/index.html', {'form': form})
