# Generated by Django 4.0 on 2023-12-04 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimsonquest_django', '0009_college'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='collegeMap',
            field=models.ImageField(blank=True, null=True, upload_to='college_images/'),
        ),
        migrations.AlterField(
            model_name='college',
            name='collegePic1',
            field=models.ImageField(blank=True, null=True, upload_to='college_images/'),
        ),
        migrations.AlterField(
            model_name='college',
            name='collegePic2',
            field=models.ImageField(blank=True, null=True, upload_to='college_images/'),
        ),
        migrations.AlterField(
            model_name='college',
            name='collegePic3',
            field=models.ImageField(blank=True, null=True, upload_to='college_images/'),
        ),
    ]
