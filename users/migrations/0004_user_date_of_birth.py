# Generated by Django 4.2.2 on 2023-07-05 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.CharField(default=-2000, max_length=10),
            preserve_default=False,
        ),
    ]