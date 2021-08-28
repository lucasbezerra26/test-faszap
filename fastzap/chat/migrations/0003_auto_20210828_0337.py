# Generated by Django 3.2.6 on 2021-08-28 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20210827_0420'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendance',
            options={'ordering': ['organization']},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['attendance']},
        ),
        migrations.AlterField(
            model_name='message',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]