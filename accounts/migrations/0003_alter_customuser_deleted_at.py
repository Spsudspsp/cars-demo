# Generated by Django 4.0.1 on 2022-01-14 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_deleted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
