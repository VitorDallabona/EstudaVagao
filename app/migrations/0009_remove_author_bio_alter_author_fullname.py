# Generated by Django 4.2.7 on 2024-01-16 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='bio',
        ),
        migrations.AlterField(
            model_name='author',
            name='fullname',
            field=models.IntegerField(default=0, verbose_name='Número do CMSM'),
        ),
    ]
