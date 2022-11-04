from django.db import models
# import translation module
from django.utils.translation import gettext as _

FLAG_OPTION = [
    ('new', _('New')),
    ('sale', _('Sale')),
    ('featured', _('Featured')),
]

# Create your models here.
class Product(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    sku = models.IntegerField(_("SKU"))
    subtitle = models.CharField(_("Subtitle"), max_length=100)
    description = models.TextField(_("Description"))
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2)
    quantity = models.IntegerField(_("Quantity"))
    flag = models.CharField(_("Flag"), max_length=10, choices=FLAG_OPTION, default='new')
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def get_absolute_url(self):
        return f"/products/{self.id}"

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    pass


class Brand(models.Model):
    pass


class Category(models.Model):
    pass


class ProductReview(models.Model):
    pass