# Generated by Django 4.1.7 on 2023-04-29 16:46

import address.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_auto_20200830_1851'),
        ('main', '0002_clients_last_login_clients_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='salons',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='salons',
            name='password',
            field=models.CharField(default='admin', max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='salons',
            name='address',
            field=address.models.AddressField(on_delete=django.db.models.deletion.CASCADE, to='address.address'),
        ),
    ]