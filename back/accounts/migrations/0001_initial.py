# Generated by Django 4.2.13 on 2024-06-18 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebUser',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('username', models.TextField()),
                ('publicKey', models.TextField()),
            ],
        ),
    ]
