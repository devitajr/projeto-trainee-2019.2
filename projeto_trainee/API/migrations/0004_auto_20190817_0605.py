# Generated by Django 2.1 on 2019-08-17 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_auto_20190817_0541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conta',
            name='number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='API.Number'),
        ),
    ]
