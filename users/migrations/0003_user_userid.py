# Generated by Django 2.2.16 on 2020-09-16 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200916_1422'),
        ('users', '0002_auto_20200916_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='userID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_userID', to='home.CustomText'),
        ),
    ]