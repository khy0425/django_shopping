# Generated by Django 3.2.3 on 2021-06-03 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khyuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='khyuser',
            name='level',
            field=models.CharField(choices=[('admin', 'admin'), ('user', 'user')], default='user', max_length=8, verbose_name='등급'),
            preserve_default=False,
        ),
    ]
