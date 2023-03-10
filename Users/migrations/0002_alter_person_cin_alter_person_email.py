# Generated by Django 4.1.6 on 2023-02-06 15:26

import Users.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='cin',
            field=models.CharField(max_length=8, primary_key=True, serialize=False, validators=[django.core.validators.MaxLengthValidator(8), django.core.validators.MinLengthValidator(8)], verbose_name='Cin'),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[Users.models.is_mail_esprit], verbose_name='Email'),
        ),
    ]
