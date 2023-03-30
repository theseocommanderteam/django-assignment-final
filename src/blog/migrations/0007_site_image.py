# Generated by Django 3.2.7 on 2023-03-28 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20230328_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='site_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='blog/')),
                ('fevicon', models.ImageField(blank=True, null=True, upload_to='blog/')),
            ],
        ),
    ]