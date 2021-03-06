# Generated by Django 3.2.8 on 2022-02-09 00:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('petsgallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listtablemodel',
            old_name='images',
            new_name='images1',
        ),
        migrations.AddField(
            model_name='listtablemodel',
            name='images2',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listtablemodel',
            name='images3',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listtablemodel',
            name='content',
            field=models.TextField(max_length=80),
        ),
    ]
