# Generated by Django 2.2 on 2019-04-10 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bira', '0003_assign_issue_issue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='assignee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bira.User'),
        ),
    ]