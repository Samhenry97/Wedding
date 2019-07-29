from django.shortcuts import render
from .forms import RSVPForm

def index(request):
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            rsvp = form.save()
    else:
        form = RSVPForm()

    context = {'form': form, 'scroll': request.method == 'POST'}
    context['dating'] = ['img/gallery/dating/{}.jpg'.format(i + 1) for i in range(12)]

    return render(request, 'index.html', context)

def rsvp(request):
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            rsvp = form.save()
    else:
        form = RSVPForm()

    return render(request, 'rsvp.html', {'form': form})
