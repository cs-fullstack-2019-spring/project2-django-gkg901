# Generated by Django 2.0.6 on 2019-03-14 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wikiapp', '0004_auto_20190313_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='relatedmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='wiki'),
        ),
        migrations.AlterField(
            model_name='relatedmodel',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wikiapp.PostModel'),
        ),
    ]