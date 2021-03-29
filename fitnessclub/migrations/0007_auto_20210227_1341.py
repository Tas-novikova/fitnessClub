# Generated by Django 3.1.6 on 2021-02-27 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitnessclub', '0006_abonements'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abonements',
            name='note',
            field=models.TextField(blank=True, verbose_name='Примечание'),
        ),
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_card', models.PositiveIntegerField(verbose_name='Количество дней')),
                ('date_start', models.DateField(blank=True, null=True, verbose_name='Дата начала')),
                ('date_finish', models.DateField(blank=True, null=True, verbose_name='Дата окончания')),
                ('note', models.TextField(blank=True, verbose_name='Примечание')),
                ('abonement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fitnessclub.abonements')),
            ],
            options={
                'verbose_name': 'Карта',
                'verbose_name_plural': 'Карты',
            },
        ),
    ]