# Generated by Django 3.1.3 on 2021-11-07 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'admin'), ('FOOD_ATTENDANT', 'food_attendant'), ('NORMAL_USER', 'normal_user')], max_length=50, null=True),
        ),
    ]
