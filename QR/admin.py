from django.contrib import admin
from .models import (
    Cylinder_Inward_Details,
    Cylinder_Outward_Details,
    Cylinder_Store,
    Cylinder_Type_Master,
    Gas_Cylinder_Vendors_Master,
    GAS_CYLINDER_SCANNER_NAME,
)

admin.site.site_header = GAS_CYLINDER_SCANNER_NAME
admin.site.site_title = GAS_CYLINDER_SCANNER_NAME
admin.site.index_title = "Gas Cylinder Scanner Administration"


@admin.register(Cylinder_Type_Master)
class CylinderTypeMasterAdmin(admin.ModelAdmin):
    list_display = ("cylinder_type_id", "cylinder_gas_type")
    search_fields = ("cylinder_gas_type",)


@admin.register(Gas_Cylinder_Vendors_Master)
class GasCylinderVendorsMasterAdmin(admin.ModelAdmin):
    list_display = (
        "gas_cylinder_vendor_id",
        "gas_cylinder_vendor_name",
        "gas_cylinder_vendor_contact_person",
        "gas_cylinder_vendor_phone",
        "gas_cylinder_vendor_active",
    )
    list_filter = ("gas_cylinder_vendor_active",)
    search_fields = (
        "gas_cylinder_vendor_name",
        "gas_cylinder_vendor_contact_person",
        "gas_cylinder_vendor_phone",
        "gas_cylinder_vendor_email",
    )


@admin.register(Cylinder_Inward_Details)
class CylinderInwardDetailsAdmin(admin.ModelAdmin):
    list_display = ("cylinder_inward_id", "cylinder_po_no", "cylinder_GRN_no", "cylinder_Invoice_DC_no")
    search_fields = ("cylinder_po_no", "cylinder_GRN_no", "cylinder_Invoice_DC_no")


@admin.register(Cylinder_Outward_Details)
class CylinderOutwardDetailsAdmin(admin.ModelAdmin):
    list_display = ("cylinder_outward_id", "cylinder_return_DC", "cylinder_remarks")
    search_fields = ("cylinder_return_DC", "cylinder_remarks")


@admin.register(Cylinder_Store)
class CylinderStoreAdmin(admin.ModelAdmin):
    list_display = (
        "cylinder_db_id",
        "cylinder_sl_r_qr_no",
        "cylinder_vendor_name",
        "cylinder_gas_type",
        "cylinder_Inward",
        "cylinder_Outward",
        "cylinder_stocked_in",
        "cylinder_stock_out",
    )
    list_filter = ("cylinder_Inward", "cylinder_Outward", "cylinder_stocked_in", "cylinder_stock_out")
    search_fields = ("cylinder_sl_r_qr_no", "cylinder_scanned_r_submitted_by")
