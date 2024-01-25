# Generated by Django 4.2 on 2023-09-20 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0007_rename_country_stations_ctslot_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='0', max_length=120)),
                ('rating', models.CharField(choices=[('1', 'Poor'), ('2', 'Fair '), ('3', 'Good '), ('4', 'Very Good'), ('5', 'Excellent')], default='0', max_length=20)),
                ('comment', models.CharField(default='0', max_length=120)),
            ],
        ),
    ]