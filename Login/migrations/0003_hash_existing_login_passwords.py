from django.contrib.auth.hashers import identify_hasher, make_password
from django.db import migrations


def hash_existing_passwords(apps, schema_editor):
    login_model = apps.get_model('Login', 'qr_scanner_login')
    for login in login_model.objects.exclude(qr_scanned_password__isnull=True):
        password = login.qr_scanned_password
        try:
            identify_hasher(password)
            continue
        except ValueError:
            login.qr_scanned_password = make_password(password)
            login.save(update_fields=['qr_scanned_password'])


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_rename_qr_scanner_master_qr_scanner_login'),
    ]

    operations = [
        migrations.RunPython(hash_existing_passwords, migrations.RunPython.noop),
    ]
