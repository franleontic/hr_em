# Generated by Django 4.2.1 on 2023-06-14 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_text_user_delete_belongs'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='confidence',
            field=models.FloatField(default=1.0),
            preserve_default=False,
        ),
    ]
