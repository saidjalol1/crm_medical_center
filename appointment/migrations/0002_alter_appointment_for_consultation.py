# Generated by Django 4.2.10 on 2024-05-29 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='for_consultation',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]