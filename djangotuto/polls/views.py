# from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.db.models import F
from django.http import HttpResponseRedirect    # HttpResponse is not used anymore
# from django.template import loader
from django.urls import reverse
### Import Generic View Library ###
### Now, the views.py code will be totally different due to this library ###
from django.views import generic
from django.utils import timezone

from .models import Question, Choice


#def index(request):
    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    ### Replace loader + HttpResponse with render() ###
    # template = loader.get_template("polls/index.html")
    
    # context = {"latest_question_list": latest_question_list}
    # output = ", ".join([q.question_txt for q in latest_question_list])
    
    ### Replace loader + HttpResponse with render() ###
    # return HttpResponse(template.render(context, request))

    # return HttpResponse(template.render(context, request))

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

#def detail(request, question_id):
    # try:
    #    question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
    
    ### Simplify try:except with get_object_or_404() ###
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, "polls/detail.html", {"question":question})
    # return HttpResponse("You're looking at question %s" % question_id)

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


#def results(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    # response = "You're looking at results of question %s"
    # return render(request, "polls/results.html", {"question": question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
                request, 
                "polls/detail.html",
                {
                    "question": question,
                    "error_message": "You didn't select a choice",
                },
            )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
