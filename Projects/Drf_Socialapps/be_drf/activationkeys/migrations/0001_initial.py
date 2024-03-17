# Generated by Django 4.2.7 on 2024-01-26 12:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivationKeys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('Bands', 'Bands'), ('Cards', 'Cards'), ('Keychains', 'Keychains'), ('IICO tags', 'IICO tags')], max_length=50)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('activation_random_key', models.CharField(default=uuid.uuid4, editable=False, max_length=100, unique=True)),
                ('active', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]