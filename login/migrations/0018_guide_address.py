# Generated by Django 4.2.5 on 2023-09-14 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0017_remove_guide_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='address',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]