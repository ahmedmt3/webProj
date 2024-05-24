# Generated by Django 5.0.6 on 2024-05-23 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='uploadedPhotos/%y/%m/%d')),
                ('borrowed', models.BooleanField(default=False)),
            ],
        ),
    ]