# Generated by Django 4.1.7 on 2023-04-16 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="clients",
            name="last_login",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="last login"
            ),
        ),
        migrations.AddField(
            model_name="clients",
            name="password",
            field=models.CharField(
                default="default", max_length=128, verbose_name="password"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="clients",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]