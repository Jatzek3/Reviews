# Generated by Django 2.2.7 on 2020-01-29 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20191209_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='BooksReviewComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
            ],
        ),
    ]
