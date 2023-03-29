# Generated by Django 3.2.16 on 2023-03-29 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20230328_2031'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_follower',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='unique_follower'),
        ),
    ]
