# Generated by Django 4.2.4 on 2023-08-31 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0003_bookshelf_borrow_remove_hall_shelves_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='return_date',
            field=models.DateField(blank=True),
        ),
    ]
