# Generated by Django 2.2.1 on 2019-05-21 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('companyID', models.AutoField(primary_key=True, serialize=False, verbose_name='单位编号')),
                ('companyName', models.CharField(max_length=20, verbose_name='单位名称')),
                ('companyRegisterNumber', models.CharField(max_length=18, verbose_name='企业注册号')),
                ('telephone', models.CharField(default='', max_length=11, verbose_name='企业热线')),
                ('legalPersonName', models.CharField(max_length=10, verbose_name='企业法人')),
                ('legalPersonPhone', models.CharField(max_length=11, verbose_name='法人联系方式')),
                ('amountOfProStoreHouse', models.IntegerField(verbose_name='产品仓库数量')),
                ('amountOfItemStoreHouse', models.IntegerField(verbose_name='投入品仓库数量')),
                ('joiningDate', models.DateField(verbose_name='加入时间')),
                ('updateTime', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('superCompany', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.CompanyInfo', verbose_name='上级公司')),
            ],
            options={
                'verbose_name': '单位信息',
                'verbose_name_plural': '单位信息',
            },
        ),
        migrations.CreateModel(
            name='MemberInfo',
            fields=[
                ('memberID', models.AutoField(primary_key=True, serialize=False, verbose_name='工号')),
                ('memberName', models.CharField(max_length=10, verbose_name='员工姓名')),
                ('position', models.CharField(max_length=10, verbose_name='员工职位')),
                ('telephone', models.CharField(max_length=11, verbose_name='联系方式')),
                ('hireDate', models.DateField(verbose_name='聘用时间')),
                ('updateDate', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('companyName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.CompanyInfo', verbose_name='隶属单位')),
            ],
            options={
                'verbose_name': '员工信息',
                'verbose_name_plural': '员工信息',
            },
        ),
        migrations.CreateModel(
            name='FinanceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=15, verbose_name='收支明细')),
                ('type', models.CharField(choices=[(0, '支出'), (1, '收入')], max_length=3, verbose_name='类型')),
                ('amount', models.IntegerField(verbose_name='金额')),
                ('unit', models.CharField(choices=[('yuan', '元'), ('thousand', '千元'), ('million', '百万元')], max_length=20, verbose_name='单位')),
                ('payer', models.CharField(max_length=20, verbose_name='付款方')),
                ('payee', models.CharField(max_length=20, verbose_name='收款方')),
                ('dealDate', models.DateField(verbose_name='交易日期')),
                ('createTime', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('updateTime', models.DateField(auto_now_add=True, verbose_name='修改时间')),
                ('hash', models.CharField(max_length=128, null=True, verbose_name='hash值')),
                ('companyID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.CompanyInfo', verbose_name='所属单位编号')),
                ('memberID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.MemberInfo', verbose_name='经办人工号')),
            ],
            options={
                'verbose_name': '收支记录',
                'verbose_name_plural': '收支记录',
            },
        ),
        migrations.CreateModel(
            name='EquipmentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipmentName', models.CharField(max_length=20, verbose_name='设备名称')),
                ('amount', models.IntegerField(verbose_name='数量')),
                ('description', models.CharField(default='', max_length=999, verbose_name='备注')),
                ('share', models.BooleanField(default=False, verbose_name='共享与否')),
                ('shareCondition', models.CharField(default='', max_length=999, verbose_name='共享条件')),
                ('companyID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.CompanyInfo', verbose_name='所属公司编号')),
            ],
            options={
                'verbose_name': '设备信息',
                'verbose_name_plural': '设备信息',
            },
        ),
        migrations.CreateModel(
            name='BlockInfo',
            fields=[
                ('blockID', models.AutoField(primary_key=True, serialize=False, verbose_name='地块编号')),
                ('blockName', models.CharField(default='', max_length=20, verbose_name='地块别名')),
                ('blockSquare', models.IntegerField(verbose_name='地块面积')),
                ('unit', models.CharField(choices=[('1', '亩'), ('2', '平方米')], max_length=10)),
                ('soilInfo', models.CharField(max_length=200, verbose_name='土壤信息')),
                ('companyID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.CompanyInfo', verbose_name='所属公司编号')),
            ],
            options={
                'verbose_name': '地块信息',
                'verbose_name_plural': '地块信息',
            },
        ),
    ]
