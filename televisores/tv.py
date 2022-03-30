
class TV:
    numTV = 0
    def __init__(self, marca, estado, control = None, canal = 1, precio = 500, volumen = 1):
        self._marca = marca
        self._canal = canal
        self._precio = precio
        self._estado = estado
        self._volumen = volumen
        self._control = control
        TV.numTV += 1

    def getMarca(self):
        return self._marca
    def setMarca(self, nuevaMarca):
        self._marca = nuevaMarca

    def getCanal(self):
        return self._canal
    def setCanal(self, nuevoCanal):
        if nuevoCanal < 121 and self._estado:
            self._canal = nuevoCanal

    def getPrecio(self):
        return self._precio
    def setPrecio(self, nuevoPrecio):
        self._precio = nuevoPrecio

    def getVolumen(self):
        return self._volumen
    def setVolumen(self, nuevoVolumen):
        if nuevoVolumen < 8 and self._estado:
            self._volumen = nuevoVolumen

    def getControl(self):
        return self._control
    def setControl(self, nuevoControl):
        self._control = nuevoControl

    @classmethod
    def getNumTV(cls):
        return cls.numTV
    @classmethod
    def setNumTV(cls, numero):
        cls.numTV = numero
    
    def turnOn(self):
        self._estado = True
    def turnOff(self):
        self._estado = False

    def getEstado(self):
        return self._estado

    def volumenUp(self):
        if self._volumen < 7 and self._estado:
            self._volumen += 1
    def volumenDown(self):
        if self._volumen > 0 and self._estado:
            self._volumen -= 1

    def canalUp(self):
        if self._canal < 120 and self._estado:
            self._canal += 1
    def canalDown(self):
        if self._canal > 1 and self._estado:
            self._canal -= 1