"""
Autogenerated APIS models.py module
based on ../sicprod-datamodel/model.xml
"""
# pylint: disable=line-too-long too-few-public-methods
# pylint: disable=import-error import-outside-toplevel unused-import
# pylint: disable=too-many-locals too-many-statements

import reversion
from django.contrib.contenttypes.models import ContentType
from django.db import models
from apis_core.apis_entities.models import TempEntityClass

from apis_ontology.mixins import MetadataMixin



@reversion.register(follow=["tempentityclass_ptr"])
class Person(MetadataMixin, TempEntityClass):
    """
    Person, eine Subklasse von crm:E21_Person.
    Generated from model xml
    """
    first_name = models.CharField(max_length=1024, blank=True, null=True, verbose_name = "Vorname", help_text = "Vorname der Person.")
    GENDER_CHOICES = (("männlich", "männlich"), ("weiblich", "weiblich"), ("unbekannt", "unbekannt"), )
    gender = models.CharField(max_length=9, choices=GENDER_CHOICES, blank=True, verbose_name = "Geschlecht", help_text = "Geschlecht der Person.")
    alternative_label = models.TextField(blank=True, null=True, verbose_name = "Alternativer Name", help_text = "Feld um alternative Namen anzugeben.")


@reversion.register(follow=["tempentityclass_ptr"])
class Function(MetadataMixin, TempEntityClass):
    """
    Eine Funktion kann von einer Person an einer Institution oder einem Hof ausgeübt werden kann.
    Generated from model xml
    """
    alternative_label = models.TextField(blank=True, null=True, verbose_name = "Alternativer Name", help_text = "Andere Namen für die Funktion.")


@reversion.register(follow=["tempentityclass_ptr"])
class Place(MetadataMixin, TempEntityClass):
    """
    Orte in SiCProD, Subklasse von crm:E53_Place.
    Generated from model xml
    """
    alternative_label = models.TextField(blank=True, null=True, verbose_name = "Alternativer Name", help_text = "Alternativer Name für einen Ort.")
    TYPE_CHOICES = (("Stadt", "Stadt"), ("Dorf/Nachbarschaft/Gemein/Siedlung/Weiler", "Dorf/Nachbarschaft/Gemein/Siedlung/Weiler"), ("Burg/Schloss", "Burg/Schloss"), ("Land/Herrschaftskomplex", "Land/Herrschaftskomplex"), ("Landschaft/Region", "Landschaft/Region"), ("Lehen", "Lehen"), ("Haus/Hof", "Haus/Hof"), ("Gericht", "Gericht"), ("Kloster", "Kloster"), ("Gewässer", "Gewässer"), ("Grundherrschaft", "Grundherrschaft"), ("Hofmark", "Hofmark"), ("Tal", "Tal"), ("Berg", "Berg"), ("Bergrevier", "Bergrevier"), ("Pflege", "Pflege"), ("(Land-)Vogtei", "(Land-)Vogtei"), ("Propstei", "Propstei"), )
    type = models.CharField(max_length=41, choices=TYPE_CHOICES, blank=True, verbose_name = "Typ", help_text = "Art des Ortes.")
    latitude = models.FloatField(null=True, blank=True, verbose_name = "Breitengrad", help_text = "Breitengrad des Ortes. Bei Polygonen wird die Mitte verwendet.")
    longitude = models.FloatField(null=True, blank=True, verbose_name = "Längengrad", help_text = "Längengrad des Ortes. Bei Polygonen wird die Mitte verwendet.")


@reversion.register(follow=["tempentityclass_ptr"])
class Institution(MetadataMixin, TempEntityClass):
    """
    SiCProD Institution, Subklasse von crm:E74_Group. Wird für alle Institutionen benutzt die kein Hof sind
    Generated from model xml
    """
    alternative_label = models.TextField(blank=True, null=True, verbose_name = "Alternativer Name", help_text = "Alternativer Name der Institution.")
    TYPE_CHOICES = (("Kanzlei", "Kanzlei"), ("Hofkapelle", "Hofkapelle"), ("Küche", "Küche"), ("(Dom-)Kapitel", "(Dom-)Kapitel"), ("Universität", "Universität"), ("Kloster", "Kloster"), ("Frauenzimmer", "Frauenzimmer"), ("Bistum", "Bistum"), ("Pfarrei", "Pfarrei"), )
    type = models.CharField(max_length=13, choices=TYPE_CHOICES, blank=True, verbose_name = "Typ", help_text = "Art der institution.")


@reversion.register(follow=["tempentityclass_ptr"])
class Court(MetadataMixin, TempEntityClass):
    """
    SiCProD Hof, Subklasse von crm:E74_Group. Wird für alle Institutionen benutzt die ein Hof sind
    Generated from model xml
    """
    alternative_label = models.TextField(blank=True, null=True, verbose_name = "Alternativer Name", help_text = "Alternativer Name des Hofes.")
    TYPE_CHOICES = (("Hof", "Hof"), ("Klosterhof", "Klosterhof"), ("Kaiserhof", "Kaiserhof"), ("Königshof", "Königshof"), ("Bischöflicher Hof", "Bischöflicher Hof"), ("Kurfürstlicher Hof", "Kurfürstlicher Hof"), ("Erzbischöflicher Hof", "Erzbischöflicher Hof"), ("Königlicher Hof", "Königlicher Hof"), ("Kaiserlicher Hof", "Kaiserlicher Hof"), ("Frauenzimmer", "Frauenzimmer"), )
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, blank=True, verbose_name = "Typ", help_text = "Art des Hofes")


@reversion.register(follow=["tempentityclass_ptr"])
class Event(MetadataMixin, TempEntityClass):
    """
    SiCProD Ereignis, Subklasse von crm:E5_Event.
    Generated from model xml
    """
    alternative_label = models.TextField(blank=True, null=True, verbose_name = "Alternativer Name", help_text = "Alternativer Name.")
    TYPE_CHOICES = (("Hochzeit", "Hochzeit"), ("Landtag", "Landtag"), ("Fest/Turnier", "Fest/Turnier"), ("Schlacht", "Schlacht"), ("Gesandtschaft/Reise", "Gesandtschaft/Reise"), ("Taufe", "Taufe"), ("Amtseinsetzung", "Amtseinsetzung"), ("Reichstag", "Reichstag"), )
    type = models.CharField(max_length=19, choices=TYPE_CHOICES, blank=True, verbose_name = "Typ", help_text = "Typ des Ereignisses.")


@reversion.register(follow=["tempentityclass_ptr"])
class Salary(MetadataMixin, TempEntityClass):
    """
    Ein Gehalt ist die Menge an Geld die eine Person als Gegenleistung erhalten hat. Das Gehalt muss keine wiederkehrende Zahlung sein.
    Generated from model xml
    """
    TYP_CHOICES = (("Sold", "Sold"), ("Zehrung", "Zehrung"), ("Provision", "Provision"), ("Kredit", "Kredit"), ("Sonstiges", "Sonstiges"), ("Burghut", "Burghut"), ("Botenlohn", "Botenlohn"), )
    typ = models.CharField(max_length=9, choices=TYP_CHOICES, blank=True, verbose_name = "Typ", help_text = "Art des Gehalts.")
    REPETITIONTYPE_CHOICES = (("einfach", "einfach"), ("wiederholend", "wiederholend"), )
    repetitionType = models.CharField(max_length=12, choices=REPETITIONTYPE_CHOICES, blank=True, verbose_name = "Typ Wiederholungen", help_text = "Typ des Gehalts.")



def construct_properties():
    """
    construct properties for all the models
    based on the relations defined in the xml
    """

    from apis_core.apis_relations.models import Property


    person_has_living_place = Property.objects.get_or_create(
        name="bewohnt",
        name_reverse="Bewohner von",
    )[0]
    person_has_living_place.subj_class.clear()
    person_has_living_place.subj_class.add(ContentType.objects.get(model=Person.__name__))
    person_has_living_place.obj_class.clear()
    person_has_living_place.obj_class.add(ContentType.objects.get(model=Place.__name__))

    person_owns_place = Property.objects.get_or_create(
        name="besitzt",
        name_reverse="Besitzer von",
    )[0]
    person_owns_place.subj_class.clear()
    person_owns_place.subj_class.add(ContentType.objects.get(model=Person.__name__))
    person_owns_place.obj_class.clear()
    person_owns_place.obj_class.add(ContentType.objects.get(model=Place.__name__))

    person_is_working_in_place = Property.objects.get_or_create(
        name="ist tätig in",
        name_reverse="ist Tätigkeitsort von",
    )[0]
    person_is_working_in_place.subj_class.clear()
    person_is_working_in_place.subj_class.add(ContentType.objects.get(model=Person.__name__))
    person_is_working_in_place.obj_class.clear()
    person_is_working_in_place.obj_class.add(ContentType.objects.get(model=Place.__name__))

    person_place_of_residence = Property.objects.get_or_create(
        name="hält sich auf in",
        name_reverse="ist Aufenthaltsort von",
    )[0]
    person_place_of_residence.subj_class.clear()
    person_place_of_residence.subj_class.add(ContentType.objects.get(model=Person.__name__))
    person_place_of_residence.obj_class.clear()
    person_place_of_residence.obj_class.add(ContentType.objects.get(model=Place.__name__))

    person_has_correspondance_with = Property.objects.get_or_create(
        name="hat Korrespondenz mit",
        name_reverse="hat Korrespondenz mit",
    )[0]
    person_has_correspondance_with.subj_class.clear()
    person_has_correspondance_with.subj_class.add(ContentType.objects.get(model=Person.__name__))
    person_has_correspondance_with.obj_class.clear()
    person_has_correspondance_with.obj_class.add(ContentType.objects.get(model=Person.__name__))

    person_has_family_relation_with = Property.objects.get_or_create(
        name="hat Familienbeziehung zu",
        name_reverse="hat Familienbeziehung zu",
    )[0]
    person_has_family_relation_with.subj_class.clear()
    person_has_family_relation_with.subj_class.add(ContentType.objects.get(model=Person.__name__))
    person_has_family_relation_with.obj_class.clear()
    person_has_family_relation_with.obj_class.add(ContentType.objects.get(model=Person.__name__))

    person_is_father_of = Property.objects.get_or_create(
        name="ist Elternteil von",
        name_reverse="ist Kind von",
    )[0]
    person_is_father_of.subj_class.clear()
    person_is_father_of.subj_class.add(ContentType.objects.get(model=Person.__name__))
    person_is_father_of.obj_class.clear()
    person_is_father_of.obj_class.add(ContentType.objects.get(model=Person.__name__))

    person_is_brother_of = Property.objects.get_or_create(
        name="ist Bruder/Schwester von",
        name_reverse="ist Bruder/Schwester von",
    )[0]
    person_is_brother_of.subj_class.clear()
    person_is_brother_of.subj_class.add(ContentType.objects.get(model=Person.__name__))
    person_is_brother_of.obj_class.clear()
    person_is_brother_of.obj_class.add(ContentType.objects.get(model=Person.__name__))

    person_is_son_of = Property.objects.get_or_create(
        name="ist Kind von",
        name_reverse="ist Elternteil von",
    )[0]
    person_is_son_of.subj_class.clear()
    person_is_son_of.subj_class.add(ContentType.objects.get(model=Person.__name__))
    person_is_son_of.obj_class.clear()
    person_is_son_of.obj_class.add(ContentType.objects.get(model=Person.__name__))

    person_has_marrige_with = Property.objects.get_or_create(
        name="hat Ehe mit",
        name_reverse="hat Ehe mit",
    )[0]
    person_has_marrige_with.subj_class.clear()
    person_has_marrige_with.subj_class.add(ContentType.objects.get(model=Person.__name__))
    person_has_marrige_with.obj_class.clear()
    person_has_marrige_with.obj_class.add(ContentType.objects.get(model=Person.__name__))

    person_was_present_at_court = Property.objects.get_or_create(
        name="war anwesend bei",
        name_reverse="hatte anwesende Person",
    )[0]
    person_was_present_at_court.subj_class.clear()
    person_was_present_at_court.subj_class.add(ContentType.objects.get(model=Person.__name__))
    person_was_present_at_court.obj_class.clear()
    person_was_present_at_court.obj_class.add(ContentType.objects.get(model=Court.__name__))

    person_recommended_person_for_court = Property.objects.get_or_create(
        name="empfahl",
        name_reverse="wurde empfohlen von",
    )[0]
    person_recommended_person_for_court.subj_class.clear()
    person_recommended_person_for_court.subj_class.add(ContentType.objects.get(model=Person.__name__))
    person_recommended_person_for_court.obj_class.clear()
    person_recommended_person_for_court.obj_class.add(ContentType.objects.get(model=Person.__name__))

    person_had_business_realtionship_with_person = Property.objects.get_or_create(
        name="hat Geschäftsbeziehung zu",
        name_reverse="hat Geschäftsbeziehung zu",
    )[0]
    person_had_business_realtionship_with_person.subj_class.clear()
    person_had_business_realtionship_with_person.subj_class.add(ContentType.objects.get(model=Person.__name__))
    person_had_business_realtionship_with_person.obj_class.clear()
    person_had_business_realtionship_with_person.obj_class.add(ContentType.objects.get(model=Person.__name__))

    person_is_custodian_of_person = Property.objects.get_or_create(
        name="ist Vormund von",
        name_reverse="ist Mündel von",
    )[0]
    person_is_custodian_of_person.subj_class.clear()
    person_is_custodian_of_person.subj_class.add(ContentType.objects.get(model=Person.__name__))
    person_is_custodian_of_person.obj_class.clear()
    person_is_custodian_of_person.obj_class.add(ContentType.objects.get(model=Person.__name__))

    person_was_member_of_institution = Property.objects.get_or_create(
        name="Mitglied von",
        name_reverse="hatte Mitglied",
    )[0]
    person_was_member_of_institution.subj_class.clear()
    person_was_member_of_institution.subj_class.add(ContentType.objects.get(model=Person.__name__))
    person_was_member_of_institution.obj_class.clear()
    person_was_member_of_institution.obj_class.add(ContentType.objects.get(model=Institution.__name__))

    person_was_active_in_institution = Property.objects.get_or_create(
        name="war tätig an",
        name_reverse="hatte tätige Person",
    )[0]
    person_was_active_in_institution.subj_class.clear()
    person_was_active_in_institution.subj_class.add(ContentType.objects.get(model=Person.__name__))
    person_was_active_in_institution.obj_class.clear()
    person_was_active_in_institution.obj_class.add(ContentType.objects.get(model=Institution.__name__))

    person_gets_pension_from_institution = Property.objects.get_or_create(
        name="ist Pfründner von",
        name_reverse="hat Pfründner",
    )[0]
    person_gets_pension_from_institution.subj_class.clear()
    person_gets_pension_from_institution.subj_class.add(ContentType.objects.get(model=Person.__name__))
    person_gets_pension_from_institution.obj_class.clear()
    person_gets_pension_from_institution.obj_class.add(ContentType.objects.get(model=Institution.__name__))

    person_took_part_in_event = Property.objects.get_or_create(
        name="nahm teil an",
        name_reverse="hatte teilnehmende Person",
    )[0]
    person_took_part_in_event.subj_class.clear()
    person_took_part_in_event.subj_class.add(ContentType.objects.get(model=Person.__name__))
    person_took_part_in_event.obj_class.clear()
    person_took_part_in_event.obj_class.add(ContentType.objects.get(model=Event.__name__))

    person_recieved_salary = Property.objects.get_or_create(
        name="erhielt Gehalt",
        name_reverse="wurde ausbezahlt an",
    )[0]
    person_recieved_salary.subj_class.clear()
    person_recieved_salary.subj_class.add(ContentType.objects.get(model=Salary.__name__))
    person_recieved_salary.obj_class.clear()
    person_recieved_salary.obj_class.add(ContentType.objects.get(model=Person.__name__))

    person_authorized_salary = Property.objects.get_or_create(
        name="weist an",
        name_reverse="auf Anweisung von",
    )[0]
    person_authorized_salary.subj_class.clear()
    person_authorized_salary.subj_class.add(ContentType.objects.get(model=Person.__name__))
    person_authorized_salary.obj_class.clear()
    person_authorized_salary.obj_class.add(ContentType.objects.get(model=Salary.__name__))

    person_born_in = Property.objects.get_or_create(
        name="geboren in",
        name_reverse="Geburtsort von",
    )[0]
    person_born_in.subj_class.clear()
    person_born_in.subj_class.add(ContentType.objects.get(model=Person.__name__))
    person_born_in.obj_class.clear()
    person_born_in.obj_class.add(ContentType.objects.get(model=Place.__name__))

    person_died_in = Property.objects.get_or_create(
        name="gestorben in",
        name_reverse="Sterbeort von",
    )[0]
    person_died_in.subj_class.clear()
    person_died_in.subj_class.add(ContentType.objects.get(model=Person.__name__))
    person_died_in.obj_class.clear()
    person_died_in.obj_class.add(ContentType.objects.get(model=Place.__name__))

    person_is_servant_of_person = Property.objects.get_or_create(
        name="ist im Dienst von",
        name_reverse="hat Diener",
    )[0]
    person_is_servant_of_person.subj_class.clear()
    person_is_servant_of_person.subj_class.add(ContentType.objects.get(model=Person.__name__))
    person_is_servant_of_person.obj_class.clear()
    person_is_servant_of_person.obj_class.add(ContentType.objects.get(model=Person.__name__))

    person_has_hometown = Property.objects.get_or_create(
        name="hat Heimatort in",
        name_reverse="Heimatort von",
    )[0]
    person_has_hometown.subj_class.clear()
    person_has_hometown.subj_class.add(ContentType.objects.get(model=Person.__name__))
    person_has_hometown.obj_class.clear()
    person_has_hometown.obj_class.add(ContentType.objects.get(model=Place.__name__))

    person_sells_property_to = Property.objects.get_or_create(
        name="verkauft Besitz an",
        name_reverse="kauft Besitz von",
    )[0]
    person_sells_property_to.subj_class.clear()
    person_sells_property_to.subj_class.add(ContentType.objects.get(model=Person.__name__))
    person_sells_property_to.obj_class.clear()
    person_sells_property_to.obj_class.add(ContentType.objects.get(model=Person.__name__))

    person_has_dispute_with = Property.objects.get_or_create(
        name="hat Streit mit",
        name_reverse="hat Streit mit",
    )[0]
    person_has_dispute_with.subj_class.clear()
    person_has_dispute_with.subj_class.add(ContentType.objects.get(model=Person.__name__))
    person_has_dispute_with.obj_class.clear()
    person_has_dispute_with.obj_class.add(ContentType.objects.get(model=Person.__name__))

    person_or_function_executes_salary = Property.objects.get_or_create(
        name="führt durch",
        name_reverse="wird durchgeführt von",
    )[0]
    person_or_function_executes_salary.subj_class.clear()
    person_or_function_executes_salary.subj_class.add(ContentType.objects.get(model=Person.__name__))
    person_or_function_executes_salary.subj_class.add(ContentType.objects.get(model=Function.__name__))
    person_or_function_executes_salary.obj_class.clear()
    person_or_function_executes_salary.obj_class.add(ContentType.objects.get(model=Salary.__name__))

    person_or_function_takes_salary = Property.objects.get_or_create(
        name="nimmt entgegen",
        name_reverse="wird entgegengenommen von",
    )[0]
    person_or_function_takes_salary.subj_class.clear()
    person_or_function_takes_salary.subj_class.add(ContentType.objects.get(model=Person.__name__))
    person_or_function_takes_salary.subj_class.add(ContentType.objects.get(model=Function.__name__))
    person_or_function_takes_salary.obj_class.clear()
    person_or_function_takes_salary.obj_class.add(ContentType.objects.get(model=Salary.__name__))

    person_vouchers_for_person = Property.objects.get_or_create(
        name="bürgt für",
        name_reverse="wird gebürgt von",
    )[0]
    person_vouchers_for_person.subj_class.clear()
    person_vouchers_for_person.subj_class.add(ContentType.objects.get(model=Person.__name__))
    person_vouchers_for_person.obj_class.clear()
    person_vouchers_for_person.obj_class.add(ContentType.objects.get(model=Person.__name__))

    person_possible_identical_with_person = Property.objects.get_or_create(
        name="ist möglicherweise identisch mit",
        name_reverse="ist möglicherweise identisch mit",
    )[0]
    person_possible_identical_with_person.subj_class.clear()
    person_possible_identical_with_person.subj_class.add(ContentType.objects.get(model=Person.__name__))
    person_possible_identical_with_person.obj_class.clear()
    person_possible_identical_with_person.obj_class.add(ContentType.objects.get(model=Person.__name__))

    function_is_located_at_institution = Property.objects.get_or_create(
        name="ist an",
        name_reverse="hat Funktion",
    )[0]
    function_is_located_at_institution.subj_class.clear()
    function_is_located_at_institution.subj_class.add(ContentType.objects.get(model=Function.__name__))
    function_is_located_at_institution.obj_class.clear()
    function_is_located_at_institution.obj_class.add(ContentType.objects.get(model=Institution.__name__))

    function_is_located_at_institution.obj_class.add(ContentType.objects.get(model=Court.__name__))

    function_is_hold_by = Property.objects.get_or_create(
        name="wird bekleidet von",
        name_reverse="hat Funktion inne",
    )[0]
    function_is_hold_by.subj_class.clear()
    function_is_hold_by.subj_class.add(ContentType.objects.get(model=Function.__name__))
    function_is_hold_by.obj_class.clear()
    function_is_hold_by.obj_class.add(ContentType.objects.get(model=Person.__name__))

    function_ging_hervor_aus = Property.objects.get_or_create(
        name="ging hervor aus",
        name_reverse="war Vorgänger von",
    )[0]
    function_ging_hervor_aus.subj_class.clear()
    function_ging_hervor_aus.subj_class.add(ContentType.objects.get(model=Function.__name__))
    function_ging_hervor_aus.obj_class.clear()
    function_ging_hervor_aus.obj_class.add(ContentType.objects.get(model=Function.__name__))

    function_is_subordinary_of = Property.objects.get_or_create(
        name="ist untergeordnet",
        name_reverse="hat untergeordnete Funktion",
    )[0]
    function_is_subordinary_of.subj_class.clear()
    function_is_subordinary_of.subj_class.add(ContentType.objects.get(model=Function.__name__))
    function_is_subordinary_of.obj_class.clear()
    function_is_subordinary_of.obj_class.add(ContentType.objects.get(model=Function.__name__))

    function_was_located_in = Property.objects.get_or_create(
        name="ausgeübt in",
        name_reverse="war Ausübungsort von",
    )[0]
    function_was_located_in.subj_class.clear()
    function_was_located_in.subj_class.add(ContentType.objects.get(model=Function.__name__))
    function_was_located_in.obj_class.clear()
    function_was_located_in.obj_class.add(ContentType.objects.get(model=Place.__name__))

    place_located_in_place = Property.objects.get_or_create(
        name="Teil von",
        name_reverse="hat Teil",
    )[0]
    place_located_in_place.subj_class.clear()
    place_located_in_place.subj_class.add(ContentType.objects.get(model=Place.__name__))
    place_located_in_place.obj_class.clear()
    place_located_in_place.obj_class.add(ContentType.objects.get(model=Place.__name__))

    institution_paid_salary = Property.objects.get_or_create(
        name="zahlte aus",
        name_reverse="wurde ausbezahlt von",
    )[0]
    institution_paid_salary.subj_class.clear()
    institution_paid_salary.subj_class.add(ContentType.objects.get(model=Institution.__name__))
    institution_paid_salary.obj_class.clear()
    institution_paid_salary.obj_class.add(ContentType.objects.get(model=Salary.__name__))

    institutionlocated_in = Property.objects.get_or_create(
        name="ist gelegen in",
        name_reverse="inkludiert",
    )[0]
    institutionlocated_in.subj_class.clear()
    institutionlocated_in.subj_class.add(ContentType.objects.get(model=Institution.__name__))
    institutionlocated_in.obj_class.clear()
    institutionlocated_in.obj_class.add(ContentType.objects.get(model=Place.__name__))

    institution_given_in_mortage_to = Property.objects.get_or_create(
        name="ist verpfändet an",
        name_reverse="hat als Pfand",
    )[0]
    institution_given_in_mortage_to.subj_class.clear()
    institution_given_in_mortage_to.subj_class.add(ContentType.objects.get(model=Institution.__name__))
    institution_given_in_mortage_to.obj_class.clear()
    institution_given_in_mortage_to.obj_class.add(ContentType.objects.get(model=Person.__name__))

    institution_belongs_to_institution = Property.objects.get_or_create(
        name="gehört zu",
        name_reverse="zuständig für",
    )[0]
    institution_belongs_to_institution.subj_class.clear()
    institution_belongs_to_institution.subj_class.add(ContentType.objects.get(model=Institution.__name__))
    institution_belongs_to_institution.obj_class.clear()
    institution_belongs_to_institution.obj_class.add(ContentType.objects.get(model=Institution.__name__))

    institution_orders_salary = Property.objects.get_or_create(
        name="weist an",
        name_reverse="angewiesen von",
    )[0]
    institution_orders_salary.subj_class.clear()
    institution_orders_salary.subj_class.add(ContentType.objects.get(model=Institution.__name__))
    institution_orders_salary.obj_class.clear()
    institution_orders_salary.obj_class.add(ContentType.objects.get(model=Salary.__name__))

    institution_has_tie_to_institution = Property.objects.get_or_create(
        name="steht in Verbindung mit",
        name_reverse="steht in Verbindung mit",
    )[0]
    institution_has_tie_to_institution.subj_class.clear()
    institution_has_tie_to_institution.subj_class.add(ContentType.objects.get(model=Institution.__name__))
    institution_has_tie_to_institution.obj_class.clear()
    institution_has_tie_to_institution.obj_class.add(ContentType.objects.get(model=Institution.__name__))

    event_took_place_at = Property.objects.get_or_create(
        name="fand statt in",
        name_reverse="inkludierte",
    )[0]
    event_took_place_at.subj_class.clear()
    event_took_place_at.subj_class.add(ContentType.objects.get(model=Event.__name__))
    event_took_place_at.obj_class.clear()
    event_took_place_at.obj_class.add(ContentType.objects.get(model=Place.__name__))

    salary_paid_to = Property.objects.get_or_create(
        name="wurde ausbezahlt an",
        name_reverse="erhielt",
    )[0]
    salary_paid_to.subj_class.clear()
    salary_paid_to.subj_class.add(ContentType.objects.get(model=Salary.__name__))
    salary_paid_to.obj_class.clear()
    salary_paid_to.obj_class.add(ContentType.objects.get(model=Function.__name__))

    salary_ordered_by = Property.objects.get_or_create(
        name="auf Anweisung von",
        name_reverse="wies an",
    )[0]
    salary_ordered_by.subj_class.clear()
    salary_ordered_by.subj_class.add(ContentType.objects.get(model=Salary.__name__))
    salary_ordered_by.obj_class.clear()
    salary_ordered_by.obj_class.add(ContentType.objects.get(model=Function.__name__))
