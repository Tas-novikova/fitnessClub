from django.shortcuts import render, redirect
from django.db.models import Count
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from datetime import date
from .models import Gallery
from .models import Services
from .models import Trainers
from .models import SpecializationTrainer
from .models import Lessons
from .models import Cards
from .models import DAY
from .forms import LessonsForm
from django.core.exceptions import ValidationError
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
#def index(request):
 #   return render(request, 'fitnessclub/base1.html')


def index(request):
    return render(request, 'fitnessclub/index.html')


#def enter(request):
#    return render(request, 'fitnessclub/enter.html')


#def register(request):
#    return render(request, 'fitnessclub/registration.html')


def services(request):
    services = Services.objects.all()
    return render(request, 'fitnessclub/services.html', {'services': services})


class ServicesDetailView(DetailView):
    model = Services
    template_name = 'fitnessclub/services_details_view.html'
    context_object_name = 'service'

def price(request):
    return render(request, 'fitnessclub/price.html')


def timetable(request):
    return render(request, 'fitnessclub/timetable.html')


def trainers(request, Services=Services, SpecializationTrainer=SpecializationTrainer):
    trainers = Trainers.objects.all()
    specialization = SpecializationTrainer.objects.all
    choseService =''
    if request.method == 'POST':
        choseService = request.POST['choseService']

    services = Services.objects.all()
    trainerdata =''
    if choseService =='':
        trainerdata = SpecializationTrainer.objects.all()
    else:
        trainerdata = SpecializationTrainer.objects.filter(service__id=choseService)
    return render(request, 'fitnessclub/trainers.html', {'services': services, 'trainerdata': trainerdata, 'choseService': choseService})


def photos(request):
    photos = Gallery.objects.order_by('id')
    return render(request, 'fitnessclub/photos.html', {'photos': photos})


def contacts(request):
    return render(request, 'fitnessclub/contacts.html')


def gym(request):
    return render(request, 'fitnessclub/gym.html')


def functionalTraining(request):
    return render(request, 'fitnessclub/functionalTraining.html')


def pilates(request):
    return render(request, 'fitnessclub/pilates.html')


def bodySculpt(request):
    return render(request, 'fitnessclub/bodySculpt.html')


def lowerBody(request):
    return render(request, 'fitnessclub/lowerBody.html')


def upperBody(request):
    return render(request, 'fitnessclub/upperBody.html')


def stepAerobics(request):
    return render(request, 'fitnessclub/stepAerobics.html')


def stretching(request):
    return render(request, 'fitnessclub/stretching.html')


def tabsStretching(request):
    return render(request, 'fitnessclub/tabsStretching.html')


def checkCard(request, Cards=Cards):
    checkCard = ''
    if request.method == 'POST':
        checkCard = request.POST['checkCard']
    card = Cards.objects.all()
    carddata = ''
    status = 0
    if checkCard == '':
        carddata = ''
    else:

        if Cards.objects.filter(number_card=checkCard).count() == 0:
            carddata = ''
            status = 1
        else:
            carddata = Cards.objects.get(number_card=checkCard)
            #cardX = Cards.objects.get(number_card=checkCard)
            if carddata.date_finish < date.today():
                status = 2
            else:
                status = 3
    return render(request, 'fitnessclub/checkCard.html', {'card': card, 'carddata': carddata, 'checkCard': checkCard,  'status': status})


def freeLesson(request):
    error = ''
    leng = ''
    if request.method == 'POST':
        #form = LessonsForm(request.POST)
        obj = LessonsForm()
        obj.phone = request.POST['phone']
        obj.name = request.POST['name']
        obj.textMessage = request.POST['textMessage']
        obj.days = request.POST['days']
        leng = len(obj.phone)
        if obj.is_valid():
            obj.save()
            return redirect('freeLesson')
        else:
            if leng != 9 and obj.phone.isdigit():
                error = 'Введите только 9 цифр'
            else:
                error = 'Форма заполнена не корректно'
           #error = 'Форма заполнена не корректно'


    form = LessonsForm()

    data = {
        'form': form,
        'error': error,
        'leng': leng
    }

    return render(request, 'fitnessclub/freeLesson.html', data)


def statistic(request):
    stat = Lessons.objects.values('days').annotate(dcount=Count('days')).order_by('-dcount')
    for dct in stat:
        for templ in DAY:
            if templ[0]==dct['days']:
                dct['days_name']=templ[1]

    return render(request, 'fitnessclub/statistic.html', {'stat': stat})


#def tableFreeLesson(request):
 #   tableFreeLesson = Lessons.objects.order_by('-id')
  #  return render(request, 'fitnessclub/tableFreeLesson.html', {'tableFreeLesson': tableFreeLesson})





