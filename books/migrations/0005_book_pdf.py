# Generated by Django 5.0.2 on 2024-03-31 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pdf',
            field=models.FileField(blank=True, upload_to='pdfs/'),
        ),
    ]