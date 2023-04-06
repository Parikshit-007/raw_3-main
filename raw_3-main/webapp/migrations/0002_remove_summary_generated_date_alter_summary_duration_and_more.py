# Generated by Django 4.1.3 on 2023-04-04 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='summary',
            name='generated_date',
        ),
        migrations.AlterField(
            model_name='summary',
            name='duration',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='summary',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.userprofile'),
        ),
    ]
