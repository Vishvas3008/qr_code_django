# Generated by Django 4.0.4 on 2024-10-12 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_total_member_member_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='total',
            name='cloudinary_api_key',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='total',
            name='cloudinary_api_secret',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='total',
            name='cloudinary_cloud_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]