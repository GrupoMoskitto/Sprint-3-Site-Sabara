# Generated by Django 5.2 on 2025-04-25 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "pacientes",
            "0003_remove_paciente_endereco_paciente_endereco_bairro_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="paciente",
            options={"verbose_name": "Paciente", "verbose_name_plural": "Pacientes"},
        ),
        migrations.AddField(
            model_name="paciente",
            name="plano_saude",
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
