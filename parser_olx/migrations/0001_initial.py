# Generated by Django 4.0.6 on 2022-07-27 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_to_category_page', models.CharField(max_length=255, verbose_name='Посилання на сторінку')),
                ('date_of_last_update', models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')),
                ('data_string', models.TextField(verbose_name='Конвертовані дані')),
            ],
            options={
                'verbose_name': 'Категорія',
                'verbose_name_plural': 'Категорії',
            },
        ),
    ]
