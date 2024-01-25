from django.db.models import Model, CharField, IntegerField, DecimalField, DateTimeField
from django.core.validators import MaxValueValidator

# Create your models here.
class Booking(Model):
  # id = IntegerField(primary_key=True, validators=[MaxValueValidator(99999999999)])
  name = CharField(max_length=255)
  no_of_guests = IntegerField(validators=[MaxValueValidator(999999)])
  booking_date = DateTimeField()

  def __str__(self) -> str:
    return f'{self.name} | Guests: {self.no_of_guests} | Date: {self.booking_date}'

class MenuItem(Model):
  # id = IntegerField(primary_key=True, validators=[MaxValueValidator(99999)])
  title = CharField(max_length=255)
  price = DecimalField(max_digits=10, decimal_places=2)
  inventory = IntegerField(default=0)

  def __str__(self) -> str:
    return f'{self.title} : {str(self.price)}'
