# Generated by Django 4.0.1 on 2022-01-14 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
    ]
