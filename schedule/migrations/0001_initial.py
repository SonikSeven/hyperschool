# Generated by Django 2.2 on 2023-03-13 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('info', models.CharField(max_length=1020)),
                ('duration_months', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('about', models.CharField(max_length=1020)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('course', models.ManyToManyField(to='schedule.Course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ManyToManyField(to='schedule.Teacher'),
        ),
    ]
