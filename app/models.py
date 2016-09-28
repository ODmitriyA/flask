import mongoengine as me


class Directory(me.Document):
    """Directory"""
    name = me.StringField(max_length=255)

    meta = {'allow_inheritance': True}
    
    def __str__(self):
        return self.name


class NomenclatureType(Directory):
    """Type of Nomenklature"""


class Nomenclature(Directory):
    """Nomenklature"""
    nomType = me.ReferenceField(NomenclatureType)
    comment = me.StringField()
