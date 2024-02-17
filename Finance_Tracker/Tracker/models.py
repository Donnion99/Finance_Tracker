from django.db import models

class Finance_Info(models.Model):
    Amount = models.IntegerField()
    BILLS = "BILLS"
    RENT = "RENT"
    FOOD = "FOOD"
    EDUCATION = "EDUCATION"
    MISC = "MISC"
    TRAVEL = "TRAVEL"

    CATEGORIES_CHOICE = {
    BILLS : "Bills",
    RENT : "Rent",
    FOOD : "Food",
    EDUCATION : "Education",
    MISC : "Misc",
    TRAVEL : "Travel",
    }
    Category = models.CharField(
        max_length=10,
        choices=CATEGORIES_CHOICE,
        default=BILLS,
    )
    Date = models.DateField()
    Desc = models.CharField(max_length=50)