# Generated by Django 2.2.1 on 2019-08-23 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UnityInfo',
            fields=[
                ('unityID', models.AutoField(primary_key=True, serialize=False, verbose_name='联盟编号')),
                ('unityName', models.CharField(max_length=20, verbose_name='联盟名称')),
            ],
        ),
    ]
