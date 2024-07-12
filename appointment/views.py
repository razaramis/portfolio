from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import AppointmentForm
from django.conf import settings

def appointment_view(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            # Construct the email message
            message = f"Message: {form.cleaned_data['message']}\n\n"
            message += f"Sender's Email: {form.cleaned_data['email']}"
            # Send email
            send_mail(
                'New Appointment Request',
                message,
                form.cleaned_data['email'],
                [settings.EMAIL_HOST_USER],
                fail_silently = False,
            )
            return redirect('success')
    else:
        form = AppointmentForm()
    return render(request, 'appointment/appointment_form.html', {'form': form})

def success_view(request):
    return render(request, 'appointment/success.html')