# Generated by Django 2.2.1 on 2019-05-03 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='queremos que guardes el titulo de la pregunta', max_length=200)),
                ('fecha', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'pregunta',
                'verbose_name_plural': 'preguntas',
                'ordering': ['-fecha'],
            },
        ),
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='Queremos que guardes el título de la opcion', max_length=200)),
                ('votos', models.IntegerField(help_text='Votos de la opcion')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Pregunta')),
            ],
            options={
                'verbose_name': 'opcion',
                'verbose_name_plural': 'opciones',
                'ordering': ['votos'],
            },
        ),
    ]
