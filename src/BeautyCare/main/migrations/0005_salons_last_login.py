# Generated by Django 4.1.7 on 2023-04-29 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_salons_last_login_salons_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='salons',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
