# Generated by Django 4.2.7 on 2023-11-17 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='is_over',
            field=models.BooleanField(default=False),
        ),
    ]
