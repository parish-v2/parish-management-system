from django.db import models
from parishsystem.enums import Status


# Create your models here.
class SacramentModel(models.Model):
    APPROVED = 0
    DECLINED = 1
    PENDING = 2
    FINISHED = 3
    _STATUS_CHOICES = (
        (APPROVED, "Approved"),
        (DECLINED, "Declined"),
        (PENDING, "Pending"),
        (FINISHED, "Finished"),
    )
    """Base class of all sacraments
    """
    status = models.SmallIntegerField(choices=_STATUS_CHOICES)
    registry_number = models.CharField(max_length=64, null=True, blank=True)
    record_number = models.CharField(max_length=64, null=True, blank=True)
    page_number = models.CharField(max_length=64, null=True, blank=True)
    remarks = models.CharField(max_length=1024, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    target_price = models.DecimalField(null=True,blank=True, max_digits=16, decimal_places=2)

    class Meta:
        # This class is abstract and will not be used
        # on its own.
        abstract=True

class Baptism(SacramentModel):

    # TODO: Change this to actual legitimacy types
    NATURAL = 0
    _CHOICES = (
        (NATURAL, "Natural"),
    )
    # prevent deletion of referenced object by
    # using models.PROTECT on delete.
    minister = models.ForeignKey(
        'Minister', 
        on_delete=models.PROTECT, 
        related_name="baptisms",
        null=True,
        blank=True
    )
    profile = models.ForeignKey(
        'Profile',
        on_delete=models.PROTECT,
        related_name="baptism"
    )
    legitimacy = models.SmallIntegerField(max_length=1, choices=_CHOICES)
    
    

class Marriage(SacramentModel):

    # prevent deletion of referenced object by
    # using models.PROTECT on delete.
    minister = models.ForeignKey(
        'Minister', 
        on_delete=models.PROTECT, 
        related_name="marriages",
        null=True,
        blank=True
    )
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
    
    # prevent deletion of referenced object by
    # using models.PROTECT on delete.
    minister = models.ForeignKey(
        'Minister', 
        on_delete=models.PROTECT, 
        related_name="confirmations",
        null=True,
        blank=True
    )
    # All fields are defined in SacramentsModel.
    profile = models.ForeignKey(
        'Profile',
        on_delete=models.PROTECT,
        related_name="confirmation"
    )

"""
Sacraments
"""



class Invoice(models.Model):
    date_issued = models.DateField()
    or_number = models.CharField(max_length=255)
    received_by = models.CharField(max_length=255) # name that appears on the actual invoice
    profiles_id = [] # profiles that are connected to this invoice item
    pass

class InvoiceItems(models.Model):
    invoice = models.ForeignKey(
        'Invoice', 
        on_delete=models.CASCADE,
        related_name='invoice_items',
    )
    quantity = models.IntegerField() # defaults to 1 if item type is sacrament
    balance = models.DecimalField(max_digits=16, decimal_places=2)  # the amount needed to be paid (remaining)
    amount_paid = models.DecimalField(max_digits=16, decimal_places=2) # actual amount paid
    # the next invoice item's balance is computed by this invoice items's balance and amount_paid.



class ItemType(models.Model):
    name = models.CharField(max_length=255)
    suggested_price = models.DecimalField(max_digits=16, decimal_places=2)


class PersonAbstractModel(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    suffix = models.CharField(max_length=255, null=True, blank=True)
    class Meta:
        abstract=True
    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

class Profile(PersonAbstractModel):
    birthdate = models.DateField()
    gender = models.BooleanField()
    birthplace = models.CharField(max_length=255, null=True, blank=True)
    residence = models.CharField(max_length=255, null=True, blank=True)
        
class Minister(PersonAbstractModel):
    # Constants in Minister class
    CARDINAL = 0
    ARCHBISHOP = 1
    BISHOP = 2
    PRIEST = 3
    MINISTER_CHOICES = (
        (CARDINAL, "Cardinal"),
        (ARCHBISHOP, "Archbishop"),
        (BISHOP, "Bishop"),
        (PRIEST, "Priest"),
    )
    birthdate = models.DateField()
    ministry_type = models.SmallIntegerField(max_length=1, choices=MINISTER_CHOICES)
    status = models.SmallIntegerField()

    


class Sponsor(PersonAbstractModel):
    confirmation = models.ForeignKey(
        'Confirmation',
        on_delete=models.PROTECT,
        related_name='sponsors',
        null=True,
        blank=True,
    )
    baptism = models.ForeignKey(
        'Baptism',
        on_delete=models.PROTECT,
        related_name='sponsors',
        null=True,
        blank=True,
    )
    marriage = models.ForeignKey(
        'Marriage',
        on_delete=models.PROTECT,
        related_name='sponsors',
        null=True,
        blank=True,
    )
    residence = models.CharField(max_length=511)
    
