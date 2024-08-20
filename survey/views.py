from django.shortcuts import render, get_object_or_404, redirect
from .models import Survey, Question, Answer
from .forms import SurveyForm, QuestionForm, AnswerForm

def home(request):
    surveys = Survey.objects.all()
    return render(request, 'survey/home.html', {'surveys': surveys})

def survey_detail(request, pk):
    survey = get_object_or_404(Survey, pk=pk)
    if request.method == 'POST':
        for question in survey.questions.all():
            answer = Answer(question=question)
            if question.question_type == 'text':
                answer.text = request.POST.get(f'question_{question.pk}')
            elif question.question_type == 'multiple_choice':
                answer.choice = request.POST.get(f'question_{question.pk}')
            elif question.question_type == 'rating':
                answer.rating = request.POST.get(f'question_{question.pk}')
            answer.save()
        return redirect('survey_thanks')
    return render(request, 'survey/survey_detail.html', {'survey': survey})

def create_survey(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SurveyForm()
    return render(request, 'survey/create_survey.html', {'form': form})

def survey_thanks(request):
    return render(request, 'survey/thanks.html')
