# Generated by Django 2.2 on 2018-12-23 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posttitle', models.TextField()),
                ('postbody', models.TextField()),
                ('posttag1', models.CharField(max_length=100)),
                ('posttag2', models.CharField(max_length=100)),
                ('posttag3', models.CharField(max_length=100)),
                ('posttag4', models.CharField(max_length=100)),
                ('dt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentauthor', models.CharField(max_length=45)),
                ('commentcontent', models.TextField()),
                ('commentdate', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Post')),
            ],
        ),
    ]
