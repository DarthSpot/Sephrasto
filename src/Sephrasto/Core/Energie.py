from EventBus import EventBus
from VoraussetzungenListe import VoraussetzungenListe
import copy

# Implementation for Energien (Karma, AsP, GuP). Using the type object pattern.
# EnergieDefinition: type object, initialized with database values
# Energie: character editor values, initialised with definition but supports overrides
class EnergieDefinition:
    displayName = "Energie"
    serializationName = "Energie"

    def __init__(self):
        # Serialized properties
        self.name = ""
        self.anzeigename = ""
        self.text = ""
        self.steigerungsfaktor = 1
        self.voraussetzungen = VoraussetzungenListe()
        self.sortorder = 0

    def deepequals(self, other): 
        if self.__class__ != other.__class__: return False
        return self.__dict__ == other.__dict__

    def finalize(self, db):
        pass

    def details(self, db):
        return f"SF {self.steigerungsfaktor}. {self.text}"

    def serialize(self, ser):
        ser.set('name', self.name)
        ser.set('text', self.text)
        ser.set('voraussetzungen', self.voraussetzungen.text)
        ser.set('anzeigename', self.anzeigename)
        ser.set('steigerungsfaktor', self.steigerungsfaktor)
        ser.set('sortorder', self.sortorder)
        EventBus.doAction("energiedefinition_serialize", { "object" : self, "serializer" : ser})

    def deserialize(self, ser):
        self.name = ser.get('name')
        self.text = ser.get('text')
        self.voraussetzungen.compile(ser.get('voraussetzungen', ''))
        self.anzeigename = ser.get('anzeigename')
        self.steigerungsfaktor = ser.getInt('steigerungsfaktor')
        self.sortorder = ser.getInt('sortorder')
        EventBus.doAction("energiedefinition_deserialize", { "object" : self, "deserializer" : ser})

class Energie:
    def __init__(self, definition, charakter):
        self.definition = definition
        self.charakter = charakter
        self.basiswert = 0
        self.wert = 0
        self.mod = 0

    def __deepcopy__(self, memo=""):
        # create new object
        cls = self.__class__
        result = cls.__new__(cls)
        # deepcopy everything except for self, charakter and definition
        memo[id(self)] = result
        memo[id(self.charakter)] = self.charakter
        memo[id(self.definition)] = self.definition
        for k, v in self.__dict__.items():
            setattr(result, k, copy.deepcopy(v, memo))
        return result

    @property
    def name(self):
        return self.definition.name

    @property
    def anzeigename(self):
        return self.definition.anzeigename

    @property
    def text(self):
        return self.definition.text

    @property
    def steigerungsfaktor(self):
        return self.definition.steigerungsfaktor

    @property
    def voraussetzungen(self):
        return self.definition.voraussetzungen

    @property
    def sortorder(self):
        return self.definition.sortorder

    @property
    def gesamtwert(self):
        return self.basiswert + self.wert + self.mod

    def steigerungskosten(self, numSteigerungen = 1):
        if numSteigerungen == 0:
           return 0
        startWert = self.wert
        multiplier = 1
        if numSteigerungen < 0:
            startWert = max(self.wert + numSteigerungen, 0)
            numSteigerungen = self.wert - startWert
            multiplier = -1

        kosten = 0
        nextWert = startWert +1
        for i in range(numSteigerungen):
            kosten += nextWert * self.steigerungsfaktor
            nextWert += 1
        kosten *= multiplier
        return EventBus.applyFilter("energie_kosten", kosten, { "charakter" : self.charakter, "energie" : self.name, "wertVon" : startWert, "wertAuf" : startWert + numSteigerungen })

    def kosten(self):
        kosten = sum(range(self.wert+1)) * self.steigerungsfaktor
        return EventBus.applyFilter("energie_kosten", kosten, { "charakter" : self.charakter, "energie" : self.name, "wertVon" : 0, "wertAuf" : self.wert })

    def aktualisieren(self):
        self.basiswert = 0
        self.mod = 0