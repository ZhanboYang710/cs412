# quotes/views.py
# view functions to handle URL requests for quotes app

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
import random

# Global Scope Variables
quotes = [
    "Time goes on. So whatever you're going to do, do it. Do it now. Don't wait.",
    "Reputation, you know – a lifetime to build, seconds to destroy.",
    "The saddest thing in life is wasted talent",
]

images = [
    "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia.nbcnewyork.com%2F2023%2F05%2F230509-robert-de-niro-getty.jpg%3Fquality%3D85%26strip%3Dall%26resize%3D1200%252C675&f=1&nofb=1&ipt=1482701af16a795bb3b2a4700fe05b946b1b5fbe5808271f12dcbeced266816a&ipo=images",
    "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fm.media-amazon.com%2Fimages%2FM%2FMV5BMjAwNDU3MzcyOV5BMl5BanBnXkFtZTcwMjc0MTIxMw%40%40._V1_FMjpg_UX1000_.jpg&f=1&nofb=1&ipt=490dff6f1e84e54969981818828bd72e5d381c56962a9629a7d23550aa0edaa0&ipo=images",
    "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fzoomboola.com%2Fimages%2Fcatalog%2F2022%2F2%2Frobert-de-niro_3.jpg&f=1&nofb=1&ipt=f0a3a6b8d254fb005b79f730f2954740fc07826005505db32656ec1eb12b9a65&ipo=images",
]

length = len(quotes) - 1

# functions

def quote(request):
    template_name = "quotes/quote.html"

    num_1 = random.randint(0, length)
    num_2 = random.randint(0, length)


    context = {
        "qts_display" : quotes[num_1],
        "img_display" : images[num_2],
    }

    return render(request, template_name, context)


def show_all(request):
    template_name = "quotes/show_all.html"

    context = {
        "quote_1" : quotes[0],
        "image_1" : images[0],
        "quote_2" : quotes[1],
        "image_2" : images[1],
        "quote_3" : quotes[2],
        "image_3" : images[2],
    }        

    return render(request, template_name, context)


def about(request):
    template_name = "quotes/about.html"

    context = {
        "description" : "Robert Anthony De Niro is one of the best actors in film who is stil alive in his generation. He received two Academy Awards. "
    }

    return render(request, template_name, context)