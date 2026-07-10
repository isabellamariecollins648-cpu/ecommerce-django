# Generated for Cash on Delivery support

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0005_feedback_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='payment_method',
            field=models.CharField(choices=[('Online Payment', 'Online Payment (Card/MoMo)'), ('Cash on Delivery', 'Cash on Delivery')], default='Online Payment', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='payment_status',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], default='Unpaid', max_length=10, null=True),
        ),
    ]
