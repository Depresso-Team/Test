# Generated by Django 4.2.4 on 2023-09-14 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0014_remove_customuser_guided_tours_remove_guide_tours'),
        ('tours', '0013_remove_tourslist_guide'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourslist',
            name='guide',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='login.guide'),
        ),
    ]