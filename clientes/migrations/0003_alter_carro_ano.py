# Generated by Django 4.2.8 on 2023-12-07 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clientes", "0002_alter_carro_ano"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carro",
            name="ano",
            field=models.BigIntegerField(),
        ),
    ]
