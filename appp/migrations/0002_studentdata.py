# Generated by Django 4.2.5 on 2023-11-23 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studentdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(max_length=255)),
                ('Name', models.CharField(max_length=255)),
                ('Father_name', models.CharField(max_length=255)),
                ('College', models.CharField(max_length=255)),
                ('Phone', models.CharField(max_length=255)),
                ('Alternate_phone', models.CharField(max_length=255)),
                ('Paid_Amount', models.CharField(max_length=255)),
                ('Mode_of_payment', models.CharField(max_length=255)),
                ('Balance_amount', models.CharField(max_length=255)),
                ('Type_of_course', models.CharField(max_length=255)),
                ('Cources_name', models.CharField(max_length=255)),
                ('additional_course', models.CharField(max_length=255)),
            ],
        ),
    ]
