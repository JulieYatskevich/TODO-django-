# Generated by Django 4.0.5 on 2022-06-23 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='end',
            field=models.DateField(),
        ),
    ]
