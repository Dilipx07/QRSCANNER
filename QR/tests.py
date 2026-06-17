from django.test import TestCase
from .models import Cylinder_Type_Master, DEFAULT_CYLINDER_TYPES


class CylinderTypeSeedDataTests(TestCase):
    def test_default_cylinder_types_are_seeded(self):
        seeded_types = set(
            Cylinder_Type_Master.objects.filter(
                cylinder_gas_type__in=DEFAULT_CYLINDER_TYPES
            ).values_list("cylinder_gas_type", flat=True)
        )

        self.assertEqual(seeded_types, set(DEFAULT_CYLINDER_TYPES))
