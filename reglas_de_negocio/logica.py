from abc import ABC, abstractmethod
from datetime import datetime, timedelta
import math

class ModalidadCobro(ABC):
    @abstractmethod
    def calcular_importe(self, fecha_ingreso: datetime, fecha_salida: datetime) -> int:
        pass

class CobroPorMinuto(ModalidadCobro):
    def __init__(self, tarifa_minuto: int):
        self.tarifa_minuto = tarifa_minuto

    @property
    def tarifa_minuto(self) -> int:
        return self.__tarifa_minuto

    @tarifa_minuto.setter
    def tarifa_minuto(self, valor: int):
        if valor <= 0:
            raise ValueError("La tarifa por minuto debe ser positiva.")
        self.__tarifa_minuto = valor

    def calcular_importe(self, fecha_ingreso: datetime, fecha_salida: datetime) -> int:
        if fecha_salida < fecha_ingreso:
            raise ValueError("La fecha de salida no puede ser anterior al ingreso.")
        segundos = (fecha_salida - fecha_ingreso).total_seconds()
        minutos = max(1, math.ceil(segundos / 60))
        return minutos * self.__tarifa_minuto

class CobroDiario(ModalidadCobro):
    def __init__(self, tarifa_diaria: int):
        self.tarifa_diaria = tarifa_diaria

    @property
    def tarifa_diaria(self) -> int:
        return self.__tarifa_diaria

    @tarifa_diaria.setter
    def tarifa_diaria(self, valor: int):
        if valor <= 0:
            raise ValueError("La tarifa diaria debe ser positiva.")
        self.__tarifa_diaria = valor

    def calcular_importe(self, fecha_ingreso: datetime, fecha_salida: datetime) -> int:
        if fecha_salida < fecha_ingreso:
            raise ValueError("La fecha de salida no puede ser anterior al ingreso.")
        segundos = (fecha_salida - fecha_ingreso).total_seconds()
        dias = max(1, math.ceil(segundos / 86400))  # 86400 segundos = 24 horas
        return dias * self.__tarifa_diaria

class CobroMensual(ModalidadCobro):
    def __init__(self, tarifa_mensual: int):
        self.tarifa_mensual = tarifa_mensual

    @property
    def tarifa_mensual(self) -> int:
        return self.__tarifa_mensual

    @tarifa_mensual.setter
    def tarifa_mensual(self, valor: int):
        if valor <= 0:
            raise ValueError("La tarifa mensual debe ser positiva.")
        self.__tarifa_mensual = valor

    def calcular_importe(self, fecha_ingreso: datetime, fecha_salida: datetime) -> int:
        if fecha_salida < fecha_ingreso:
            raise ValueError("La fecha de salida no puede ser anterior al ingreso.")
        # Las estadías cubiertas por suscripción no generan cobro adicional al salir
        return 0

# --- CREACIÓN CLASE VEHICULO ---

class Vehiculo:
    def __init__(self, patente: str, nombre_responsable: str, contacto_responsable: str):
        # Al asignar aquí, Python redirige el valor al setter automáticamente
        self.patente = patente
        self.nombre_responsable = nombre_responsable
        self.contacto_responsable = contacto_responsable

    # --- ATRIBUTO PATENTE ---
    @property
    def patente(self) -> str:
        return self.__patente

    @patente.setter
    def patente(self, valor: str):
        p_valida = valor.strip().upper()  # ¡Llama al método con ()!
        if not p_valida:
            raise ValueError("La patente no puede estar vacía.")
        self.__patente = p_valida

    # --- ATRIBUTO NOMBRE RESPONSABLE ---
    @property
    def nombre_responsable(self) -> str:
        return self.__nombre_responsable

    @nombre_responsable.setter
    def nombre_responsable(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("El nombre del responsable no puede estar vacío.")
        self.__nombre_responsable = valor.strip()

    # --- ATRIBUTO CONTACTO RESPONSABLE ---
    @property
    def contacto_responsable(self) -> str:
        return self.__contacto_responsable

    @contacto_responsable.setter
    def contacto_responsable(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("El contacto del responsable no puede estar vacío.")
        self.__contacto_responsable = valor.strip()

# --- CREACIÓN CLASE SUSCRIPCION ---

class Suscripcion:
    def __init__(self, patente: str, fecha_inicio: datetime, tarifa_pago: int):
        self.patente = patente
        self.fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_inicio + timedelta(days=30)
        self.__tarifa_pago = tarifa_pago

    @property
    def patente(self):
        return self.__patente

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @property
    def fecha_fin(self):
        return self.__fecha_fin

    @property
    def tarifa_pago(self):
        return self.__tarifa_pago

    @patente.setter
    def patente(self, valor: str):
        valida = valor.strip().upper()
        if not valida:
            raise ValueError("La patente no puede estar vacía.")
        self.__patente = valida

    @tarifa_pago.setter
    def tarifa_pago(self, valor: int):
        if valor <= 0:
            raise ValueError("El pago de la suscripción debe ser positivo.")
        self.__tarifa_pago = valor

    def esta_vigente(self, fecha_referencia: datetime) -> bool:
        return self.__fecha_inicio <= fecha_referencia < self.__fecha_fin

# --- CREACIÓN CLASE SUSCRIPCION ---

class Estadia:
    def __init__(self, patente, modalidad: ModalidadCobro, fecha_ingreso):
        self.patente = patente
        self.__modalidad = modalidad
        self.__fecha_ingreso = fecha_ingreso
        self.__fecha_salida = None
        self.__monto_pagado = None
        self.__activa = True

    @property
    def modalidad(self) -> ModalidadCobro:
        return self.__modalidad

    @property
    def fecha_ingreso(self) -> datetime:
        return self.__fecha_ingreso

    @property
    def fecha_salida(self) -> datetime:
        return self.__fecha_salida

    @property
    def monto_pagado(self):
        return self.__monto_pagado

    @property
    def activa(self) -> bool:
        return self.__activa

    def finalizar_estadia(self, fecha_salida: datetime) -> int:
        if not self.__activa:
            raise ValueError("Esta estadía ya fue finalizada.")
        
        monto = self.__modalidad.calcular_importe(self.__fecha_ingreso, fecha_salida)
        
        self.__fecha_salida = fecha_salida
        self.__monto_pagado = monto
        self.__activa = False
        return monto

# --- CREACIÓN FUNCIÓN validar_ingreso_permitido  ---

def validar_ingreso_permitido(patente, estadias_activas: list[Estadia]):
    patente_limpia = patente.strip().upper()
    
    for estadia in estadias_activas:
        if estadia.patente == patente_limpia and estadia.activa:
            raise ValueError(f"El vehículo con patente {patente_limpia} ya tiene una estadía activa.")


# --- CREACIÓN FUNCIÓN validar_suscripcion_nueva ---

def validar_suscripcion_nueva(patente, fecha_inicio: datetime, suscripciones_existentes: list[Suscripcion]):
    patente_limpia = patente.strip().upper()
    fecha_fin_nueva = fecha_inicio + timedelta(days=30)
    
    for sub in suscripciones_existentes:
        if sub.patente == patente_limpia:
            if not (fecha_fin_nueva <= sub.fecha_inicio or fecha_inicio >= sub.fecha_fin):
                raise ValueError(f"El vehículo {patente_limpia} ya posee una suscripción en ese período.")