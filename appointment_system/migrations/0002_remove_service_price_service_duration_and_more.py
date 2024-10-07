# Generated by Django 4.2.4 on 2024-10-07 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment_system', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='price',
        ),
        migrations.AddField(
            model_name='service',
            name='duration',
            field=models.PositiveIntegerField(default=60),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(),
        ),
    ]
