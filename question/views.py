from django.shortcuts import render, Http404

# Create your views here.
from .models import Question
from .forms import UserResponseForm

def home(request):


    if request.user.is_authenticated():
        form = UserResponseForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)

        queryset = Question.objects.all().order_by("-timestamp")
        instance = queryset[0]

        context = {
            "form": form,
            "instance": instance,
            # "queryset": queryset
        }
        return render(request, "question/home.html", context)
    else:
        raise Http404
