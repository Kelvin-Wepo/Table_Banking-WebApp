# Generated by Django 3.2 on 2024-03-28 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savingsapp', '0003_auto_20240328_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='telephone',
            field=models.CharField(max_length=30),
        ),
    ]
