# Generated by Django 3.0 on 2020-09-22 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0002_auto_20200922_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='female',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='hotels',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='male',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='other',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='population',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
