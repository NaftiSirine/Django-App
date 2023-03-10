# Generated by Django 4.1.6 on 2023-02-06 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import events.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=250, verbose_name='Title')),
                ('description', models.TextField()),
                ('state', models.BooleanField(default=False)),
                ('imageEvent', models.ImageField(blank=True, upload_to='images/')),
                ('nbParticipants', models.IntegerField(default=0)),
                ('category', models.CharField(choices=[('Music', 'Music'), ('sport', 'Sport'), ('Cinema', 'Cinema')], max_length=10)),
                ('dateEvent', models.DateField(validators=[events.models.is_date_valid])),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updatedAt', models.DateField(auto_now=True)),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datePart', models.DateField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Participations',
                'unique_together': {('person', 'event')},
            },
        ),
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(related_name='participations', through='events.Participation', to=settings.AUTH_USER_MODEL),
        ),
    ]
