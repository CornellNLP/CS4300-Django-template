# Generated by Django 2.1.7 on 2019-04-15 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_recreational', models.BooleanField()),
                ('conditions', models.CharField(max_length=250)),
                ('undesired_effects', models.CharField(max_length=250)),
                ('tolerance', models.CharField(choices=[('N', 'No Tolerance'), ('L', 'Low Tolerance'), ('M', 'Mild Tolerance'), ('H', 'High Tolerance')], max_length=1)),
                ('age', models.IntegerField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
            ],
        ),
    ]
