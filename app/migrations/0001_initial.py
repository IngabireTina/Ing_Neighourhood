# Generated by Django 3.2 on 2021-05-04 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('image', models.ImageField(default='a.jpg', upload_to='hood')),
                ('police', models.IntegerField(blank=True, null=True)),
                ('health', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]
