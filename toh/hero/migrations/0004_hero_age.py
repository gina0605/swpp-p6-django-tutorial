# Generated by Django 3.2.6 on 2021-10-04 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0003_remove_hero_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]