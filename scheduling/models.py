from django.db import models
from sacrament.models import Baptism, Confirmation, Marriage

# Create your models here.
class Schedule(models.Model):
	SACRAMENT_TYPES_CHOICES = (
		(1, 'Baptism'),
		(2, 'Confirmation'),
		(3, 'Marriage'),
	)

	sacrament_type = models.PositiveSmallIntegerField(choices=SACRAMENT_TYPES_CHOICES, null=True, blank=True)
	# TODO: add schedule classes then push to models dev-

	# Nullable in case the schedule is connected to
	# a sacrament.

	baptism = models.ForeignKey(
		Baptism,
		on_delete=models.PROTECT,
		related_name='schedules',
		null=True,
		blank=True,
	)

	marriage = models.ForeignKey(
		Marriage,
		on_delete=models.PROTECT,
		related_name='schedules',
		null=True,
		blank=True,
	)

	confirmation = models.ForeignKey(
		Confirmation,
		on_delete=models.PROTECT,
		related_name='schedules',
		null=True,
		blank=True,
	)

	# title of the event
	title = models.CharField(max_length=255)
	details = models.TextField(null=True, blank=True)
	start_date_time = models.DateTimeField()
	end_date_time = models.DateTimeField()

	def __str__(self):
		return f'{self.title} - {self.start_date_time.strftime("%Y-%m-%d %H:%M")} to {self.end_date_time.strftime("%Y-%m-%d %H:%M")}'