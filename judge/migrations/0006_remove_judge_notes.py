# Generated by Django 5.0.6 on 2024-11-25 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0005_judge_criteria4'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='judge',
            name='notes',
        ),
    ]