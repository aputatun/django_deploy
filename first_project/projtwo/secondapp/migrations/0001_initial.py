# Generated by Django 3.0.3 on 2020-05-10 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userfirst', models.CharField(max_length=264)),
                ('userlast', models.CharField(max_length=265)),
                ('userEmail', models.URLField()),
            ],
        ),
    ]
