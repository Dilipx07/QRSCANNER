from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("QR", "0032_define_gas_cylinder_scanner_and_seed_types"),
    ]

    operations = [
        migrations.AddField(
            model_name="gas_cylinder_vendors_master",
            name="gas_cylinder_vendor_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="gas_cylinder_vendors_master",
            name="gas_cylinder_vendor_address",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AddField(
            model_name="gas_cylinder_vendors_master",
            name="gas_cylinder_vendor_contact_person",
            field=models.CharField(blank=True, default="", max_length=120),
        ),
        migrations.AddField(
            model_name="gas_cylinder_vendors_master",
            name="gas_cylinder_vendor_email",
            field=models.EmailField(blank=True, default="", max_length=254),
        ),
        migrations.AddField(
            model_name="gas_cylinder_vendors_master",
            name="gas_cylinder_vendor_phone",
            field=models.CharField(blank=True, default="", max_length=40),
        ),
    ]
