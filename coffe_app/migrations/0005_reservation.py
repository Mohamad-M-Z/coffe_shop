# Generated by Django 5.1.2 on 2024-11-01 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffe_app', '0004_contact_newsletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateTimeField(auto_now=True)),
                ('time', models.TimeField(blank=True)),
                ('person', models.IntegerField(choices=[(1, 'person'), (2, 'person'), (3, 'person'), (4, 'person'), (5, 'Leading candidate')], default=1)),
            ],
        ),
    ]