# Generated by Django 4.0.4 on 2024-10-12 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_total_cloudinary_api_key_total_cloudinary_api_secret_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='qr_code_url',
            field=models.CharField(default='hey', max_length=255),
            preserve_default=False,
        ),
    ]