from django.db import models

GAS_CYLINDER_SCANNER_NAME = "Gas Cylinder Scanner"

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

class Cylinder_Type_Master(models.Model):
    cylinder_type_id = models.BigAutoField(primary_key=True,unique=True)
    cylinder_gas_type = models.CharField(null=False,unique=True)

    class Meta:
        verbose_name = "Gas Cylinder Type"
        verbose_name_plural = "Gas Cylinder Types"
        ordering = ["cylinder_gas_type"]

    def __str__(self):
        return self.cylinder_gas_type

class Gas_Cylinder_Vendors_Master(models.Model):
    gas_cylinder_vendor_id = models.BigAutoField(primary_key=True,unique=True)
    gas_cylinder_vendor_name = models.CharField(unique=True,null=False)
    gas_cylinder_vendor_contact_person = models.CharField(max_length=120, blank=True, default="")
    gas_cylinder_vendor_phone = models.CharField(max_length=40, blank=True, default="")
    gas_cylinder_vendor_email = models.EmailField(blank=True, default="")
    gas_cylinder_vendor_address = models.TextField(blank=True, default="")
    gas_cylinder_vendor_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Gas Cylinder Vendor"
        verbose_name_plural = "Gas Cylinder Vendors"
        ordering = ["gas_cylinder_vendor_name"]

    def __str__(self):
        return self.gas_cylinder_vendor_name

    @property
    def vendor_detail_label(self):
        details = [
            self.gas_cylinder_vendor_contact_person,
            self.gas_cylinder_vendor_phone,
            self.gas_cylinder_vendor_email,
        ]
        detail_text = " | ".join(item for item in details if item)
        return f"{self.gas_cylinder_vendor_name} - {detail_text}" if detail_text else self.gas_cylinder_vendor_name

class Cylinder_Inward_Details(models.Model):
    cylinder_inward_id = models.BigAutoField(primary_key=True,unique=True)
    cylinder_po_no = models.CharField()
    cylinder_po_Date = models.DateField()
    cylinder_GRN_no= models.CharField(unique=True)
    cylinder_GRN_Date = models.DateField()
    cylinder_Invoice_DC_no = models.CharField(unique=True)
    cylinder_description = models.CharField()

    class Meta:
        verbose_name = "Gas Cylinder Inward Detail"
        verbose_name_plural = "Gas Cylinder Inward Details"

    def __str__(self):
        return f"Inward {self.cylinder_GRN_no}"

class Cylinder_Outward_Details(models.Model):
    cylinder_outward_id = models.BigAutoField(primary_key=True,unique=True)
    cylinder_return_DC = models.CharField(unique=True)
    cylinder_remarks = models.CharField(null=True)

    class Meta:
        verbose_name = "Gas Cylinder Outward Detail"
        verbose_name_plural = "Gas Cylinder Outward Details"

    def __str__(self):
        return f"Outward {self.cylinder_return_DC}"

# Cylinder Store.
class Cylinder_Store(models.Model):
    cylinder_db_id = models.BigAutoField(primary_key=True,unique=True)
    cylinder_sl_r_qr_no = models.CharField()
    cylinder_vendor_name = models.ForeignKey(Gas_Cylinder_Vendors_Master,on_delete=models.SET,default=None)
    cylinder_gas_type = models.ForeignKey(Cylinder_Type_Master,on_delete=models.SET,default=None)
    cylinder_scanned_r_submitted_date = models.DateTimeField(default=None,null=True)
    cylinder_scanned_r_submitted_by = models.CharField(max_length=300)
    cylinder_Inward = models.BooleanField(default=False)
    cylinder_Inward_Date = models.DateTimeField(null=True)
    cylinder_Outward = models.BooleanField(default=False)
    cylinder_Outward_Date = models.DateTimeField(null=True)
    cylinder_stocked_in = models.BooleanField(default=False)
    cylinder_stocked_in_Date = models.DateTimeField(null=True)
    cylinder_stock_out = models.BooleanField(default=False)
    cylinder_stock_out_Date = models.DateTimeField(null=True)
    Cylinder_Inward_Table = models.ForeignKey(Cylinder_Inward_Details,on_delete=models.SET,null=True)
    Cylinder_Outward_Table = models.ForeignKey(Cylinder_Outward_Details,on_delete=models.SET,null=True)

    class Meta:
        verbose_name = "Gas Cylinder Scanner Record"
        verbose_name_plural = "Gas Cylinder Scanner Records"
        ordering = ["-cylinder_db_id"]

    def __str__(self):
        return self.cylinder_sl_r_qr_no
