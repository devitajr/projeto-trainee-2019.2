# Generated by Django 2.1 on 2019-08-17 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_auto_20190817_0528'),
    ]

    operations = [
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='API.Number'),
        ),
    ]
