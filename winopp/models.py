from django.db import models

# Create your models here.
class Handover2pm(object):
	"""docstring for Handover2pm"""
	ho_id = models.AutoField(primary_key=True)
	customer_name = models.CharField(max_length=250)
	po_date = models.DateField()