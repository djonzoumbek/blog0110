# Generated by Django 5.1.2 on 2024-11-01 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]