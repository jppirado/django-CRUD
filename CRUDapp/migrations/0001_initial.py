# Generated by Django 4.0.6 on 2022-07-31 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(max_length=200)),
                ('value_product', models.FloatField()),
                ('invetory_product', models.FloatField()),
            ],
        ),
    ]