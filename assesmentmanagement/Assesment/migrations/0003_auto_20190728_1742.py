# Generated by Django 2.2.2 on 2019-07-28 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Assesment', '0002_auto_20190728_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assesment',
            name='course_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Assesment.Course'),
        ),
    ]