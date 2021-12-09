# Generated by Django 2.2.24 on 2021-12-09 23:44

import django.core.files.storage
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scan_name', models.CharField(max_length=200, unique=True, verbose_name='Scan Name')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('start_date', models.DateTimeField(null=True, verbose_name='Date Started')),
                ('end_date', models.DateTimeField(null=True, verbose_name='Date Ended')),
                ('notes', models.TextField(blank=True, verbose_name='Notes (optional)')),
                ('result', models.FileField(storage=django.core.files.storage.FileSystemStorage(), upload_to='', verbose_name='Scan Result')),
                ('auto_create', models.BooleanField(default=False, verbose_name='Automatically create scan')),
                ('auto_start', models.BooleanField(default=False, verbose_name='Automatically start scan')),
                ('auto_retrieve', models.BooleanField(default=False, verbose_name='Automatically retrieve scan')),
                ('status', models.CharField(choices=[('NW', 'New'), ('CR', 'Creating'), ('CD', 'Created'), ('ST', 'Starting'), ('IP', 'In progress'), ('PD', 'Paused'), ('ST', 'Stopped'), ('FI', 'Finished'), ('RG', 'Retrieving'), ('RD', 'Retrieved'), ('ER', 'Error occurred')], default='NW', max_length=2)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_dd_downloader.scan_set+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Scanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scanner_name', models.CharField(max_length=200, unique=True, verbose_name='Scanner Name')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('notes', models.TextField(blank=True, verbose_name='Notes (optional)')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_dd_downloader.scanner_set+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Burp_Suite_Scan',
            fields=[
                ('scan_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dd_downloader.Scan')),
                ('endpoints', models.TextField()),
                ('scan_id', models.IntegerField(default=None, null=True, validators=[django.core.validators.MinValueValidator(1)])),
            ],
            bases=('dd_downloader.scan',),
        ),
        migrations.CreateModel(
            name='Burp_Suite_Scanner',
            fields=[
                ('scanner_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dd_downloader.Scanner')),
                ('api_url', models.CharField(max_length=200, verbose_name='API URL')),
                ('api_key', models.CharField(max_length=200, verbose_name='API Key')),
            ],
            bases=('dd_downloader.scanner',),
        ),
        migrations.CreateModel(
            name='Nessus_Scan',
            fields=[
                ('scan_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dd_downloader.Scan')),
                ('endpoints', models.TextField()),
                ('override_policy_id', models.IntegerField(blank=True, default=None, null=True)),
                ('scan_id', models.IntegerField(default=None, null=True, validators=[django.core.validators.MinValueValidator(1)])),
            ],
            bases=('dd_downloader.scan',),
        ),
        migrations.CreateModel(
            name='Nessus_Scanner',
            fields=[
                ('scanner_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dd_downloader.Scanner')),
                ('api_url', models.CharField(max_length=200, verbose_name='API URL')),
                ('access_key', models.CharField(max_length=200, verbose_name='API Access Key')),
                ('secret_key', models.CharField(max_length=200, verbose_name='API Secret Key')),
                ('default_policy_id', models.IntegerField(blank=True, default=None, null=True, verbose_name='Default policy ID for scans (optional)')),
            ],
            bases=('dd_downloader.scanner',),
        ),
        migrations.AddField(
            model_name='scan',
            name='scanner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dd_downloader.Scanner'),
        ),
    ]
