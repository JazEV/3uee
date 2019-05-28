# Generated by Django 2.2.1 on 2019-05-08 19:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pregunta',
            options={'ordering': ['-creacion'], 'verbose_name': 'pregunta', 'verbose_name_plural': 'preguntas'},
        ),
        migrations.RenameField(
            model_name='pregunta',
            old_name='fecha',
            new_name='modificacion',
        ),
        migrations.AddField(
            model_name='pregunta',
            name='creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]