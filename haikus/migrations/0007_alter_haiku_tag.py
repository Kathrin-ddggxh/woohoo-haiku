# Generated by Django 3.2.16 on 2022-11-09 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haikus', '0006_alter_haiku_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='haiku',
            name='tag',
            field=models.CharField(default='Tag your haiku', max_length=80),
        ),
    ]
