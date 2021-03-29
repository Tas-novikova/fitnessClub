# Generated by Django 3.1.6 on 2021-02-27 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitnessclub', '0005_specializationtrainer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abonements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100, verbose_name='Вид')),
                ('quantity_visits', models.CharField(blank=True, max_length=20, verbose_name='Количество посещений')),
                ('quantity_days', models.PositiveIntegerField(verbose_name='Количество дней')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('note', models.TextField(verbose_name='Примечание')),
            ],
            options={
                'verbose_name': 'Абонемент',
                'verbose_name_plural': 'Абонементы',
            },
        ),
    ]
