# Generated by Django 3.1.6 on 2021-02-27 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitnessclub', '0004_auto_20210223_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecializationTrainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, verbose_name='Примечание')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fitnessclub.services')),
                ('trainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fitnessclub.trainers')),
            ],
            options={
                'verbose_name': 'Специализация тренера',
                'verbose_name_plural': 'Специализации тренеров',
            },
        ),
    ]