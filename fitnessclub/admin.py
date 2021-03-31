from django.contrib import admin
from .models import Gallery, Services, Trainers, SpecializationTrainer, Abonements, Cards, Lessons

#admin.site.register(Gallery)
#admin.site.register(Services)
#admin.site.register(Trainers)

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('photo', 'description')
    save_on_top = True


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo')
    save_on_top = True


@admin.register(Trainers)
class TrainersAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'dateBirth', 'dateStartJob', 'description', 'photo', 'note')
    fields = [('last_name', 'first_name'), ('dateBirth', 'dateStartJob'), 'photo', 'description', 'note']
    save_on_top = True


@admin.register(SpecializationTrainer)
class SpecializationTrainerAdmin(admin.ModelAdmin):
    list_display = ('trainer', 'service', 'note')
    list_filter = ['service', 'trainer']
    save_on_top = True


#@admin.register(Abonements)
#class AbonementsAdmin(admin.ModelAdmin):
#    list_display = ('type', 'quantity_visits', 'quantity_days', 'price', 'note')
#    fields = ['type', ('quantity_visits', 'quantity_days'), 'price', 'note']
#    list_filter = ['type']

@admin.register(Cards)
class CardsAdmin(admin.ModelAdmin):
    list_display = ('number_card', 'abonement', 'date_start', 'date_finish', 'note')
    fields = ['number_card', 'abonement', ('date_start', 'date_finish'),  'note']
    search_fields = ['number_card']
    list_filter = ['date_finish', 'abonement']
    save_on_top = True


@admin.register(Lessons)
class LessonsAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'days', 'textMessage', 'date_in', 'time_in', 'note')
    fields = ['name', 'phone', 'days', 'textMessage',  'note']
    readonly_fields = ['date_in', 'time_in']
    list_filter = ['days', 'date_in', 'note']
    ordering = ['-date_in', '-time_in']
    search_fields = ['phone']
    save_on_top = True
    list_editable = ['note']


admin.site.site_title = 'Администрирование сайта'
admin.site.site_header = 'Администрирование сайта'