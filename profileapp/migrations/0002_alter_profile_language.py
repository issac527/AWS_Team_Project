# Generated by Django 3.2.8 on 2021-10-11 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='language',
            field=models.CharField(choices=[('English', 'English'), ('Japanese', 'Japanese'), ('Simplified Chinese', 'Simplified Chinese'), ('Traditional Chinese', 'Traditional Chinese'), ('Vietnamese', 'Vietnamese'), ('Indonesian', 'Indonesian'), ('Thai', 'Thai'), ('German', 'German'), ('Russian', 'Russian'), ('Spanish', 'Spanish'), ('Italian', 'Italian'), ('French', 'French')], max_length=20),
        ),
    ]
