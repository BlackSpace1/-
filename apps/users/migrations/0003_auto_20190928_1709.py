# Generated by Django 2.2.1 on 2019-09-28 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unity', '0002_auto_20190928_1700'),
        ('users', '0002_auto_20190928_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='employeeID',
            field=models.CharField(max_length=20, null=True, verbose_name='员工编号'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='identityID',
            field=models.CharField(max_length=20, null=True, verbose_name='身份证号'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='unityID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='unity.UnityInfo'),
        ),
    ]
