# Generated by Django 3.2.9 on 2021-12-01 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_rename_active_taskmodel_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='todo.listmodel'),
        ),
    ]
