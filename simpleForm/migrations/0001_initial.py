# Generated by Django 2.1.7 on 2020-11-28 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=15)),
                ('mobile', models.CharField(max_length=10)),
                ('place', models.CharField(max_length=50)),
            ],
        ),
    ]
