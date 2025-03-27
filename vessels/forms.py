from django import forms
from .models import Feature



temper_choices = (
    (None, "unknown"),
    (True, "manual"),
    (False, "not added"),
) 

techniques = (
    ('unknown', 'all'),
    ('coil', 'coil'), 
    ('coil-spiral', 'coil-spiral'),
    ('coil-ring', 'coil-ring'),
    ('slab', 'slab'),
    ('pinching', 'pinching'),
    ('moulded', 'moulded'),
    ('hammering', 'hammering'),  
    ('wheel', 'wheel'),
    ('other', 'other'),
)

techniquesb = (
    ('unknown', 'all'),
    ('ball', 'ball'), 
    ('spiral', 'spiral'),
    ('slab', 'slab'),
    ('other', 'other'),
)

techniquess = (
    ('unknown', 'all'),
    ('beating', 'beating'), 
    ('paddle and anvil', 'paddle and anvil'),
    ('scraping', 'scraping'),
    ('other', 'other'),
)

gender = (
    ('unknown', 'unknown'),
    ('both', 'women and men'), 
    ('women', 'women'),
    ('men', 'men'),
)



def feature_choices():
    features =  Feature.objects.all().order_by("name")
    flist =  tuple()
    for f in features:
        flist += (
        (f.name, f),   
        ) 
    return flist

def feature_choicesM():
    features =  Feature.objects.all().filter(type='M').order_by("name")
    flist =  tuple()
    for f in features:
        flist += (
        (f.name, f),   
        ) 
    return flist

def feature_choicesR():
    features =  Feature.objects.all().filter(type='R').order_by("name")
    flist =  tuple()
    for f in features:
        flist += (
        (f.name, f),   
        ) 
    return flist

def feature_choicesD():
    features =  Feature.objects.all().filter(type='D').order_by("name")
    flist =  tuple()
    for f in features:
        flist += (
        (f.name, f),   
        ) 
    return flist

def feature_choicesP():
    features =  Feature.objects.all().filter(type='P').order_by("name")
    flist =  tuple()
    for f in features:
        flist += (
        (f.name, f),   
        ) 
    return flist

def feature_choicesU():
    features =  Feature.objects.all().filter(type='U').order_by("name")
    flist =  tuple()
    for f in features:
        flist += (
        (f.name, f),   
        ) 
    return flist

class SearchForm(forms.Form):
    base_build = forms.ChoiceField(choices= techniquesb, required = False)
    primary_build = forms.ChoiceField(choices= techniques, required = False)
    rim_build = forms.ChoiceField(choices= techniques, required = False)
    secondary_build = forms.ChoiceField(choices= techniquess, required = False)
    tempered = forms.ChoiceField(choices= temper_choices, required = False)
    gender_make = forms.ChoiceField(choices= gender, required = False)
    gender_dec = forms.ChoiceField(choices= gender, required = False)
    baking = forms.BooleanField(required = False)
    boiling = forms.BooleanField(required = False)
    cooking = forms.BooleanField(required = False)
    burial = forms.BooleanField(required = False)
    ceremonial = forms.BooleanField(required = False)
    eating = forms.BooleanField(required = False)
    frying = forms.BooleanField(required = False)
    hearth = forms.BooleanField(required = False)
    lid = forms.BooleanField(required = False)
    light = forms.BooleanField(required = False)
    musical_instrument = forms.BooleanField(required = False)
    serving = forms.BooleanField(required = False)
    smoking = forms.BooleanField(required = False)
    storage = forms.BooleanField(required = False)
    transfer = forms.BooleanField(required = False)
    bowl = forms.BooleanField(required = False)
    carination = forms.BooleanField(required = False)
    cup = forms.BooleanField(required = False)
    dish = forms.BooleanField(required = False)
    feet = forms.BooleanField(required = False)
    flatbase = forms.BooleanField(required = False)
    forno = forms.BooleanField(required = False)
    handle = forms.BooleanField(required = False)
    collar = forms.BooleanField(required = False)
    neck = forms.BooleanField(required = False)
    jar = forms.BooleanField(required = False)
    jug = forms.BooleanField(required = False)
    lamp = forms.BooleanField(required = False)
    multimouth = forms.BooleanField(required = False)
    nipplebase = forms.BooleanField(required = False)
    plate = forms.BooleanField(required = False)
    pointedbase = forms.BooleanField(required = False)
    restricted = forms.BooleanField(required = False)
    ringfoot = forms.BooleanField(required = False)
    roundedbase = forms.BooleanField(required = False)
    spout = forms.BooleanField(required = False)
    unrestricted = forms.BooleanField(required = False)
    rim_abr_nar = forms.BooleanField(required = False)
    rim_abr_wide = forms.BooleanField(required = False)
    rim_dir_in = forms.BooleanField(required = False)
    rim_dir_out = forms.BooleanField(required = False)
    rim_dir = forms.BooleanField(required = False)
    rim_eve = forms.BooleanField(required = False)
    rim_grad_nar = forms.BooleanField(required = False)
    rim_grad_thick_ex = forms.BooleanField(required = False)
    rim_grad_thick_int = forms.BooleanField(required = False)
    rim_incur = forms.BooleanField(required = False)
    rim_invert = forms.BooleanField(required = False)
    rim_outc = forms.BooleanField(required = False)
    rim_para = forms.BooleanField(required = False)
    rim_round_both = forms.BooleanField(required = False)
    rim_thick_ex = forms.BooleanField(required = False)
    rim_thick_int = forms.BooleanField(required = False)
    dec_lip = forms.BooleanField(required = False)
    dec_rim = forms.BooleanField(required = False)
    dec_internal_rim = forms.BooleanField(required = False)
    dec_neck = forms.BooleanField(required = False)
    dec_shoulders = forms.BooleanField(required = False)
    dec_body = forms.BooleanField(required = False)
    plain = forms.BooleanField(required = False)
    exposed_coil = forms.BooleanField(required = False)
    finger_marks = forms.BooleanField(required = False)
    impressing = forms.BooleanField(required = False)
    punctation = forms.BooleanField(required = False)
    comb_impression = forms.BooleanField(required = False)
    dentate = forms.BooleanField(required = False)
    paddle_impressing = forms.BooleanField(required = False)
    cord_impressing = forms.BooleanField(required = False)
    incising = forms.BooleanField(required = False)
    simple_incising = forms.BooleanField(required = False)
    comb_incising = forms.BooleanField(required = False)
    grooving = forms.BooleanField(required = False)
    scouring = forms.BooleanField(required = False)
    carving = forms.BooleanField(required = False)
    perforating = forms.BooleanField(required = False)
    applique = forms.BooleanField(required = False)
    nubbins_lugs = forms.BooleanField(required = False)
    bands = forms.BooleanField(required = False)
    sculpting = forms.BooleanField(required = False)
    red_slip = forms.BooleanField(required = False)
    glaze = forms.BooleanField(required = False)
    painting = forms.BooleanField(required = False)
    starttime = forms.IntegerField(required = False, initial=5000, min_value = 0, max_value = 6000)
    endtime = forms.IntegerField(required = False, initial = 0, min_value = 0, max_value = 6000)

