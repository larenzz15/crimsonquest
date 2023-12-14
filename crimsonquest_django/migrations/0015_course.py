# Generated by Django 4.0 on 2023-12-08 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crimsonquest_django', '0014_elementary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('courseID', models.AutoField(primary_key=True, serialize=False)),
                ('courseName', models.CharField(max_length=255)),
                ('courseInfo', models.TextField()),
                ('coursePic', models.ImageField(blank=True, null=True, upload_to='highschool_images/')),
                ('collegeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crimsonquest_django.college')),
            ],
        ),
    ]
