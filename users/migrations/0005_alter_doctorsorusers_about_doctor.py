# Generated by Django 4.2.10 on 2024-05-28 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_doctorsorusers_specializations_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorsorusers',
            name='about_doctor',
            field=models.TextField(blank=True, null=True),
        ),
    ]