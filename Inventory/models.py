from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid #Required for unique Mobile Instance

# Create your models here.
class Category(models.Model):
    category=models.CharField(max_length=250, help_text="Enter category such as Electronics, Furniture etc")
    def __str__(self):
        return self.category
    class Meta:
        verbose_name_plural = "1. Category"

class Type(models.Model):
        #fields
    type=models.CharField(max_length=100,help_text="Enter Type")
    def __str__(self):
        """String for representing Device Object in Admin site etc"""
        return self.type
    class Meta:
        verbose_name_plural = "2. Type"

class Items(models.Model):
    name=models.CharField(max_length=200)
            # Foreign Key used because mobile can only have one brand, but brands can have multiple mobiles
    # brand as a string rather than object because it hasn't been declared yet in the file
    brand= models.ForeignKey('brand', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the mobile')
    Quantity=models.IntegerField()
    Cost=models.IntegerField()
    SellPrice=models.IntegerField()
    Date = models.DateField(null=True, blank=True)
    Status_Types = (
            ('In Stock', 'Available'),
            ('Out of Stock', 'Out of Stock'),
            ('On way', 'On way'),
            ('Reserved', 'Reserved'),
        )

    status = models.CharField(
            max_length=100,
            choices=Status_Types,
            blank=True,
            default='In Stock',
            help_text='Availability',
        )

               # ManyToManyField used because Device can contain many mobiles. mobile can cover many devices.
    # Device class has already been defined so we can specify the object above.
    type_name = models.ManyToManyField(Type, help_text='Select a Type for this Item')
    category_name = models.ManyToManyField(Category, help_text='Select a Category for this Item')

    def __str__(self):
        #"""String for representing the Model object."""
        return self.name
    #Methods

    def display_category(self):
            #    """Create a string for the device. This is required to display genre in Admin."""
            return ', '.join(category_name.category for category_name in self.category_name.all())

    def get_absolute_url(self):
        #"""Returns the url to access a detail record for this item."""
        return reverse('item-detail', args=[str(self.id)])
    def display_type(self):
            #    """Create a string for the device. This is required to display genre in Admin."""
        return ', '.join(type_name.type for type_name in self.type_name.all())

    display_type.short_description = 'Type'


    class Meta:
         verbose_name_plural = "4. Items"

class ItemDetail(models.Model):
    #modle representing the specific parts of a mobile
    #id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    item=models.ForeignKey('Items',on_delete=models.SET_NULL,null=True)
    Color_types=(
        ('Red','Red'),
        ('BLK','Black'),
        ('WHT','White'),
        ('GLD','Gold'),
    )
    color=models.CharField(max_length=10,choices=Color_types,blank=True,default='BLK')
    condition=models.CharField(max_length=100,null=True)


    def display_item(self):
        #    """Create a string for the device. This is required to display genre in Admin."""
        return ', '.join(item.name for item in self.item.all())


    class Meta:
        verbose_name_plural="5. Item-Details"

    def __str__(self):
        #"""String for representing the Mobile object."""
        return str(self.item)


class Brand(models.Model):
    """Model representing   Brand."""
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "3. Brand"

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('brand-detail', args=[str(self.id)]) #View on Site (front-end)

    def __str__(self):
        """String for representing the Model object."""
        return self.name
