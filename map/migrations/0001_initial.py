# Generated by Django 3.0.6 on 2020-06-08 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('classification', models.CharField(max_length=100)),
                ('event_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('gu', models.CharField(default='', max_length=100)),
                ('agency', models.CharField(default='', max_length=100)),
                ('user', models.CharField(default='', max_length=100)),
                ('cost', models.CharField(default='', max_length=100)),
                ('casting', models.CharField(default='', max_length=100)),
                ('information', models.TextField(default='')),
                ('etc', models.TextField(default='')),
                ('url', models.URLField(verbose_name='site url')),
                ('img', models.ImageField(default='photos/no_image.png', upload_to='photos')),
                ('tel', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
