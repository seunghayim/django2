# Generated by Django 4.0 on 2022-04-17 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coplate', '0005_review_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')], default=None),
        ),
    ]
