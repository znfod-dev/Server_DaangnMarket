# Generated by Django 3.0.4 on 2020-04-27 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_post_address'),
        ('chat', '0002_message_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='post',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='post.Post'),
            preserve_default=False,
        ),
    ]
