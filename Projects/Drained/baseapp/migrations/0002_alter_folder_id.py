# Generated by Django 4.2.10 on 2024-04-27 17:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
