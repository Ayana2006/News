# Generated by Django 4.2.4 on 2023-08-25 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=55)),
                ('email', models.EmailField(max_length=254)),
                ('instagram', models.URLField()),
                ('twitter', models.URLField()),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.AlterField(
            model_name='media',
            name='image',
            field=models.ImageField(upload_to='media_news/'),
        ),
        migrations.CreateModel(
            name='Professions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('description', models.TextField()),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profession', to='posts.media')),
            ],
            options={
                'verbose_name': 'Профессия',
                'verbose_name_plural': 'Профессии',
            },
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created', models.DateField(auto_now_add=True)),
                ('text', models.TextField()),
                ('media_awards', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media_awards', to='posts.media')),
            ],
            options={
                'verbose_name': 'Награда',
                'verbose_name_plural': 'Награды',
            },
        ),
    ]
