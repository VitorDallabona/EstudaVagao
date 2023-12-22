# Generated by Django 4.1.7 on 2023-12-05 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("django_app", "0003_disciplinas_alter_users_nome_respostas"),
    ]

    operations = [
        migrations.DeleteModel(name="disciplinas",),
        migrations.AddField(
            model_name="questions", name="ano", field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="questions",
            name="disciplina",
            field=models.TextField(default="DEFAULT VALUE", max_length=500),
        ),
        migrations.AddField(
            model_name="questions",
            name="nivel",
            field=models.TextField(default=0, max_length=500),
        ),
        migrations.AlterField(
            model_name="questions",
            name="pergunta",
            field=models.CharField(max_length=500),
        ),
    ]