# Generated by Django 2.1.7 on 2019-03-31 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PracticeQues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=400)),
                ('studentAns', models.CharField(default='', max_length=264)),
                ('rightAns', models.CharField(max_length=264)),
            ],
        ),
    ]
