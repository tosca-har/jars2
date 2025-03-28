from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from decouple import config
from .models import Vessel, Vesselgroup, Site, Sitegroup, Report, Image
from .forms import SearchForm

mbsu = config('MBSU')
thsu = config('THSU')

def home(request):
    return render(request, "vessels/home.html")

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST) 
        vessels = Vessel.objects.all() 
        query = "Matching vessels for "    
        if form.is_valid():
            valStart = form.cleaned_data.get("starttime")
            valEnd = form.cleaned_data.get("endtime")
            if valStart:
                query = query + "from " + str(valStart) + "BP"
                vessels = vessels.filter(time_end__lte=valStart)
            if valEnd == 0:
                query = query + " to " + str(valEnd) + "BP"
                vessels = vessels.filter(time_start__gte=valEnd)
            elif valEnd:
                query = query + " to " + str(valEnd) + "BP"
                vessels = vessels.filter(time_start__gte=valEnd)
            valB = form.cleaned_data.get("base_build")
            if valB != 'unknown':
                query = query + "; base is " +valB
                vessels = vessels.filter(base_technique=valB)
            valP = form.cleaned_data.get("primary_build")
            if valP != 'unknown':
                query = query + "; primary is " +valP
                if valP == 'coil':
                    vessels = vessels.filter(primary_technique=valP) | vessels.filter(primary_technique='coil-spiral') | vessels.filter(primary_technique='coil-ring')
                else:
                    vessels = vessels.filter(primary_technique=valP)
            valR = form.cleaned_data.get("rim_build")
            if valR != 'unknown':
                query = query + "; rim build is " +valR
                if valR == 'coil':
                    vessels = vessels.filter(rim_technique=valR) | vessels.filter(rim_technique='coil-spiral') | vessels.filter(rim_technique='coil-ring')
                else:
                    vessels = vessels.filter(rim_technique=valR)          
            valS = form.cleaned_data.get("secondary_build")
            if valS != 'unknown':
                query = query + "; secondary build is " +valS
                vessels = vessels.filter(secondary_technique=valS)
            valT = form.cleaned_data.get("tempered")    
            if valT != '':
                query = query + "; manually tempered-" + str(valT)
                vessels = vessels.filter(temper=valT)
            valGP = form.cleaned_data.get("gender_make")    
            if valGP != 'unknown':
                query = query + "; maker gender is  " +valGP
                vessels = vessels.filter(gender_make=valGP)
            valGD = form.cleaned_data.get("gender_dec") 
            if valGD != 'unknown':
                query = query + "; decorater gender is  " +valGD
                vessels = vessels.filter(gender_decorate=valGD)
            valF = form.cleaned_data.get("baking")
            if valF:
                 vessels = vessels.filter(use_baking__gt=0 )
                 query = query + "; baking"
            valF = form.cleaned_data.get("boiling") 
            if valF:
                 vessels = vessels.filter(use_boiling__gt=0 )
                 query = query + "; boiling" 
            valF = form.cleaned_data.get("burial")
            if valF:
                 vessels = vessels.filter(use_burial__gt=0 )
                 query = query + "; burial"
            valF = form.cleaned_data.get("ceremonial")
            if valF:
                 vessels = vessels.filter(use_ceremonial__gt=0 )
                 query = query + "; ceremonial"
            valF = form.cleaned_data.get("cooking")
            if valF:
                 vessels = vessels.filter(use_cooking__gt=0 )
                 query = query + "; cooking" 
            valF = form.cleaned_data.get("eating")
            if valF:
                 vessels = vessels.filter(use_eating__gt=0 )
                 query = query + "; eating" 
            valF = form.cleaned_data.get("frying")
            if valF:
                 vessels = vessels.filter(use_frying__gt=0 )
                 query = query + "; frying"
            valF = form.cleaned_data.get("hearth")
            if valF:
                 vessels = vessels.filter(use_hearth__gt=0 )
                 query = query + "; hearth"
            valF = form.cleaned_data.get("lid")
            if valF:
                 vessels = vessels.filter(use_lid__gt=0 )
                 query = query + "; lid" 
            valF = form.cleaned_data.get("light")
            if valF:
                 vessels = vessels.filter(use_light__gt=0 )
                 query = query + "; light" 
            valF = form.cleaned_data.get("musical_instrument")
            if valF:
                 vessels = vessels.filter(use_musical_instrument__gt=0 )
                 query = query + "; musical instrument"
            valF = form.cleaned_data.get("serving")
            if valF:
                 vessels = vessels.filter(use_serving__gt=0 )
                 query = query + "; serving" 
            valF = form.cleaned_data.get("smoking")
            if valF:
                 vessels = vessels.filter(use_smoking__gt=0 )
                 query = query + "; smoking"
            valF = form.cleaned_data.get("storage")
            if valF:
                 vessels = vessels.filter(use_storage__gt=0 )
                 query = query + "; storage" 
            valF = form.cleaned_data.get("transfer")
            if valF:
                 vessels = vessels.filter(use_transfer__gt=0 )
                 query = query + "; transfer"           
            valF = form.cleaned_data.get("spout")
            if valF:
                 vessels = vessels.filter(morph_spout__gt=0 )
                 query = query + "; spout"
            valF = form.cleaned_data.get("multimouth")
            if valF:
                 vessels = vessels.filter(morph_multimouth__gt=0 )
                 query = query + "; multi-mouth"
            valF = form.cleaned_data.get("neck")
            if valF:
                 vessels = vessels.filter(morph_neck__gt=0 )
                 query = query + "; has neck"
            valF = form.cleaned_data.get("collar")
            if valF:
                 vessels = vessels.filter(morph_collar__gt=0 )
                 query = query + "; has collar"
            valF = form.cleaned_data.get("carination")
            if valF:
                 vessels = vessels.filter(morph_carination__gt=0 )
                 query = query + "; has carination"
            valF = form.cleaned_data.get("handle")
            if valF:
                 vessels = vessels.filter(morph_handle__gt=0 )
                 query = query + "; has handle"
            valF = form.cleaned_data.get("feet")
            if valF:
                 vessels = vessels.filter(morph_feet__gt=0 )
                 query = query + "; has feet"
            valF = form.cleaned_data.get("ringfoot")
            if valF:
                 vessels = vessels.filter(morph_ringfoot__gt=0 )
                 query = query + "; has ringfoot"
            valF = form.cleaned_data.get("restricted")
            if valF:
                 vessels = vessels.filter(morph_restricted__gt=0 )
                 query = query + "; restricted"
            valF = form.cleaned_data.get("unrestricted")
            if valF:
                 vessels = vessels.filter(morph_unrestricted__gt=0 )
                 query = query + "; unrestricted"
            valF = form.cleaned_data.get("jar")
            if valF:
                 vessels = vessels.filter(morph_jar__gt=0 )
                 query = query + "; jar"
            valF = form.cleaned_data.get("bowl")
            if valF:
                 vessels = vessels.filter(morph_bowl__gt=0 )
                 query = query + "; bowl"
            valF = form.cleaned_data.get("dish")
            if valF:
                 vessels = vessels.filter(morph_dish__gt=0 )
                 query = query + "; dish"
            valF = form.cleaned_data.get("plate")
            if valF:
                 vessels = vessels.filter(morph_plate__gt=0 )
                 query = query + "; plate"
            valF = form.cleaned_data.get("cup")
            if valF:
                 vessels = vessels.filter(morph_cup__gt=0 )
                 query = query + "; cup"
            valF = form.cleaned_data.get("jug")
            if valF:
                 vessels = vessels.filter(morph_jug__gt=0 )
                 query = query + "; jug"
            valF = form.cleaned_data.get("forno")
            if valF:
                 vessels = vessels.filter(morph_forno__gt=0 )
                 query = query + "; forno"
            valF = form.cleaned_data.get("lamp")
            if valF:
                 vessels = vessels.filter(morph_lamp__gt=0 )
                 query = query + "; lamp"
            valF = form.cleaned_data.get("nipplebase")
            if valF:
                 vessels = vessels.filter(morph_nipplebase__gt=0 )
                 query = query + "; has nipple base"
            valF = form.cleaned_data.get("pointedbase")
            if valF:
                 vessels = vessels.filter(morph_pointedbase__gt=0 )
                 query = query + "; has pointed base"
            valF = form.cleaned_data.get("roundedbase")
            if valF:
                 vessels = vessels.filter(morph_roundedbase__gt=0 )
                 query = query + "; has rounded base"
            valF = form.cleaned_data.get("flatbase")
            if valF:
                 vessels = vessels.filter(morph_flatbase__gt=0 )
                 query = query + "; has flat base"
            valF = form.cleaned_data.get("rim_outc")
            if valF:
                 vessels = vessels.filter(rim_outcurving__gt=0 )
                 query = query + "; outcurving rim"
            valF = form.cleaned_data.get("rim_eve")
            if valF:
                 vessels = vessels.filter(rim_everted__gt=0 )
                 query = query + "; everted rim"           
            valF = form.cleaned_data.get("rim_dir_out")
            if valF:
                 vessels = vessels.filter(rim_direct_out__gt=0 )
                 query = query + "; direct outward rim"       
            valF = form.cleaned_data.get("rim_dir")
            if valF:
                 vessels = vessels.filter(rim_direct__gt=0 )
                 query = query + "; direct rim"            
            valF = form.cleaned_data.get("rim_dir_in")
            if valF:
                 vessels = vessels.filter(rim_direct_in__gt=0 )
                 query = query + "; direct inward rim"        
            valF = form.cleaned_data.get("rim_invert")
            if valF:
                 vessels = vessels.filter(rim_inverted__gt=0 )
                 query = query + "; inverted rim"         
            valF = form.cleaned_data.get("rim_incur")
            if valF:
                 vessels = vessels.filter(rim_incurving__gt=0 )
                 query = query + "; incurving rim"            
            valF = form.cleaned_data.get("rim_para")
            if valF:
                 vessels = vessels.filter(rim_parallel__gt=0 )
                 query = query + "; parallel rim"            
            valF = form.cleaned_data.get("rim_abr_nar")
            if valF:
                 vessels = vessels.filter(rim_abrupt_narrow__gt=0 )
                 query = query + "; abrupt narrowing rim"          
            valF = form.cleaned_data.get("rim_abr_wide")
            if valF:
                 vessels = vessels.filter(rim_abrupt_wide__gt=0 )
                 query = query + "; abrupt widening rim"          
            valF = form.cleaned_data.get("rim_grad_nar")
            if valF:
                 vessels = vessels.filter(rim_gradually_narrow__gt=0 )
                 query = query + "; gradually narrowing rim"         
            valF = form.cleaned_data.get("rim_grad_thick_ex")
            if valF:
                 vessels = vessels.filter(rim_gradually_thickened_exterior__gt=0 )
                 query = query + "; gradually thickened exterior rim"     
            valF = form.cleaned_data.get("rim_grad_thick_int")
            if valF:
                 vessels = vessels.filter(rim_gradually_thickened_interior__gt=0 )
                 query = query + "; gradually thickened interior rim"          
            valF = form.cleaned_data.get("rim_round_both")
            if valF:
                 vessels = vessels.filter(rim_rounded_both__gt=0 )
                 query = query + "; rounded both sides rim"        
            valF = form.cleaned_data.get("rim_thick_ex")
            if valF:
                 vessels = vessels.filter(rim_thickened_exterior__gt=0 )
                 query = query + "; round thickened exterior rim"        
            valF = form.cleaned_data.get("rim_thick_int")
            if valF:
                 vessels = vessels.filter(rim_thickened_interior__gt=0 )
                 query = query + "; round thickened interior rim"
            valF = form.cleaned_data.get("dec_lip")
            if valF:
                 vessels = vessels.filter(dec_lip__gt=0 )
                 query = query + "; decorated lip"
            valF = form.cleaned_data.get("dec_rim")
            if valF:
                 vessels = vessels.filter(dec_rim__gt=0 )
                 query = query + "; decorated rim"
            valF = form.cleaned_data.get("dec_internal_rim")
            if valF:
                 vessels = vessels.filter(dec_internal_rim__gt=0 )
                 query = query + "; decorated internal rim"
            valF = form.cleaned_data.get("dec_neck")
            if valF:
                 vessels = vessels.filter(dec_neck__gt=0 )
                 query = query + "; decorated neck"
            valF = form.cleaned_data.get("dec_shoulders")
            if valF:
                 vessels = vessels.filter(dec_shoulders__gt=0 )
                 query = query + "; decorated shoulders"
            valF = form.cleaned_data.get("dec_body")
            if valF:
                 vessels = vessels.filter(dec_body__gt=0 )
                 query = query + "; decorated body"
            valF = form.cleaned_data.get("plain")
            if valF:
                 vessels = vessels.filter(dec_plain__gt=0 )
                 query = query + "; plain decoration"
            valF = form.cleaned_data.get("exposed_coil")
            if valF:
                 vessels = vessels.filter(dec_exposed_coil__gt=0 )
                 query = query + "; exposed coil decoration"
            valF = form.cleaned_data.get("finger_marks")
            if valF:
                 vessels = vessels.filter(dec_finger_marks__gt=0 )
                 query = query + "; finger mark decoration"
            valF = form.cleaned_data.get("impressing")
            if valF:
                 vessels = vessels.filter(dec_impressing__gt=0 )
                 query = query + "; impressing decoration"
            valF = form.cleaned_data.get("punctation")
            if valF:
                 vessels = vessels.filter(dec_punctation__gt=0 )
                 query = query + "; punctation decoration"                                 
            valF = form.cleaned_data.get("comb_impression")
            if valF:
                 vessels = vessels.filter(dec_comb_impression__gt=0 )
                 query = query + "; comb impression decoration"
            valF = form.cleaned_data.get("dentate")
            if valF:
                 vessels = vessels.filter(dec_dentate__gt=0 )
                 query = query + "; dentate decoration"
            valF = form.cleaned_data.get("paddle_impressing")
            if valF:
                 vessels = vessels.filter(dec_paddle_impressing__gt=0 )
                 query = query + "; paddle impression decoration"
            valF = form.cleaned_data.get("cord_impressing")
            if valF:
                 vessels = vessels.filter(dec_cord_impressing__gt=0 )
                 query = query + "; cord impression decoration"                                 
            valF = form.cleaned_data.get("incising")
            if valF:
                 vessels = vessels.filter(dec_incising__gt=0 )
                 query = query + "; incision decoration"
            valF = form.cleaned_data.get("simple_incising")
            if valF:
                 vessels = vessels.filter(dec_simple_incising__gt=0 )
                 query = query + "; simple incision decoration"
            valF = form.cleaned_data.get("comb_incising")
            if valF:
                 vessels = vessels.filter(dec_comb_incising__gt=0 )
                 query = query + "; comb incision decoration"
            valF = form.cleaned_data.get("grooving")
            if valF:
                 vessels = vessels.filter(dec_grooving__gt=0 )
                 query = query + "; groove decoration"                                 
            valF = form.cleaned_data.get("scouring")
            if valF:
                 vessels = vessels.filter(dec_scouring__gt=0 )
                 query = query + "; scouring decoration"  
            valF = form.cleaned_data.get("carving")
            if valF:
                 vessels = vessels.filter(dec_carving__gt=0 )
                 query = query + "; carving decoration"  
            valF = form.cleaned_data.get("perforating")
            if valF:
                 vessels = vessels.filter(dec_perforating__gt=0 )
                 query = query + "; perforation decoration"  
            valF = form.cleaned_data.get("applique")
            if valF:
                 vessels = vessels.filter(dec_applique__gt=0 )
                 query = query + "; applique decoration"  
            valF = form.cleaned_data.get("nubbins_lugs")
            if valF:
                 vessels = vessels.filter(dec_nubbins_lugs__gt=0 )
                 query = query + "; nubbin and lug decoration"  
            valF = form.cleaned_data.get("bands")
            if valF:
                 vessels = vessels.filter(dec_bands__gt=0 )
                 query = query + "; band decoration"  
            valF = form.cleaned_data.get("sculpting")
            if valF:
                 vessels = vessels.filter(dec_sculpting__gt=0 )
                 query = query + "; sculptural decoration"  
            valF = form.cleaned_data.get("red_slip")
            if valF:
                 vessels = vessels.filter(dec_red_slip__gt=0 )
                 query = query + "; red slip decoration"  
            valF = form.cleaned_data.get("glaze")
            if valF:
                 vessels = vessels.filter(dec_glaze__gt=0 )
                 query = query + "; glaze decoration"  
            valF = form.cleaned_data.get("painting")
            if valF:
                 vessels = vessels.filter(dec_painting__gt=0 )
                 query = query + "; paint decoration"  

            val = form.cleaned_data.get("regions_to_include") 
            vessels = vessels.filter(region__in=val)
            query = query + "." 
            query2 = "Regions searched: " + ', '.join(val) + '.'
            query = query + query2
            vessels = vessels.distinct()
            sites = Site.objects.all()
     
            if len(vessels) > 0:
                return render(request, "vessels/search-results.html", {
                    "vessels": vessels,
                    "query": query,
                    "prod_sites": sites.filter(vessel__in = vessels).distinct(),
                    "imp_sites": sites.filter(import_vessel__in = vessels).distinct() ,
                    "mbsu": mbsu,
                    "thsu":thsu
                })
            else: return HttpResponseRedirect("no-match")
        else: return HttpResponseRedirect("no-match")       
    else:   
        form = SearchForm()
    return render(request, "vessels/search.html", {
        "form": form
    })

def compare(request):
    vesselgroups = Vesselgroup.objects.all().order_by("name")
    return render(request, "vessels/compare.html", {
        "groups": vesselgroups
    })
def map(request):
    sites = Site.objects.all().order_by("name")
    return render(request, "vessels/map.html", {
        "sites": sites,
        "mbsu": mbsu,
        "thsu":thsu
    })

def vesselgr(request, slug):
    identified_vg = get_object_or_404(Vesselgroup, slug=slug)
    vessels = identified_vg.vessels.all()
    return render(request, "vessels/vesselgr.html", {
        "groups": identified_vg,
        "vg_vessels": vessels,
        "vg_parents": identified_vg.vg_parent.all(),
        "images": Image.objects.all().filter(vessels__in=vessels).distinct(),
        "prod_sites": identified_vg.site.all(),
        "imp_sites": identified_vg.isite.all(),
        "vg_fabrics": identified_vg.fabric.all(),
        "v_ref": identified_vg.refs.all(),
        "mbsu": mbsu,
        "thsu":thsu
    })

def sitegr(request, slug):
    identified_vg = get_object_or_404(Sitegroup, slug=slug)
    id_sites = identified_vg.sites.all()
    return render(request, "vessels/sitegr.html", {
        "groups": identified_vg,
        "sites": id_sites
    })

def site(request, slug):
    identified_v = get_object_or_404(Site, slug=slug)
    return render(request, "vessels/site.html", {
        "site": identified_v,
        "vessels": identified_v.vessel.all(),
        "ivessels": identified_v.import_vessel.all(),
        "vesselgr": identified_v.vesselgroup.all(),
        "ivesselgr": identified_v.import_vesselgroup.all()
    })


def vessel(request, slug):
    identified_v = get_object_or_404(Vessel, slug=slug)
    return render(request, "vessels/vessel.html", {
        "the_vessel": identified_v,
        "fabrics": identified_v.fabric.all(),
        "vessel_images": identified_v.image.all(),
        "v_ref": identified_v.refs.all(),
        "vgr": identified_v.vesselgroup.all(),
        "typ_features": identified_v.typical_feature.all(),
        "com_features": identified_v.occasional_feature.all(),
        "prod_sites": identified_v.site.all(),
        "imp_sites": identified_v.isite.all(),
        "mbsu": mbsu,
        "thsu":thsu
    })
def report(request, slug):
    identified_r = get_object_or_404(Report, slug=slug)
    return render(request, "vessels/report.html", {
        "report": identified_r,
    })
def glossary(request):
    return render(request, "vessels/glossary.html")
def no_match(request):
    return render(request, "vessels/no-match.html")