# Generated by Django 4.0 on 2023-12-04 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimsonquest_django', '0006_cq_campus_delete_campus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('campusID', models.AutoField(primary_key=True, serialize=False)),
                ('campusName', models.CharField(max_length=255)),
                ('campusInfo', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='cq_Campus',
        ),
    ]
