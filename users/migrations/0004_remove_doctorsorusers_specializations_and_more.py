# Generated by Django 4.2.10 on 2024-05-28 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_qualifications_owner_alter_skills_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorsorusers',
            name='specializations',
        ),
        migrations.AlterField(
            model_name='doctorsorusers',
            name='about_doctor',
            field=models.TextField(null=True),
        ),
    ]