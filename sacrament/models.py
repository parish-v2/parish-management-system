from django.db import models

# Create your models here.
class SacramentModel(models.Model):
    """Base class of all sacraments
    """
    # prevent deletion of referenced object by
    # using models.PROTECT on delete.
    minister = models.ForeignKey(
        'Minister', 
        on_delete=models.PROTECT, 
        related_name="baptisms"
    )
    status = models.SmallIntegerField()
    registry_number = models.CharField(max_length=64)
    record_number = models.CharField(max_length=64)
    page_number = models.CharField(max_length=64)
    remarks = models.CharField(max_length=1024)
    date = models.DateTimeField()
    target_price = models.DecimalField(max_digits=16, decimal_places=2)

    class Meta:
        # This class is abstract and will not be used
        # on its own.
        abstract=True

class Baptism(SacramentModel):
    profile = models.ForeignKey(
        'Profile',
        on_delete=models.PROTECT,
        related_name="baptism"
    )
    legitimacy = models.SmallIntegerField()
    

class Marriage(SacramentModel):
    groom_profile = models.ForeignKey(
        'Profile',
        on_delete=models.PROTECT,
        related_name='grooms'
    )
    bride_profile = models.ForeignKey(
        'Profile',
        on_delete=models.PROTECT,
        related_name='brides'
    )


class Confirmation(models.Model):
    # All fields are defined in SacramentsModel.
    pass