from django.db import models
###
#Diagram: https://dbdiagram.io/d/67b1482b263d6cf9a04aa460
###

# Table: Countries
class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Table: Languages
class Language(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    specifier = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f"Language: {self.name} -> {self.specifier}"

# Table: Sales_Tax
class SalesTax(models.Model):
    id = models.AutoField(primary_key=True)
    sales_tax = models.FloatField(null=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE) # * ---> 1

    def __str__(self):
        return f"{self.sales_tax}% for {self.country.name}"

# Table: ProductType
class ProductType(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255, null=False)

#eg: type 1-> Product; type 2-> Service
    def __str__(self):
        return self.type

# Table: Product
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True, null=False)
    price = models.FloatField(null=False)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE) # * ---> 1
    sales_tax = models.ForeignKey(SalesTax, on_delete=models.SET_NULL, null=True, blank=True) # * ---> 1

    def __str__(self):
        return self.name

# Table: Inventory
class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True) # * ---> 1
    quantity = models.PositiveIntegerField(null=False)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} in stock"

# Table: Bank_Information
class BankInformation(models.Model):
    id = models.AutoField(primary_key=True)
    swift = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.swift

# Table: Credentials
class Credentials(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.description

# Table: User
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, default="")
    auth = models.ForeignKey(Credentials, on_delete=models.CASCADE)
    tax_id = models.IntegerField(null=True, blank=True, default=None)
    bank = models.OneToOneField(BankInformation, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    def __str__(self):
        return self.username

# Table: Financial_Movement
class FinancialMovement(models.Model):
    id = models.AutoField(primary_key=True)
    issue_date = models.DateTimeField(null=False)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sales")
    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="purchases", default=None)
    client_name = models.CharField(max_length=255, null=False, default="N/A")
    client_tax_id = models.IntegerField(null=True, blank=True, default=None)

    def __str__(self):
        return f"Movement {self.id} - {self.issue_date}"

# Table: Financial_Movement_Contents
class FinancialMovementContents(models.Model):
    financial_movement = models.ForeignKey(FinancialMovement, on_delete=models.CASCADE) # * ---> 1
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # * ---> 1
    quantity = models.PositiveIntegerField(null=False, default=1)

    class Meta:
        unique_together = ('financial_movement', 'product')  # Composite key

    def __str__(self):
        return f"Movement {self.financial_movement.id} - {self.product.name} x {self.quantity}"
