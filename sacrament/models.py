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
    last_name = models.CharField(max_length=255)
    suffix = models.CharField(max_length=255)
    class Meta:
        abstract=True

class Profile(PersonAbstractModel):
    birthdate = models.DateField()
    gender = models.BooleanField()
    birthplace = models.CharField(max_length=255)
    residence = models.CharField(max_length=255)

class Minister(PersonAbstractModel):
    birthdate = models.DateField()
    ministry_type = models.SmallIntegerField()
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
