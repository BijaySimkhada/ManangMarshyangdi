from django.contrib import admin
from .models import Booking, Contact, Gallery, Tournament, BookingHistory


# Register your models here.
class BookingHistoryAdmin(admin.ModelAdmin):
    list_display = ('booked_by', 'booked_date', 'booked_time', 'booked_at', 'deleted_at')
    list_filter = ('booked_date', 'deleted_at')



class BookingAdmin(admin.ModelAdmin):
    list_display = ('booked_by', 'booked_date', 'book_time', 'contact')
    list_filter = ('booked_date', )


class ContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'contact')


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('uploaded_at', 'caption')


admin.site.register(Booking, BookingAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Tournament)
admin.site.register(BookingHistory, BookingHistoryAdmin)