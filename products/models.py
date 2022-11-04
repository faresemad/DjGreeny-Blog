from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext as _
from taggit.managers import TaggableManager

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
    image = models.ImageField(_("Image"), upload_to='products/', blank=True)
    flag = models.CharField(_("Flag"),
                            max_length=10,
                            choices=FLAG_OPTION,
                            default='new')
    brand = models.ForeignKey('Brand',
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True,
                              related_name='product_brand')
    category = models.ForeignKey('Category',
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 related_name='product_category')
    tags = TaggableManager()

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def get_absolute_url(self):
        return f"/products/{self.id}"

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='images_products')
    image = models.ImageField(_("Image"), upload_to="products/%y/%m/%d/")

    def __str__(self):
        return str(self.product)


class Brand(models.Model):
    # [name-image]
    name = models.CharField(_("Name"), max_length=100)
    image = models.ImageField(_("Image"), upload_to="brands/%y/%m/%d/")

    def __str__(self):
        return self.name


class Category(models.Model):
    # [name-image]
    name = models.CharField(_("Name"), max_length=100)
    image = models.ImageField(_("Image"), upload_to="categories/%y/%m/%d/")

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    # [product_id-user_id-rating[1:5]-comment-datetime]
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='reviews_products',
                                verbose_name=_("Product"))
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='reviews_users',
                             verbose_name=_("User"))
    rating = models.IntegerField(
        _("Rating"), validators=[MinValueValidator(0),
                                 MaxValueValidator(5)])
    comment = models.TextField(_("Comment"))
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)

    def __str__(self):
        return str(self.user)