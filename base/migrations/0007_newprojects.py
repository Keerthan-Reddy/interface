# Generated by Django 4.2.10 on 2024-02-16 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_imagewithlink_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('projecturl', models.URLField(max_length=1000)),
            ],
        ),
    ]