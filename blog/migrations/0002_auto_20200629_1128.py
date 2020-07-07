# Generated by Django 3.0.7 on 2020-06-29 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.CharField(blank=True, max_length=150)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField()),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
