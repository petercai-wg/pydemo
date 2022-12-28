from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from .storages import ProtectedStorage
from django.db.models.signals import pre_save, post_save


class Product(models.Model):
    # id = models.AutoField()
    title = models.CharField(max_length=220)
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    inventory = models.IntegerField(default=0)
    requires_shipping = models.BooleanField(default=False)

    # automatically datetime object
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    updatedby = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    video_link = models.TextField(blank=True, null=True)
    media = models.FileField(storage=ProtectedStorage,
                             upload_to='products/', null=True, blank=True)

    @property
    def can_order(self):
        if self.has_inventory():
            return True
        return False

    @property
    def order_btn_title(self):
        if not self.can_order:
            return "Cannot purchase."
        return "Purchase"

    def has_inventory(self):
        return self.inventory > 0  # True or False

    def remove_items_from_inventory(self, count=1, save=True):
        current_inv = self.inventory
        current_inv -= count
        self.inventory = current_inv
        if save == True:
            self.save()
        return self.inventory


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    report_list = models.TextField(max_length=500, null=True, blank=True)
    modified = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    owner = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Report_Category'


class Report(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    ref_table = models.CharField(
        verbose_name="Reference_table", max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    submit_user = models.ManyToManyField(User)
    modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.name + ":" + self.ref_table

    class Meta:
        db_table = 'Report_Definition'


ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('stale', 'Stale'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'),
)


class Order(models.Model):

    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    status = models.CharField(
        max_length=20, choices=ORDER_STATUS_CHOICES, default='created')
    subtotal = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)

    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    shipping_address = models.TextField(blank=True, null=True)
    # automatically datetime object
    timestamp = models.DateTimeField(auto_now_add=True)
    inventory_updated = models.BooleanField(default=False)

    def get_absolute_url(self):
        return f"/orders/{self.pk}"

    def get_download_url(self):
        return f"/orders/download/{self.pk}/"

    @property
    def is_downloadable(self):
        return True

    def mark_paid(self, custom_amount=None, save=False):
        paid_amount = self.total
        if custom_amount != None:
            paid_amount = custom_amount
        self.paid = paid_amount
        self.status = 'paid'
        if not self.inventory_updated and self.product:
            self.product.remove_items_from_inventory(count=1, save=True)
            self.inventory_updated = True
        if save == True:
            self.save()
        return self.paid

    def calculate(self, save=False):
        if not self.product:
            return {}
        subtotal = self.product.price
        tax_rate = Decimal(0.12)
        tax_total = subtotal * tax_rate
        tax_total = Decimal("%.2f" % (tax_total))
        total = subtotal + tax_total
        total = Decimal("%.2f" % (total))
        totals = {
            "subtotal": subtotal,
            "tax": tax_total,
            "total": total
        }
        for k, v in totals.items():
            setattr(self, k, v)
            if save == True:
                self.save()  # obj.save()
        return totals


def order_pre_save(sender, instance, *args, **kwargs):
    instance.calculate(save=False)


# pre_save.connect(order_pre_save, sender=Order)
