# from django.db import models

# # Create your models here.


# class ProductModel(models.Model):
#     prod_name = models.TextField(max_length=100)
#     prod_image = models.FileField(upload_to="resumes/", default=None)
#     prod_price = models.FileField(upload_to="product_pictures/", default=None)
#     prod_description = models.TextField(max_length=255, default=None)

#     class Meta:
#         db_table = "product"


#         def __str__(self):
#             return self.prod_name