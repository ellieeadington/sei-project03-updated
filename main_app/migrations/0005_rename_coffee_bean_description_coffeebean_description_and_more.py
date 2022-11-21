# Generated by Django 4.1.1 on 2022-10-04 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_cafe_coffee_beans'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coffeebean',
            old_name='coffee_bean_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='coffeebean',
            old_name='coffee_bean_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='coffeebean',
            old_name='coffee_bean_location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='coffeebean',
            old_name='coffee_bean_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='coffeebean',
            old_name='roastery_name',
            new_name='roastery',
        ),
        migrations.RenameField(
            model_name='coffeebean',
            old_name='coffee_bean_variety',
            new_name='variety',
        ),
    ]