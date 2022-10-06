# Generated by Django 4.1.1 on 2022-10-06 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_merge_20221005_1259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brewingmethod',
            old_name='method_cafe',
            new_name='cafe',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_cafe',
            new_name='cafe',
        ),
        migrations.AddField(
            model_name='cafe',
            name='coffee_beans',
            field=models.ManyToManyField(blank=True, to='main_app.coffeebean'),
        ),
    ]