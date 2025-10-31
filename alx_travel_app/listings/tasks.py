from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_booking_confirmation_email(email, booking_id):
    subject = f"Booking Confirmation - #{booking_id}"
    message = f"Hello,\n\nYour booking (ID: {booking_id}) has been successfully created!\n\nThank you for choosing us!"
    from_email = None  # Uses DEFAULT_FROM_EMAIL
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
    return f"Email sent to {email} for booking #{booking_id}"
