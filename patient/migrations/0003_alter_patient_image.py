# Generated by Django 5.1.1 on 2025-04-18 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_alter_patient_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='image',
            field=models.ImageField(upload_to='patient/images/'),
        ),
    ]
