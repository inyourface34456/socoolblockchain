# Generated by Django 3.1.5 on 2021-05-26 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eggcoin', '0003_block_chain_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block_chain',
            name='previous_hash',
            field=models.CharField(max_length=200),
        ),
    ]
