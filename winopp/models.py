from django.db import models

# Create your models here.
class Handover2pm(models.Model):
	"""docstring for Handover2pm"""
	# ho_id = models.AutoField(primary_key=True)
	status = (
			('0', 'Project Charter - Draft'),
			('1', 'Project Charter - Approval GM Presales'),
			('2', 'Project Charter - Approval GM PM'),
			('3', 'Project Charter - Approval PM'),
			('4', 'Project Charter - Approved | Handover - Draft'),
			('5', 'Handover - Approval PM'),
			('6', 'Handover - Approved'),
		)
	customer = models.ManyToManyField('Customer')
	project_name = models.CharField(max_length=250)
	po_date = models.DateField()
	po_known_date = models.DateField()
	initial_ho = models.DateField(blank=True)
	pmois_status = models.CharField(max_length=1, choices=status)
	approve_ho = models.DateField(blank=True)
	remark = models.TextField(blank=True)

	table_updated = models.DateField(auto_now=True, auto_now_add=False)
	table_creation_timestamp = models.DateField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.project_name

class Customer(models.Model):
	segment = (
			('0', 'Banking 1'),
			('1', 'Banking 2'),
			('2', 'Finance Non-Bank'),
			('3', 'Supply Chain'),
			('4', 'Public Sector 1'),
			('5', 'Public Sector 2'),
			('6', 'Resources'),
			('7', 'Telco'),
		)
	customer_name = models.CharField(max_length=100)
	customersegment = models.CharField(max_length=1, choices=segment)

	def __str__(self):
		return self.customer_name