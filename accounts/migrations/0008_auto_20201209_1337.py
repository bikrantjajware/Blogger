# Generated by Django 3.1.1 on 2020-12-09 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20201127_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, default='write your bio', max_length=200, null=True),
        ),
    ]
