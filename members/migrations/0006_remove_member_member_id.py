# Generated by Django 4.0.4 on 2024-10-12 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_alter_member_qr_code_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='member_id',
        ),
    ]
