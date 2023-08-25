# Generated by Django 4.2.4 on 2023-08-25 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('image', models.ImageField(upload_to='media/')),
            ],
            options={
                'verbose_name': 'Медиа',
                'verbose_name_plural': 'Медии',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('description', models.TextField()),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='posts.media')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='AdditionalCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('description', models.TextField()),
                ('media_cours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media_cours', to='posts.media')),
            ],
            options={
                'verbose_name': 'Дополнительный кружок',
                'verbose_name_plural': 'Дополнительные кружки',
            },
        ),
    ]
