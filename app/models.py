class Directory:
    """Справочник"""
    def __init__(self, code, name):
        self.code = code
        self.name = name

    def __str__(self):
        return '{0} - {1}'.format(str(self.code), self.name)


class NomenclatureType(Directory):
    """Справочник - Вид номенклатуры"""
    def __init__(self, code, name):
        Directory.__init__(self, code, name)

    def __str__(self):
        return '{0}: {1}'.format(self.__doc__, Directory.__str__(self))


class Nomenclature(Directory):
    """Справочник - Номенклатура"""
    def __init__(self, code, name, nomtype):
        Directory.__init__(self, code, name)
        self.nomType = nomtype

    def __str__(self):
        return '{0}: {1}, ({2})'.format(
            self.__doc__,
            Directory.__str__(self),
            str(self.nomType)
            )
