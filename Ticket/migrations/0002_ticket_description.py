# Generated by Django 4.0.1 on 2022-08-07 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]