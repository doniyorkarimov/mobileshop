from django.db import models
import uuid

class Category(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name

DEFAULT = './f74f39dbc9b60954c926d72401adf1cc.jpg'

class Product(models.Model):
    regions = [
        ('Toshkent', 'Toshkent'),
        ('Toshkent viloyati', 'Toshkent viloyati'),
        ('Samarkand', 'Samarkand'),
        ('Navoiy', 'Navoiy'),
        ('Andijon', 'Andijon'),
        ('Xorazm', 'Xorazm'),
        ('Buxoro', 'Buxoro'),
        ('Qoroqolg\'iston', 'Qoroqolg\'iston'),
        ('Farg\'ona', 'Farg\'ona'),
        ('Surxondaryo', 'Surxondaryo'),
        ('Sirdaryo', 'Sirdaryo'),
        ('Namangan', 'Namangan'),
        ('Jizzah', 'Jizzah'),
    ]


    Category = models.ForeignKey(Category, max_length=200, blank=True, null=True, on_delete=models.SET_NULL)
    Model = models.CharField(max_length=200, blank=True, null=True)
    Joylashuv = models.CharField(max_length=50, blank=True, null=True, choices=regions)
    Yetkazib_berish = models.IntegerField(default=0, blank=True, null=True)
    Oldindan_tulov = models.IntegerField(default=0, blank=True, null=False)
    General_image = models.ImageField(blank=True, null=True, default=DEFAULT)
    image1 = models.ImageField(blank=True, null=True, default=DEFAULT)
    image2 = models.ImageField(blank=True, null=True, default=DEFAULT)
    Narxi = models.IntegerField(default=0, blank=True, null=True)
    Chegirma_narxi_bilan = models.IntegerField(blank=True, null=True)
    Kredit = models.CharField(max_length=200, blank=True, null=True)
    Kerakli_hujjatlar = models.CharField(max_length=200, blank=True, null=True, default='Passport/ID Karta, Plastik Karta')
    Raqam1 = models.CharField(max_length=200, blank=True, null=True, default='+998 71 123 45 67')
    Raqam2 = models.CharField(max_length=200, blank=True, null=True, default='+998 71 123 45 67')
    Kafolat = models.CharField(max_length=70, null=True, blank=True, default='12 oy')
    OS_versiyasi_ishga_tushirilganda = models.CharField(max_length=100, null=True, blank=True)
    SIM_kartalar_soni = models.IntegerField(null=True, blank=True, default='1')
    SIM_karta_turi = models.CharField(max_length=100, null=True, blank=True)
    Ogirligi = models.CharField(max_length=100, null=True, blank=True)
    ulchamlari_WxHxD = models.CharField(max_length=100, null=True, blank=True)
    rang = models.CharField(max_length=100, null=True, blank=True)
    rasm_hajmi = models.CharField(max_length=100, null=True, blank=True)
    tirnalishga_chidamli_shisha = models.CharField(max_length=100, null=True, blank=True)
    Asosiy_kameralar_soni = models.CharField(max_length=100, null=True, blank=True)
    Asosiy_kameralarning_ulchamlari = models.CharField(max_length=100, null=True, blank=True)
    Old_kamera = models.CharField(max_length=100, null=True, blank=True)
    Audio = models.CharField(max_length=100, null=True, blank=True)
    Interfeyslar = models.CharField(max_length=100, null=True, blank=True)
    Geopozitsiyalash = models.CharField(max_length=100, null=True, blank=True)
    Markaziy_protsessor = models.CharField(max_length=100, null=True, blank=True)
    Protsessor_yadrolari_soni = models.CharField(max_length=100, null=True, blank=True)
    video_protsessor = models.CharField(max_length=100, null=True, blank=True)
    Urnatilgan_xotira = models.CharField(max_length=100, null=True, blank=True)
    RAM = models.CharField(max_length=100, null=True, blank=True)
    Batareya = models.CharField(max_length=100, null=True, blank=True)
    Zaryadlovchi_ulagichi_turi = models.CharField(max_length=100, null=True, blank=True)
    Batareya_quvvati = models.CharField(max_length=100, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    @property
    def oyma_oy_tulov(self):
        # Agar chegirma narxi mavjud bo‘lsa, u narxni tanlaymiz; aks holda asl narxni.
        price = self.Chegirma_narxi_bilan if self.Chegirma_narxi_bilan is not None else self.Narxi
        if not price:
            return 0
        # Oldindan tolovni xavfsiz tarzda olish (None bo‘lsa 0 bo‘ladi)
        down_payment = self.oldindan_tulov_safe
        remaining = price - down_payment
        # Qolgan miqdor manfiy bo‘lib qolmasligi uchun:
        if remaining < 0:
            remaining = 0
        # Natijani 12 oyga bo‘lamiz
        return int(remaining / 12)

    @property
    def oldindan_tulov_safe(self):
        return self.Oldindan_tulov if self.Oldindan_tulov is not None else 0

    def __str__(self):
        return self.Model

class Contact(models.Model):
    Ismi = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    Xabar = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.email


    # telefon_admin
    # 159753