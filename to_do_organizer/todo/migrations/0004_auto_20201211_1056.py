# Generated by Django 3.1.4 on 2020-12-11 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20201211_0941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='todos',
        ),
        migrations.AddField(
            model_name='todo',
            name='todolist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='todo.todolist'),
            preserve_default=False,
        ),
    ]