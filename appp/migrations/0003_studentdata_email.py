# Generated by Django 4.2.7 on 2023-11-29 08:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appp', '0002_studentdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdata',
            name='Email',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]