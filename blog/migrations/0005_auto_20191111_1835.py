# Generated by Django 2.1 on 2019-11-11 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191111_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='address',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='phone',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
