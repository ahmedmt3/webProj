# Generated by Django 5.0.6 on 2024-06-27 08:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_remove_user_id_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='borrower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='borrowed_books_set', to='books.user'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('Classic', 'Classic'), ('Fiction', 'Fiction'), ('Fantasy', 'Fantasy'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Biography', 'Biography'), ('Science Fiction', 'Science Fiction'), ('Historical Fiction', 'Historical Fiction')], max_length=50),
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateField(auto_now_add=True)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.user')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='borrowed_books',
            field=models.ManyToManyField(related_name='borrowed_by_users', through='books.Borrow', to='books.book'),
        ),
    ]
