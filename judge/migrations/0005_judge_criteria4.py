# Generated by Django 5.0.6 on 2024-11-13 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0004_judge_event_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='judge',
            name='criteria4',
            field=models.DecimalField(decimal_places=2, default=23, max_digits=5),
            preserve_default=False,
        ),
    ]
