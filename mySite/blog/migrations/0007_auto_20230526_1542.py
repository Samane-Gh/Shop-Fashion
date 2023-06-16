# Generated by Django 3.2.19 on 2023-05-26 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created_date',)},
        ),
        migrations.AddField(
            model_name='post',
            name='login_required',
            field=models.BooleanField(default=False),
        ),
    ]
