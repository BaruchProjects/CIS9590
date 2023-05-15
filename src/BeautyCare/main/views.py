import datetime
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Salons, Services, Appointments
from address.models import Address
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

@ensure_csrf_cookie
def home(request):
    # Render the service selection page when a POST request is made
    if request.method == 'POST':
        # Fetch services based on the salon ID provided in the POST data
        services = Services.objects.filter(salon_id=request.POST.get('salonID')).values('service_id', 'service_name', 'description', 'price')
        ctx = {'services': services, 'csrf_token': request.POST['csrfmiddlewaretoken']}
        return render(request, 'scheduling/service-selection.html', context=ctx)
    # Render the home page template for other requests
    return render(request, 'home/home.html')

def select_time(request):
    # Save the selected service ID in the session and render the appointment time page
    if request.method == 'POST':
        service_id = request.POST.get('svcChkbx')
        request.session['service_id'] = service_id
        return render(request, 'scheduling/appointment-time.html')
    # Redirect to the main home page for other requests
    return redirect('main-home')

@csrf_exempt
def available_times(request):
    # Extract the JSON data from the request body
    data = json.loads(request.body)
    # Parse the date provided in the data
    date = datetime.datetime.strptime(data['date'], '%Y-%m-%d')
    times_available = []
    # Fetch the salon associated with the selected service ID
    salon = Services.objects.filter(service_id=request.session['service_id']).first()
    # Fetch the services available at the salon
    services_available = Services.objects.filter(salon_id=salon.salon_id).values('service_id')
    # Fetch existing appointments for the selected services on the given date
    existing_appointments = Appointments.objects.filter(appointment_date__date=date.date(), service_id__in=services_available).values()
    # Create a set of already taken hours
    taken = {appointment['appointment_date'].hour for appointment in existing_appointments}

    # If the selected date is the current date, mark hours until the current hour as taken
    if date.date() == datetime.datetime.now().date():
        for hour in range(0, datetime.datetime.today().hour + 1):
            taken.add(hour)

    # Generate available time slots from 9 AM to 8 PM (inclusive)
    while date.hour <= 20:
        if date.hour >= 9:
            # Add time slots with availability status based on taken hours
            times_available.append({'text': date.strftime('%H:%M'), 'time': str(date), 'available': False if date.hour in taken else True})
        date = date + datetime.timedelta(hours=1)
    
    # Return the available time slots as JSON response
    return JsonResponse(times_available, safe=False)


def auto_complete(request):
    if request.GET.get('q'):
        q = request.GET['q']
        # Fetch salon data that starts with the provided query
        data = Salons.objects.filter(name__startswith=q).values('name', 'address', 'salon_id')
        json = []
        for item in data:
            out = {}
            # Fetch the associated address for each salon
            adr = Address.objects.filter(pk=item.get('address')).first()
            # Prepare the JSON response with salon name and address
            out['text'] = item['name'] + ' - ' + adr.raw
            out['id'] = item.get('salon_id')
            json.append(out)
        return JsonResponse(json, safe=False)
    else:
        HttpResponse("No cookies")