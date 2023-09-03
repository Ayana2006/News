# Generated by Django 4.2.4 on 2023-09-03 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DbObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_id', models.IntegerField(blank=True, null=True)),
                ('class_id', models.IntegerField(blank=True, null=True)),
                ('class_name', models.TextField()),
                ('create_date', models.TextField()),
                ('last_update', models.TextField()),
                ('create_user_id', models.IntegerField(blank=True, null=True)),
                ('update_user_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('dbobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='person.dbobject')),
                ('first_name', models.CharField(max_length=555)),
                ('last_name', models.CharField(max_length=555)),
                ('patronymic', models.CharField(max_length=555)),
                ('date_of_birth', models.CharField(max_length=777)),
                ('gender', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=155)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=666)),
            ],
            bases=('person.dbobject',),
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='person.person')),
            ],
            options={
                'verbose_name': 'Родитель',
                'verbose_name_plural': 'Родители',
            },
            bases=('person.person',),
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='person.person')),
                ('direction', models.CharField(max_length=555)),
            ],
            options={
                'verbose_name': 'Учитель',
                'verbose_name_plural': 'Учителя',
            },
            bases=('person.person',),
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='person.person')),
                ('courses', models.CharField(max_length=555)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='person.parents')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
            bases=('person.person',),
        ),
    ]
