# Generated by Django 4.2.7 on 2024-01-26 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activationkeys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivationKeysAttached',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('activation_id', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='activationkeys.activationkeys')),
            ],
        ),
    ]
