# Generated by Django 4.2.4 on 2023-08-25 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_contact_alter_media_image_professions_awards'),
        ('users', '0002_media_students_stakeholder_parents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parents',
            name='parents',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media_parents', to='posts.media'),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='stakeholder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stakeholder', to='posts.media'),
        ),
        migrations.DeleteModel(
            name='Media',
        ),
    ]