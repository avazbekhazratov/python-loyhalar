# Generated by Django 4.1.7 on 2023-05-03 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('is_menu', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=15)),
                ('sms', models.CharField(max_length=256)),
                ('is_trash', models.BooleanField(default=False)),
                ('is_view', models.BooleanField(default=False)),
                ('contacted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('short_desc', models.TextField()),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('view', models.IntegerField(default=0)),
                ('ctg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sayt.category')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=129)),
                ('text', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sayt.news')),
                ('reply_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sayt.comment')),
            ],
        ),
    ]
