from django.db import models

# Create your models here.
class Handover2pm(models.Model):
	"""docstring for Handover2pm"""
	# ho_id = models.AutoField(primary_key=True)
	customer_name = models.CharField(max_length=250)
	project_name = models.CharField(max_length=250)
	po_date = models.DateField()
	po_known_date = models.DateField()
	initial_ho = models.DateField()
	approve_ho = models.DateField()
	remark = models.TextField()
	def __str__(self):
		return self.project_name