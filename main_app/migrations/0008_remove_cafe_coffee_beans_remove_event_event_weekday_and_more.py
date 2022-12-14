# Generated by Django 4.1.1 on 2022-10-04 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_merge_20221004_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cafe',
            name='coffee_beans',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_weekday',
        ),
        migrations.AddField(
            model_name='event',
            name='event_date',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('KID', 'Children'), ('MUM', 'Parent and Children'), ('HEA', 'Health and Wellbeing'), ('FIT', 'Fitness'), ('FOO', 'Cooking and Food'), ('ENT', 'Entertainment'), ('ART', 'Arts and Crafts')], default='KID', max_length=4),
        ),
        migrations.AlterField(
            model_name='brewingmethod',
            name='method_name',
            field=models.CharField(choices=[('DB', 'Drip Brewed'), ('P', 'Percolator'), ('FP', 'French Press'), ('C', 'Chezve'), ('P', 'Pour-over'), ('S', 'Syphon'), ('CM', 'Coffee Maker'), ('V', 'V60'), ('AP', 'Aeropress')], default='DB', max_length=2),
        ),
    ]