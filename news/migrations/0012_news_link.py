# Generated by Django 4.0.4 on 2022-05-08 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_alter_comment_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
