from django.contrib import admin

from customer.models import Customer, Appointment
from customer.views import appointment

# Register your models here.
admin.site.register(Customer)
admin.site.register(Appointment)
