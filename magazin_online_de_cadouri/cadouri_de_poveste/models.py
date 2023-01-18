from django.db import models

# Create your models here.

CATEGORIE_PRODUS = [("cadouri_femei", "cadouri_femei"),
                    ("cadouri_barbati", "cadouri_barbati"),
                    ("cadouri_copii", "cadouri_copii"),
                    ("ambalare_cadou", "ambalare_cadou")

]


class Cadou(models.Model):
    nume = models.CharField(max_length=600)
    pret = models.FloatField()
    cod = models.CharField(max_length=200)
    categorie = models.CharField(max_length=200, choices=CATEGORIE_PRODUS)
    descriere = models.CharField(max_length=800)
    poster = models.CharField(max_length=30000, default=None, null=True)

    def __str__(self):
        return f"Cadou(nume = {self.nume}, pret = {self.pret}, cod = {self.cod}, categorie = {self.categorie}, descriere = {self.descriere})"


    def __repr__(self):
        return self.__str__()


class Cos(models.Model):
    data = models.DateTimeField()
    pret_total = models.FloatField()
    numar_cadouri = models.PositiveIntegerField()
    cos_inchis = models.BooleanField(default=False)

    cadouri = models.ManyToManyField(Cadou)    # legatura many-to-many catre modelul/tabela Cadou




