from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RSVPForm
import telepot

def index(request):
    if request.method == 'POST':
        request.session['form'] = request.POST
        return redirect('rsvp')
    else:
        form = RSVPForm()

    context = {'form': form, 'scroll': request.method == 'POST'}
    context['dating'] = ['img/gallery/dating/{}.jpg'.format(i + 1) for i in range(12)]
    context['engage'] = ['img/gallery/engage/{}.jpg'.format(i + 1) for i in range(24)]

    return render(request, 'index.html', context)

def rsvp(request):
    if request.method == 'POST' or request.session.get('form'):
        form = RSVPForm(request.POST or request.session.get('form'))
        if request.session.get('form'):
            del request.session['form']
        if form.is_valid():
            data = form.cleaned_data
            sendTelegram('''\
<<<NEW RSVP>>>
Name: {} ({})
Guests: {}
Response: {}
Message: {}'''.format(data['name'], data['email'], data['number'], attending[data['attending']], data['message']))
            rsvp = form.save()
            messages.success(request, 'Thank you! Your response has been recorded.')
            return redirect('home')
        else:
            messages.warning(request, 'Please fix the errors below.')
    else:
        form = RSVPForm()

    return render(request, 'rsvp.html', {'form': form})

def sendTelegram(message):
    client.sendMessage('131453030', message)
    client.sendMessage('784263152', message)

attending = {'Both': 'Attending Ceremony and Reception', 'Ceremony': 'Attending Ceremony Only', 'None': 'Not Attending'}
client = telepot.Bot('928777303:AAExgj_w0_J1yTQLzE4EYHYE-IDTHv4-iKY')
