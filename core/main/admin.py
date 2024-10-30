# main/admin.py
from django.contrib import admin
from modeltranslation.translator import register, TranslationOptions
from .models import Tour,Booking,SlideshowImage,Video,AboutUs,Gallery

class GalleryInline(admin.TabularInline):  # or admin.StackedInline
    model = Gallery
    extra = 1 
class TourAdmin(admin.ModelAdmin):
    inlines = [GalleryInline]
admin.site.register(Tour, TourAdmin)


class BookingAdmin(admin.ModelAdmin):
    list_display = ('tour', 'name', 'email', 'booking_date')
    fields = ('tour', 'name', 'email')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('tour', 'start_date', 'end_date', 'customer_name', 'customer_email')
    fields = ('tour', 'start_date', 'end_date', 'customer_name', 'customer_email')

admin.site.register(Booking, BookingAdmin)
admin.site.register(SlideshowImage)


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_file')
    search_fields = ('title',)




