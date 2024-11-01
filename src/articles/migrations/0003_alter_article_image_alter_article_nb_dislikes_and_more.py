# Generated by Django 5.1.2 on 2024-11-01 03:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('articles', '0002_article_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='articles/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='nb_dislikes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='nb_likes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='published',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='published_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
