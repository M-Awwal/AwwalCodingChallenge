# Generated by Django 3.1.6 on 2021-02-05 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('switches', '0003_auto_20210205_0451'),
    ]

    operations = [
        migrations.CreateModel(
            name='Switch1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ping_status', models.SmallIntegerField(default=0)),
                ('unix_timestamp', models.CharField(default='1612539326', max_length=500)),
                ('alert_date_time', models.CharField(default='05/02/2021 15:35:26', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Switch2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ping_status', models.SmallIntegerField(default=0)),
                ('unix_timestamp', models.CharField(default='1612539326', max_length=500)),
                ('alert_date_time', models.CharField(default='05/02/2021 15:35:26', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Switch3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ping_status', models.SmallIntegerField(default=0)),
                ('unix_timestamp', models.CharField(default='1612539326', max_length=500)),
                ('alert_date_time', models.CharField(default='05/02/2021 15:35:26', max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='ping',
            name='unix_timestamp',
            field=models.CharField(default='1612539326', max_length=500),
        ),
        migrations.AlterField(
            model_name='report',
            name='alert_date_time',
            field=models.CharField(default='05/02/2021 15:35:26', max_length=500),
        ),
        migrations.AlterField(
            model_name='report',
            name='email_date_time',
            field=models.CharField(default='05/02/2021 15:35:26', max_length=500),
        ),
    ]
