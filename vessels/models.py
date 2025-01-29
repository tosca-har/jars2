from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

class Report(models.Model):
    slug = models.SlugField(default="", blank= True, null = False, db_index=True)
    name = models.CharField(max_length= 20, blank=True)
    fullname = models.CharField(max_length= 100, blank=True)
    author_list = models.CharField(max_length= 500, null=True)
    details = models.TextField(max_length= 1000, null=True, blank=True)
    link = models.CharField(max_length= 100, blank=True, null=True)
    doi = models.CharField(max_length= 255, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.slug} ({self.fullname})"  
    
    def get_absolute_url(self):
        return reverse(
            'vessels:report',
            args=[self.slug]
        )

class Image(models.Model):
    slug = models.SlugField(default="", blank= True, null = False, db_index=True)
    name = models.CharField(max_length= 100)
    imageloc = models.CharField(max_length= 100)
    details = models.TextField(max_length= 1000, null=True, blank=True)
    ref = models.ForeignKey(Report, on_delete=models.SET_NULL, null=True, related_name="image", blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.slug} ({self.name})"  


class Sitegroup(models.Model):
    slug = models.SlugField(default="", blank= True, null = False, db_index=True)
    name = models.CharField(max_length= 100)
    details = models.TextField(max_length= 1000, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.slug} ({self.name})"  
    
class Vesselgroup(models.Model):
    slug = models.SlugField(default="", blank= True, null = False, db_index=True)
    name = models.CharField(max_length= 100)
    time_start = models.IntegerField(null=True, blank =True)
    time_start_ref = models.ForeignKey(Report, on_delete=models.SET_NULL, null=True, related_name="vg_time_start", blank=True)
    time_end = models.IntegerField(null=True, blank =True)
    time_end_ref = models.ForeignKey(Report, on_delete=models.SET_NULL, null=True, related_name="vg_time_end", blank=True)
    sitegroup = models.ManyToManyField(Sitegroup, related_name="vesselgroups", blank=True)
    details = models.TextField(max_length= 1000, null=True, blank=True)
    refs = models.ManyToManyField(Report, related_name="vesselgroups", blank=True)
    vg = models.ManyToManyField("self", symmetrical=False, null=True, blank=True)
    image = models.ManyToManyField(Image, related_name="vesselgroups", blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.slug} ({self.name})"  
    
    def get_absolute_url(self):
        return reverse(
            'vessels:vesselgr',
            args=[self.slug]
        )

class Feature(models.Model):
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    name = models.CharField(default="", max_length=50)
    description = models.TextField(max_length= 1000, null=True, blank=True)
    refs = models.ManyToManyField(Report, related_name="feature", blank=True)
    image = models.ManyToManyField(Image, related_name="feature", blank=True)


class Vessel(models.Model):
    class Types(models.TextChoices):
        RESTRICTED = 'RP', 'restricted-pot'
        UNRESTRICTED = 'UP', 'unrestricted-pot'
        SEMIRESTRICTED = 'SP', 'semirestricted-pot' 
        BOWL = 'B', 'bowl'
        FORNO = 'F', 'forno'
        CUP = 'C', 'cup'
        JUG = 'J', 'jug'
        OTHER = 'O', 'other'
        UNKNOWN = 'U', 'unknown'

    class Gender(models.TextChoices):
        WOMEN = 'W', 'women'
        MEN = 'M', 'men'
        BOTH = 'B', 'both'
        UNKNOWN = 'U', 'unknown'

    class Frequency(models.TextChoices):
        PRESENT = 'P', 'present'
        DOMINANT = 'D', 'dominant'
        COMMON = 'C', 'common'
        OCCASIONAL = 'O', 'occasional'
        RARE = 'R', 'rare'
        ABSENT = 'A', 'absent'
        UNKNOWN = 'U', 'unknown'

    class Region(models.TextChoices):
        MARIANAS = 'MAR', 'Marianas'
        CAROLINES = 'CAR', 'Carolines'
        BISMARCK = 'BIS', 'Bismarck'
        PNG = 'PNG', 'PNG'
        SOLOMONS = 'SOL', 'Solomons'
        VANUATU = 'VAN', 'Vanuatu'
        MALUKU = 'MAL', 'Maluku'
        NEWCAL = 'NCA', 'New Caledonia'
        FIJI = 'FIJ', 'Fiji'
        SAMOA = 'SAM', 'Samoa'
        TONGA = 'TON', 'Tonga'
        MARQUESA = 'MAQ', 'Marquesa'
        NEMELANESIA = 'NME', 'NE Melanesia'
        COOK = 'COO', 'Cook'
        TUVALU = 'TUV', 'Tuvalu'
        UNKNOWN = 'U', 'unknown'

    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    name = models.CharField(default="", max_length=50)
    vesselgroup = models.ManyToManyField(Vesselgroup, related_name="vessels", blank=True)
    form = models.CharField(max_length=2, choices=Types, default=Types.UNKNOWN)
    time_start = models.IntegerField(null=True, blank =True)
    time_end = models.IntegerField(null=True, blank =True)
    region = models.CharField(max_length=20, choices=Region, default=Region.UNKNOWN)
    language = models.CharField(default="", max_length=50, null=True, blank =True)
    language_code = models.CharField(default="", max_length=5, null=True, blank =True)
    word = models.CharField(default="", max_length=50, null=True, blank = True)
    details = models.TextField(max_length= 1000, null=True, blank=True)
    language_family = models.CharField(null=True, max_length=500, blank =True)
    language_superfamily = models.CharField(null=True, max_length=100, blank =True)
    gender_make = models.CharField(max_length=7, choices=Gender, default=Gender.UNKNOWN)
    gender_decorate = models.CharField(max_length=7, choices=Gender, default=Gender.UNKNOWN)
    has_neck = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    has_round_base = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    has_pointed_base = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    has_flat_base = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    temper = models.BooleanField(null = True, blank = True)
    decoration_plain = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    decoration_single_punctate = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    decoration_comb_punctate = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    decoration_fingerdrag = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    decoration_shell_punctate = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    decoration_dentate = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    decoration_single_incised = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    decoration_comb_incised = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    decoration_applique = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    decoration_exposed_coil = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    decoration_carved = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    decoration_paint = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    decoration_redslip = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    decoration_sculpt = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    decoration_paddle = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    decoration_lip = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    decoration_neck = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    decoration_whole = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    rim_direct = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    rim_direct_out =models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    rim_direct_in = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    rim_incurving = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    rim_outcurving = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    rim_everted = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    rim_inverted = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    lip_gradual_in = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    lip_gradual_out = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    lip_abrupt = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    lip_bulge_inside = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    lip_bulge_outside = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    lip_bulge_both = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    handle = models.CharField(max_length=7, choices=Frequency, default=Frequency.UNKNOWN)
    image = models.ManyToManyField(Image, related_name="vessels", blank=True)
    refs = models.ManyToManyField(Report, related_name="vessels", blank=True)
    feature = models.ManyToManyField(Feature, related_name="vessels", blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.region})"
    
    def get_absolute_url(self):
        return reverse(
            'vessels:vessel',
            args=[self.slug]
        )
    



class Site(models.Model):
    class Region(models.TextChoices):
        MARIANAS = 'MAR', 'Marianas'
        CAROLINES = 'CAR', 'Carolines'
        BISMARCK = 'BIS', 'Bismarck'
        PNG = 'PNG', 'PNG'
        SOLOMONS = 'SOL', 'Solomons'
        VANUATU = 'VAN', 'Vanuatu'
        MALUKU = 'MAL', 'Maluku'
        NEWCAL = 'NCA', 'New Caledonia'
        FIJI = 'FIJ', 'Fiji'
        SAMOA = 'SAM', 'Samoa'
        TONGA = 'TON', 'Tonga'
        MARQUESA = 'MAQ', 'Marquesa'
        NEMELANESIA = 'NME', 'NE Melanesia'
        COOK = 'COO', 'Cook'
        TUVALU = 'TUV', 'Tuvalu'
        UNKNOWN = 'U', 'unknown'
    slug = models.SlugField(default="", blank= True, null = False, db_index=True)
    name = models.CharField(max_length= 100)
    sitegroup = models.ManyToManyField(Sitegroup, related_name="sites", blank=True)
    details = models.TextField(max_length= 1000, null=True, blank=True)
    region = models.CharField(max_length=20, choices=Region, default=Region.UNKNOWN)
    lat = models.DecimalField(null=True, max_digits=9, decimal_places=6) 
    lng = models.DecimalField(null=True, max_digits=9, decimal_places=6)
    vessel = models.ManyToManyField(Vessel, related_name="site", blank=True)
    import_vessel = models.ManyToManyField(Vessel, related_name="isite", blank=True)
    geonames_id = models.IntegerField(null=True, blank=True)
    open_location_code = models.CharField(null=True, blank=True, max_length=100)
    production_site = models.BooleanField(default=False) 
   
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.region})"

    def thename(self):
        return f"{self.name}" 
    
    def get_absolute_url(self):
        return reverse(
            'vessels:site',
            args=[self.slug]
    )
    
    @property
    def vessel_string(self):
        fabs = self.vessel.all()
        fabstring = ' '
        if fabs:
            fabstring = fabstring + 'local:'

        for fab in fabs:
            fabstring = fabstring + " " + fab.name + ","
        ifabs = self.import_vessel.all()
        if ifabs:
            fabstring = fabstring + ' imports:'
        for ifab in ifabs:
            fabstring = fabstring + " " + ifab.name + ","
        return fabstring

    
