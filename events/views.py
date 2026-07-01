from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .models import Registration
from .forms import RegistrationForm

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import EventSerializer, RegistrationSerializer

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.event = event
            registration.save()
            return redirect('event_list')

    else:
        form = RegistrationForm()

    return render(request, 'events/register.html', {
        'form': form,
        'event': event
    })

def registration_list(request):
    registrations = Registration.objects.all()
    return render(request, 'events/registration_list.html', {
        'registrations': registrations
    })

def cancel_registration(request, registration_id):
    registration = get_object_or_404(Registration, id=registration_id)
    registration.delete()
    return redirect('registration_list')

@api_view(['GET'])
def api_event_list(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    serializer = EventSerializer(event)
    return Response(serializer.data)

@api_view(['GET'])
def api_registration_list(request):
    registrations = Registration.objects.all()
    serializer = RegistrationSerializer(registrations, many=True)
    return Response(serializer.data)