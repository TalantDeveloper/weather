# Generated by Django 5.0.6 on 2024-06-30 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('text', models.CharField(max_length=255, verbose_name='text')),
            ],
        ),
    ]
