# Generated by Django 2.1.7 on 2019-03-31 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trainer', '0003_auto_20190331_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='topic',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='trainerinfo',
            name='topic',
            field=models.CharField(default='', max_length=50),
        ),
    ]
