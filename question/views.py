from django.shortcuts import render, Http404, get_object_or_404, redirect

# Create your views here.
from .models import Question, Answer, UserAnswer
from .forms import UserResponseForm


def single(request, id):
    print(id)
    if request.user.is_authenticated():


        # queryset = Question.objects.all().order_by("-timestamp")
        instance = get_object_or_404(Question, id=id)
        try:
            user_answer = UserAnswer.objects.get(user=request.user, question=instance)
        except UserAnswer.DoesNotExist:
            user_answer = UserAnswer()
        except UserAnswer.MultipleObjectsReturned:
            user_answer = UserAnswer.objects.filter(user=request.user, question=instance)[0]
        except:
            user_answer = UserAnswer()


        form = UserResponseForm(request.POST or None)
        if form.is_valid():
            print("Form is VALID!!!")
            print(form.cleaned_data)
            print(request.POST)

            question_id = form.cleaned_data.get('question_id')
            answer_id = form.cleaned_data.get('answer_id')
            important_level = form.cleaned_data.get('important_level')
            their_important_level = form.cleaned_data.get('their_important_level')
            their_answer_id = form.cleaned_data.get('their_answer_id')
            # answer_importance = form.cleaned_data.get('answer_importance')

            question_instance = Question.objects.get(id=question_id)
            answer_instance = Answer.objects.get(id=answer_id)

            print(answer_instance.text, "-", question_instance.text)

            user_answer.user = request.user
            user_answer.question = question_instance
            user_answer.my_answer = answer_instance
            user_answer.my_answer_importance = important_level
            if their_answer_id != -1:
                their_answer_instance = Answer.objects.get(id=their_answer_id)
                user_answer.their_answer = their_answer_instance
                user_answer.their_answer_importance =  their_important_level
            else:
                user_answer.their_answer = None
                user_answer.their_answer_importance = "Not Important!"
            user_answer.save()

            next_q = Question.objects.all().order_by("?").first()
            return redirect("question_single", id=next_q.id)
        else:
            print("Form is INVALID!")
            # print(form.cleaned_data)

        context = {
            "form": form,
            "instance": instance,
            'user_answer': user_answer
            # "queryset": queryset
        }
        return render(request, "question/single.html", context)
    else:
        print("User is not authenticated!")
        raise Http404


def home(request):
    if request.user.is_authenticated():
        form = UserResponseForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
            question_id = form.cleaned_data.get('question_id')
            answer_id = form.cleaned_data.get('answer_id')
            question_instance = Question.objects.get(id=question_id)
            answer_instance = Answer.objects.get(id=answer_id)
            print(answer_instance.text, "-", question_instance.text)
        else:
            print("zzzzzzz")
            # print(form.cleaned_data)

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
