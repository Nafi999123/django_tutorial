from django.db import models

class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()  # Fixed typo

    def __str__(self):
        return self.dep_name

class Doctors(models.Model):
    doc_name = models.CharField(max_length=400)
    doc_spec = models.CharField(max_length=400)
    dep_name = models.ForeignKey(Departments, on_delete=models.CASCADE, related_name='doctors')  # Improved FK
    doc_image = models.ImageField(upload_to='doctors')  # Ensured correct syntax

    def __str__(self):
        return  'Dr ' + self.doc_name + '- ('+ self.doc_spec + ')'

class Booking(models.Model):
    p_name = models.CharField(max_length=255)
    p_phone= models.CharField(max_length=10)
    p_email=models.EmailField()
    doc_name =models.ForeignKey(Doctors,on_delete=models.CASCADE)
    Booking_date=models.DateField()
    booked_on = models.DateField(auto_now=True)
    @property
    def booking_date(self):
        return self.booked_on.date()
