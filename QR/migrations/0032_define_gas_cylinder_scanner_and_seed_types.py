from django.db import migrations


DEFAULT_CYLINDER_TYPES = (
    "Oxygen",
    "Nitrogen",
    "Carbon Dioxide",
    "Argon",
    "Hydrogen",
    "Helium",
    "LPG",
    "Acetylene",
)


def seed_cylinder_types(apps, schema_editor):
    cylinder_type_master = apps.get_model("QR", "Cylinder_Type_Master")
    for cylinder_type in DEFAULT_CYLINDER_TYPES:
        cylinder_type_master.objects.get_or_create(cylinder_gas_type=cylinder_type)


class Migration(migrations.Migration):

    dependencies = [
        ("QR", "0031_cylinder_inward_details_cylinder_outward_details_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cylinder_type_master",
            options={
                "ordering": ["cylinder_gas_type"],
                "verbose_name": "Gas Cylinder Type",
                "verbose_name_plural": "Gas Cylinder Types",
            },
        ),
        migrations.AlterModelOptions(
            name="gas_cylinder_vendors_master",
            options={
                "ordering": ["gas_cylinder_vendor_name"],
                "verbose_name": "Gas Cylinder Vendor",
                "verbose_name_plural": "Gas Cylinder Vendors",
            },
        ),
        migrations.AlterModelOptions(
            name="cylinder_inward_details",
            options={
                "verbose_name": "Gas Cylinder Inward Detail",
                "verbose_name_plural": "Gas Cylinder Inward Details",
            },
        ),
        migrations.AlterModelOptions(
            name="cylinder_outward_details",
            options={
                "verbose_name": "Gas Cylinder Outward Detail",
                "verbose_name_plural": "Gas Cylinder Outward Details",
            },
        ),
        migrations.AlterModelOptions(
            name="cylinder_store",
            options={
                "ordering": ["-cylinder_db_id"],
                "verbose_name": "Gas Cylinder Scanner Record",
                "verbose_name_plural": "Gas Cylinder Scanner Records",
            },
        ),
        migrations.RunPython(seed_cylinder_types, migrations.RunPython.noop),
    ]
