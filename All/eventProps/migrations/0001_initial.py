# Generated by Django 4.1 on 2022-08-23 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='eventprop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('time', models.TimeField()),
                ('rate', models.PositiveSmallIntegerField()),
                ('likes', models.PositiveIntegerField(default=0)),
                ('dislikes', models.PositiveIntegerField(default=0)),
                ('website', models.CharField(max_length=255)),
            ],
        ),
    ]
