# Generated by Django 4.2.7 on 2024-01-06 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_author_bio_alter_author_fullname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ano_escolar',
            field=models.CharField(choices=[('1', 'Fundamental: 6º ano'), ('2', 'Fundamental: 7º ano'), ('3', 'Fundamental: 8º ano'), ('4', 'Fundamental: 9º ano'), ('5', 'Ensino Médio: 1º ano'), ('6', 'Ensino Médio: 2º ano'), ('7', 'Ensino Médio: 3º ano')], default=0, max_length=400, verbose_name='Ano Escolar'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.CharField(choices=[('1', 'Matemática'), ('2', 'Física'), ('3', 'Química'), ('4', 'Biologia'), ('5', 'História'), ('6', 'Geografia'), ('7', 'Filosofia'), ('8', 'Sociologia'), ('9', 'Português'), ('10', 'Literatura'), ('11', 'Inglês'), ('12', 'Sociologia'), ('13', 'Arte'), ('14', 'Educação Física'), ('15', 'Outra')], max_length=400, verbose_name='Disciplinas'),
        ),
    ]