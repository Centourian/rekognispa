# Generated by Django 3.2.5 on 2021-08-03 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('face_detection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beard', models.CharField(blank=True, max_length=8, null=True)),
                ('smile', models.CharField(blank=True, max_length=8, null=True)),
                ('eyeglasses', models.CharField(blank=True, max_length=8, null=True)),
                ('sunglasses', models.CharField(blank=True, max_length=8, null=True)),
                ('mustache', models.CharField(blank=True, max_length=8, null=True)),
                ('eyes_open', models.CharField(blank=True, max_length=8, null=True)),
                ('mouth_open', models.CharField(blank=True, max_length=8, null=True)),
                ('face_fr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='face_detection.facedetection')),
            ],
        ),
        migrations.CreateModel(
            name='BoundingBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
                ('left', models.IntegerField()),
                ('top', models.IntegerField()),
                ('fr_feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='face_detection.features')),
            ],
        ),
    ]