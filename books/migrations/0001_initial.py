# Generated by Django 5.0.2 on 2024-02-29 12:22

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=60)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]