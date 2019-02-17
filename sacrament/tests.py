from django.test import TestCase
from datetime import datetime
# Create your tests here.
from .models import Baptism, Profile, Minister, SacramentModel
from parishsystem.enums import Status
class SacramentTestCase(TestCase):

    def setUp(self):
        Profile.objects.create (
            first_name = "Joseph",
            middle_name = "Cortez",
            last_name = "De Leon",
            suffix = "II",
            birthdate = "1993-02-02",
            gender = True,
            birthplace = "San Isidro, Davao Oriental",
            residence = "24 Kalamansi, Manay, Davao Oriental",

        )
        Minister.objects.create(
            first_name="Rodolfo",
            middle_name = "Aquino",
            last_name = "Marquez",
            birthdate = "1956-03-12",

            ministry_type = Minister.PRIEST,
            status = Status.ACTIVE,
        )
        
    def test_baptism_add(self):
        profile = Profile.objects.get(
            first_name="Joseph",
            middle_name = "Cortez",
            last_name = "De Leon",
            suffix = "II",
        )
        Baptism.objects.create(
            date = datetime.now(),
            target_price = 5000.00,
            minister = Minister.objects.get(id=1),
            profile = profile,
            legitimacy = Baptism.NATURAL,
            status = SacramentModel.PENDING
        )

        # get baptism records of guy
        a = profile.baptism.get().target_price
        self.assertEqual(
            a, 5000.00
        )