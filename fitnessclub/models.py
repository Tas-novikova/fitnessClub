from django.db import models
from django.utils import timezone
from  django.contrib.auth.models  import  User


class Gallery(models.Model):
    photo = models.CharField('Фото', max_length=100)
    description = models.CharField('Описание', max_length=100)

# При получении объекта из базы данных всегда возвращается ID записи.
# С такой информацией особо ничего не сделать, поэтому лучше в классе модели дописывать магический метод «__str__».
# В нём можно указать какое значение будет возвращается при получении объекта из БД.
    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Галерея'


class Services(models.Model):
    title = models.CharField('Название', max_length=100)
    photo = models.CharField('Фото', max_length=100)
    description = models.TextField('Описание')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Trainers(models.Model):
    last_name = models.CharField('Фамилия', max_length=100)
    first_name = models.CharField('Имя', max_length=100)
    photo = models.CharField('Фото', max_length=100)
    dateBirth = models.DateField('Дата рождения', blank=True, null=True)
    dateStartJob = models.DateField('Дата приема на работу', blank=True, null=True)
    description = models.TextField('Описание', blank=True)
    note = models.TextField('Примечание', blank=True)

    def __str__(self):
        return '%s %s' % (self.last_name, self.first_name)


    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренеры'


class SpecializationTrainer(models.Model):
    trainer = models.ForeignKey('Trainers', on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey('Services', on_delete=models.SET_NULL, null=True)
    note = models.TextField('Примечание', blank=True)

    def __str__(self):
        return '%s %s' % (self.trainer, self.service)


    class Meta:
        verbose_name = 'Специализация тренера'
        verbose_name_plural = 'Специализации тренеров'


class Abonements(models.Model):
    type = models.CharField('Вид', max_length=100)
    quantity_visits = models.CharField('Количество посещений', max_length=20, blank=True)
    quantity_days = models.PositiveIntegerField('Количество дней')
    price = models.PositiveIntegerField('Цена')
    note = models.TextField('Примечание', blank=True)

    def __str__(self):
        return '%s - %s занятий' % (self.type, self.quantity_visits)


    class Meta:
        verbose_name = 'Абонемент'
        verbose_name_plural = 'Абонементы'


class Cards(models.Model):
    number_card = models.CharField('Номер карты', max_length=15)
    abonement = models.ForeignKey('Abonements', on_delete=models.SET_NULL, null=True)
    date_start = models.DateField('Дата начала', blank=True, null=True)
    date_finish = models.DateField('Дата окончания', blank=True, null=True)
    note = models.TextField('Примечание', blank=True)

    def __str__(self):
        return '%s' % (self.number_card)


    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'


DAY = ((None, "Выберете удобное для Вас время"),
        ('1', "пн-пт утро"),
        ('2', "пн-пт вечер"),
        ('3', "сб-вс утро"),
        ('4', "сб-вс день"))


class Lessons(models.Model):
    name = models.CharField('Имя', max_length=100)
    phone = models.IntegerField('Телефон')
    days = models.CharField('Дни', max_length=30, choices=DAY, blank=False, default=None)
    textMessage = models.TextField('Текст сообщения', blank=True, null=True)
    date_in = models.DateField('Дата', null=True, auto_now=True)
    time_in = models.TimeField('Время', null=True, auto_now=True)
    note = models.CharField('Примечание', max_length=255, blank=True)
    status = models.IntegerField(default=0, verbose_name='status')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Пробная тренировка'
        verbose_name_plural = 'Пробные тренировки'