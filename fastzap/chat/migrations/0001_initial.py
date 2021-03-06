# Generated by Django 3.2.6 on 2021-08-27 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(max_length=100, verbose_name='Organização')),
                ('status', models.CharField(max_length=100, verbose_name='Status')),
            ],
            options={
                'ordering': ['client'],
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('phone', models.CharField(max_length=100, verbose_name='Telefone')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100, verbose_name='Texto')),
                ('file', models.FileField(upload_to='uploads/')),
                ('type', models.CharField(max_length=100, verbose_name='Tipo')),
                ('status', models.CharField(max_length=100, verbose_name='Status')),
                ('attendance', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='chat.attendance')),
            ],
            options={
                'ordering': ['attendance'],
            },
        ),
        migrations.AddField(
            model_name='attendance',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='chat.client'),
        ),
    ]
