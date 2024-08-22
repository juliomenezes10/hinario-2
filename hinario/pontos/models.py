from django.db import models
from django.utils.text import slugify

from django.conf import settings

# Create your models here.
class CreateHinario(models.Model):
    CHOICES = (
        ("Hino da Umbanda", "Hino da Umbanda"),
        ("Hinos da Ayahuasca", "Hinos da Ayahuasca"),
        ("Hinario do Mestre Irineu", "Hinario do Mestre Irineu"),
        ("Abertura", "Abertura"),
        ("Saldação da Porteira", "Saldação da Porteira"),
        ("Defumação", "Defumação"),
        ("Descarrego", "Descarrego"),
        ("Encerramento", "Encerramento"),
        ("Oxalá", "Oxalá"),
        ("Ogum", "Ogum"),
        ("Omulu/Obaluaê", "Omulu/Obaluaê"),
        ("Iemanjá", "Iemanjá"),
        ("Xangô", "Xangô"),
        ("Oxossi", "Oxossi"),
        ("Oxum", "Oxum"),
        ("Iansã", "Iansã"),
        ("Nanã Buruquê", "Nanã Buruquê"),
        ("Crianças", "Crianças"),
        ("Marinheiros/Marujos", "Marinheiros/Marujos"),
        ("Boiaderos", "Boiaderos"),
        ("Baianos", "Baianos"),
        ("Pretos Velhos", "Pretos Velhos"),
        ("Caboclos", "Caboclos"),
        ("Exus/Pomba Giras", "Exus/Pomba Giras")
    )

    categoria = models.CharField(max_length=300, choices= CHOICES)
    slug = models.SlugField(max_length=300, blank=True, null=True, unique=True)

    def __str__(self):
        return self.categoria
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.categoria)

        super().save(*args, **kwargs)

class Ponto(models.Model):
    category = models.ForeignKey(CreateHinario, on_delete=models.PROTECT)
    ponto = models.TextField()
    audio = models.FileField(upload_to="", max_length=100, blank=True)
    urlYoutube = models.URLField(max_length=200, blank=True)
    dateofpost = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{str(self.ponto)}"
  