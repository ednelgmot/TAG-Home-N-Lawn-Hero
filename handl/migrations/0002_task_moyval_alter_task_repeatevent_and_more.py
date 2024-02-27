# Generated by Django 4.2.9 on 2024-02-27 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handl', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='moyval',
            field=models.CharField(blank=True, choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], help_text='Select Month event repeats in', max_length=9, null=True, verbose_name='Month it repeats'),
        ),
        migrations.AlterField(
            model_name='task',
            name='repeatevent',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], help_text='Select if the event repeats or not', max_length=2, null=True, verbose_name='Task repeats?'),
        ),
        migrations.AlterField(
            model_name='task',
            name='tasktype',
            field=models.CharField(blank=True, choices=[('S', 'Seasonal'), ('A', 'Annual'), ('M', 'Maintenance')], help_text='Classify the event', max_length=2, null=True, verbose_name='Type of Task'),
        ),
    ]
