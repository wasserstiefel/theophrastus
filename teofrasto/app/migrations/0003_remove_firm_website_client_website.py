# Generated by Django 4.1 on 2022-08-07 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_firm_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firm',
            name='website',
        ),
        migrations.AddField(
            model_name='client',
            name='website',
            field=models.CharField(default='http://ww.website.com', max_length=255),
        ),
    ]
