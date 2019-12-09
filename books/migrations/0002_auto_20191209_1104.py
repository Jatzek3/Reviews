# Generated by Django 2.2.7 on 2019-12-09 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booksreview',
            old_name='books_review',
            new_name='description',
        ),
        migrations.AddField(
            model_name='booksreview',
            name='author',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='booksreview',
            name='difficulty',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='booksreview',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='booksreview',
            name='quality',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='booksreview',
            name='skill_level',
            field=models.CharField(max_length=10, null=True),
        ),
    ]