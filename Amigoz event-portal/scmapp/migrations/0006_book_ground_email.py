# Generated by Django 3.2.3 on 2021-05-24 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scmapp', '0005_auto_20210522_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_ground',
            name='email',
            field=models.CharField(default=2, max_length=40),
            preserve_default=False,
        ),
    ]
