# Generated by Django 2.2.1 on 2019-06-07 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image_link', models.CharField(blank=True, max_length=100)),
                ('image', models.FileField(blank=True, null=True, upload_to='issues/{title}')),
                ('issue_link', models.CharField(blank=True, max_length=100)),
                ('issue', models.FileField(blank=True, null=True, upload_to='issues/{title}')),
                ('youtube', models.CharField(blank=True, max_length=100)),
                ('soundcloud', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
