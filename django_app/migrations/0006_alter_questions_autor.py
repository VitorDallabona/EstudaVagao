# Generated by Django 4.1.7 on 2024-01-01 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("django_app", "0005_users_groups_users_is_active_users_is_staff_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="questions",
            name="autor",
            field=models.TextField(max_length=200),
        ),
    ]