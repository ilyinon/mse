# Generated by Django 2.0 on 2017-12-18 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(verbose_name='date published')),
                ('updated', models.DateTimeField(verbose_name='date published')),
                ('status', models.CharField(max_length=20)),
                ('version', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Servers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_fqdn', models.CharField(max_length=200)),
                ('created', models.DateTimeField(verbose_name='date published')),
                ('updated', models.DateTimeField(verbose_name='date published')),
                ('status', models.CharField(max_length=20)),
                ('info', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='clients',
            name='hosted_on',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deploy.Servers'),
        ),
    ]
