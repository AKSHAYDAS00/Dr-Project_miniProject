from django.contrib import admin

# Register your models here.
from drapp.models import Department, Doctor, Booking

admin.site.register(Department)
admin.site.register(Doctor)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','p_name','p_email','doc_name','booking_date','booked_on')
admin.site.register(Booking,BookingAdmin)