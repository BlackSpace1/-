# Generated by Django 2.2.1 on 2019-09-28 09:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unity', '0002_auto_20190928_1700'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taskManagement', '0002_auto_20190521_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='companytaskinfo',
            name='recorder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='发布人'),
        ),
        migrations.AddField(
            model_name='companytaskinfo',
            name='unityID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='unity.UnityInfo', verbose_name='所属联盟'),
        ),
    ]
