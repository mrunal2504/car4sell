from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    state_choice = (
        ('AN', 'Andaman and Nicobar'),
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CH', 'Chandigarh'),
        ('DN', 'Dadra and Nagar Haveli'),
        ('DD', 'Daman and Diu'),
        ('DL', 'Delhi'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JK', 'Jammu and Kashmir'),
        ('KA', 'Karnataka'),
        ('KL', 'Kerala'),
        ('KY', 'Kentucky'),
        ('LD', 'Lakshadweep'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('NL', 'Nagaland'),
        ('OR', 'Orissa'),
        ('PY', 'Pondicherry'),
        ('PN', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('SK', 'Sikkim'),
        ('TN', 'TamilNadu'),
        ('TR', 'Tripura'),
        ('UP', 'Uttar Pradesh'),
        ('WB', 'West Bengal'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    car_id = models.IntegerField()
    customer_need = models.CharField(max_length=100)
    car_title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(choices=state_choice, max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    create_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email
