# Generated by Django 5.0.6 on 2024-07-24 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pontos', '0006_ponto_audio_alter_createhinario_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='ponto',
            name='urlYoutube',
            field=models.URLField(blank=True),
        ),
    ]
