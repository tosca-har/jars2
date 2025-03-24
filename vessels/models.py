from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify



class Fabric(models.Model):
    slug = models.SlugField(default="", blank= True, null = False, db_index=True)
    name = models.CharField(max_length= 20, blank=True)
    fullname = models.CharField(max_length= 100, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.slug} ({self.fullname})"  

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
    legend = models.TextField(max_length= 1000, null=True, blank=True)
    
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
    vg_parent = models.ManyToManyField("self", symmetrical=False, null=True, blank=True)
    image = models.ManyToManyField(Image, related_name="vesselgroups", blank=True)
    fabric = models.ManyToManyField(Fabric, related_name="vesselgroups", blank=True)

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
    class Type(models.TextChoices):
        MORPHOLOGY = 'M', 'morphology'
        RIM = 'R', 'rim morphology'
        DECORATION = 'D', 'decoration'
        PLACE = 'P', 'decorated area'
        USE = 'U', 'use'

    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    name = models.CharField(default="", max_length=50)
    description = models.TextField(max_length= 1000, null=True, blank=True)
    refs = models.ManyToManyField(Report, related_name="feature", blank=True)
    image = models.ManyToManyField(Image, related_name="feature", blank=True)
    tag = models.CharField(default="", max_length=10, null=True, blank=True)
    type = models.CharField(max_length=20, choices=Type, default=Type.MORPHOLOGY)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.type})"





class Vessel(models.Model):

    class Gender(models.TextChoices):
        WOMEN = 'women', 'women'
        MEN = 'men', 'men'
        BOTH = 'both', 'both'
        UNKNOWN = 'unknown', 'unknown'


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
        PHILIPPINES = 'PHI', 'Philippines'
        TAIWAN = 'TAI', 'Taiwan'
        OTHER = 'OTH', 'Other'
        UNKNOWN = 'U', 'unknown'

    class Base(models.TextChoices):
        BALL = 'ball', 'ball'
        SPIRAL = 'spiral', 'spiral'
        SLAB = 'slab', 'slab'
        PINCHING = 'pinching', 'pinching'
        STRIP = 'strip', 'strip'
        OTHER = 'other', 'other'
        UNKNOWN = 'unknown', 'unknown'
    
    class Techniques(models.TextChoices):
        COIL = 'coil', 'coil' 
        SPIRAL = 'coil-spiral', 'coil-spiral'
        RING = 'coil-ring', 'coil-ring'
        SLAB = 'slab', 'slab'
        PINCHING = 'pinching', 'pinching'
        MOLDED = 'molded', 'molded' 
        HAMMERING = 'hammering', 'hammering'  
        WHEEL ='wheel', 'wheel'
        OTHER = 'other', 'other'
        UNKNOWN = 'unknown', 'unknown'
      
    class Techniques2(models.TextChoices):
        BEATING = 'beating', 'beating'
        PADDLE = 'paddle and anvil', 'paddle and anvil'
        SCRAPING = 'scraping', 'scraping'
        OTHER = 'other', 'other'
        UNKNOWN = 'unknown', 'unknown'
    
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    name = models.CharField(default="", max_length=50)
    vesselgroup = models.ManyToManyField(Vesselgroup, related_name="vessels", blank=True)
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
    temper = models.BooleanField(null = True, blank = True, default="") 
    image = models.ManyToManyField(Image, related_name="vessels", blank=True)
    refs = models.ManyToManyField(Report, related_name="vessels", blank=True)
    fabric = models.ManyToManyField(Fabric, related_name="vessels", blank=True)
    typical_feature = models.ManyToManyField(Feature, related_name="vessels_typical", blank=True)
    occasional_feature = models.ManyToManyField(Feature, related_name="vessels_common", blank=True)
    primary_technique = models.CharField(max_length=20, choices=Techniques, default=Techniques.UNKNOWN)
    secondary_technique = models.CharField(max_length=20, choices=Techniques2, default=Techniques2.UNKNOWN)
    base_technique = models.CharField(max_length=20, choices=Base, default=Base.UNKNOWN)
    rim_technique = models.CharField(max_length=20, choices=Techniques, default=Techniques.UNKNOWN)

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
        PHILIPPINES = 'PHI', 'Philippines'
        TAIWAN = 'TAI', 'Taiwan'
        OTHER = 'OTH', 'Other'
        UNKNOWN = 'U', 'unknown'
    slug = models.SlugField(default="", blank= True, null = False, db_index=True)
    name = models.CharField(max_length= 100)
    sitegroup = models.ManyToManyField(Sitegroup, related_name="sites", blank=True)
    details = models.TextField(max_length= 1000, null=True, blank=True)
    region = models.CharField(max_length=20, choices=Region, default=Region.UNKNOWN)
    lat = models.DecimalField(null=True, max_digits=9, decimal_places=6) 
    lng = models.DecimalField(null=True, max_digits=9, decimal_places=6)
    vessel = models.ManyToManyField(Vessel, related_name="site", blank=True)
    vesselgroup = models.ManyToManyField(Vesselgroup, related_name="site", blank=True)
    import_vessel = models.ManyToManyField(Vessel, related_name="isite", blank=True)
    import_vesselgroup = models.ManyToManyField(Vesselgroup, related_name="isite", blank=True)
    geonames_id = models.IntegerField(null=True, blank=True)
    open_location_code = models.CharField(null=True, blank=True, max_length=100)
    production_site = models.BooleanField(default=False)
    maptag = models.TextField(null=True, blank=True, max_length=500) 
   
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.maptag = ' '
        fabs = self.vessel.all()
        if fabs:
            self.maptag = self.maptag + 'local:'
            for fab in fabs:
                self.maptag = self.maptag + " " + fab.name + ","
        ifabs = self.import_vessel.all()
        if ifabs:
            self.maptag = self.maptag + ' imports:'
        for ifab in ifabs:
            self.maptag = self.maptag + " " + ifab.name + ","
        gfabs = self.vesselgroup.all()  
        if gfabs:
            self.maptag = self.maptag + ' groups:'
        for gfab in gfabs:
            self.maptag = self.maptag + " " + gfab.name + ","
        igfabs = self.import_vesselgroup.all()  
        if igfabs:
            self.maptag = self.maptag + ' groups imported:'
        for igfab in igfabs:
            self.maptag = self.maptag + " " + igfab.name + ","
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
            ifabs = self.import_vessel.all()
        gfabs = self.vesselgroup.all()  
        if gfabs:
            fabstring = fabstring + ' groups:'
        for gfab in gfabs:
            fabstring = fabstring + " " + gfab.name + ","
        igfabs = self.import_vesselgroup.all()  
        if igfabs:
            fabstring = fabstring + ' groups imported:'
        for igfab in igfabs:
            fabstring = fabstring + " " + igfab.name + ","
        return fabstring

    
