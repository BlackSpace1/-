# Generated by Django 2.2.1 on 2019-09-28 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unity', '0002_auto_20190928_1700'),
        ('systemInfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sysnews',
            name='unity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='unity.UnityInfo'),
        ),
        migrations.AddField(
            model_name='sysregulations',
            name='unity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='unity.UnityInfo'),
        ),
        migrations.AlterField(
            model_name='sysnews',
            name='description',
            field=models.CharField(max_length=2000, verbose_name='动态内容'),
        ),
        migrations.AlterField(
            model_name='sysregulations',
            name='regDescription',
            field=models.CharField(max_length=2000, verbose_name='制度详情'),
        ),
    ]
