# Generated by Django 3.1 on 2020-12-28 13:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('environments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Environments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('stage', models.CharField(choices=[('DEVELOPMENT', 'DEVELOPMENT'), ('SIT', 'SIT'), ('UAT', 'UAT'), ('STAGING/PRE-PROD', 'STAGING/PRE-PROD'), ('PRODUCTION', 'PRODUCTION')], max_length=100)),
                ('platform', models.CharField(choices=[('MacOs', 'MacOs'), ('LINUX', 'LINUX'), ('WINDOWS', 'WINDOWS')], max_length=100)),
                ('database', models.CharField(choices=[('POSTGRESQL', 'POSTGRESQL'), ('MariaDB', 'MariaDB'), ('MySQL', 'MySQL'), ('Oracle', 'Oracle'), ('MS SQL Server', 'MS SQL Server'), ('SQLite3', 'SQLite3'), ('CosmosDB', 'CosmosDB'), ('MongoDB', 'MongoDB')], max_length=50)),
                ('run_stack', models.CharField(max_length=100)),
                ('web_server', models.CharField(max_length=150)),
                ('ip', models.FloatField()),
                ('hardware', models.CharField(choices=[('PHISICAL_SERVER', 'PHISICAL_SERVER'), ('VIRTUAL MACHINE', 'VIRTUAL MACHINE')], max_length=50)),
                ('product_app', models.CharField(max_length=200)),
                ('port', models.IntegerField()),
                ('provider', models.CharField(choices=[('INTERNAL', 'INTERNAL'), ('OUTSOURCED', 'OUTSOURCED')], max_length=50)),
                ('created_by', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('LIVE', 'LIVE'), ('DOWN', 'DOWN')], max_length=30)),
            ],
            options={
                'ordering': ['date_created', 'name', 'stage', 'platform'],
            },
        ),
        migrations.DeleteModel(
            name='Envorionments',
        ),
    ]
