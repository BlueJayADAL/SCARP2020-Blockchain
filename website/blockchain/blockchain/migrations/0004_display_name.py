# Generated by Django 3.0.7 on 2020-08-04 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0003_auto_20200803_2354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Display_Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('display_file', models.FileField(upload_to='')),
            ],
        ),
    ]
