# Generated by Django 2.2.12 on 2020-04-14 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=60)),
                ('language', models.CharField(max_length=60)),
                ('abbreviation', models.BooleanField(default=False)),
                ('ccode', models.CharField(max_length=4)),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Major')),
            ],
        ),
    ]