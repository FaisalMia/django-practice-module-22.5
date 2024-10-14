# Generated by Django 5.0.7 on 2024-09-17 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_alter_transaction_transaction_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='is_bankrupt',
        ),
        migrations.AddField(
            model_name='transaction',
            name='recipient_balance_after_transaction',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]