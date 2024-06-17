# Generated by Django 5.0.6 on 2024-05-31 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('author', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='movie/images')),
                ('reviws', models.CharField(max_length=200, null=True)),
                ('trailers', models.TextField(null=True)),
            ],
        ),
    ]