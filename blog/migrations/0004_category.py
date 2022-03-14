# Generated by Django 4.0.3 on 2022-03-14 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
    ]
