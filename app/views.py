from django.shortcuts import render, redirect
from .models import Quiz
from django.http import HttpResponse

# Create your views here.
def home(request):
    
    return render(request, 'app/index.html')

def quiz(request):

    allQuiz = Quiz.objects.order_by('?')[:10]
    return render(request, 'app/quiz.html', {"allQuiz": allQuiz})


def addquiz(request):
    return render(request, 'app/addquiz.html')

def createquiz(request):

    # get user inputs
    question = request.POST['question']
    option1 = request.POST['option1']
    option2 = request.POST['option2']
    option3 = request.POST['option3']
    option4 = request.POST['option4']
    answer = request.POST['answer']

    # instance of the model Quiz
    newQuiz = Quiz()

    if(question == "" or option1 == "" or option2 == "" or option3 == "" or option4 == "" or answer == ""):
        return redirect('/')

    else:
        newQuiz.question = question
        newQuiz.option1 = option1
        newQuiz.option2 = option2
        newQuiz.option3 = option3
        newQuiz.option4 = option4
        newQuiz.answer = answer

        newQuiz.save()

        return redirect('/')


def submitquiz(request):

    scores = 0

    if request.method == 'GET':

        for question_id, selected_option in request.GET.items():

            #get question
            question = Quiz.objects.get(pk=question_id)

            # Process each question's selected option here
            if selected_option == question.answer:
                scores += 10

        return render(request, 'app/result.html', {'scores': scores})
    
    else:
        return HttpResponse("Method not allowed")

    


