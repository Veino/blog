# Generated by Django 4.2.3 on 2023-07-25 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('body', models.TextField()),
                ('headline', models.TextField()),
                ('image', models.ImageField(default='default.jpg', upload_to='Posts-Images')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
