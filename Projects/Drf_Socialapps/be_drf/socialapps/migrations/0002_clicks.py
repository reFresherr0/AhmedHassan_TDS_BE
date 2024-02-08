# Generated by Django 4.2.7 on 2024-01-26 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialapps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clicks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('social_app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socialapps.socialapps')),
            ],
        ),
    ]