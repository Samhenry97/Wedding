from django.shortcuts import render
from .forms import RSVPForm

def index(request):
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            rsvp = form.save()
    else:
        form = RSVPForm()
    return render(request, 'index.html', {'form': form, 'scroll': request.method == 'POST'})
