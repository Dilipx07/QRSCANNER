from django.db import models
from django.contrib.auth.hashers import check_password, identify_hasher, make_password


class qr_scanner_login(models.Model):
    qr_scanner_id = models.BigAutoField(primary_key=True,unique=True)
    qr_scanned_name = models.CharField(max_length=150,null=True)
    qr_scanned_password = models.CharField(max_length=150,null=True)

    class Meta:
        verbose_name = "Gas Cylinder Scanner Login"
        verbose_name_plural = "Gas Cylinder Scanner Logins"

    def __str__(self):
        return self.qr_scanned_name or f"Login {self.qr_scanner_id}"

    def has_usable_password(self):
        if not self.qr_scanned_password:
            return False
        try:
            identify_hasher(self.qr_scanned_password)
            return True
        except ValueError:
            return False

    def set_password(self, raw_password):
        self.qr_scanned_password = make_password(raw_password)

    def check_password(self, raw_password):
        if not self.qr_scanned_password:
            return False
        if self.has_usable_password():
            return check_password(raw_password, self.qr_scanned_password)
        return False
