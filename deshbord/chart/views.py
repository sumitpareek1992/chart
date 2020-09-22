from django.shortcuts import render, redirect
from chart.forms import CityForm
from chart.models import City


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = CityForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CityForm()
    return render(request, 'index.html', {'form': form})


def home(request):
    labels = []
    data = []
    male_l = []
    female_l = []
    other_l = []


    queryset = City.objects.all()
    for city in queryset:
        labels.append(city.name)
        data.append(city.population)
        male_l.append(city.male)
        female_l.append(city.female)
        other_l.append(city.other)


    return render(request, 'base.html',
                  {'labels': labels, 'data': data, 'male_l': male_l, 'female_l': female_l, 'other_l': other_l})
