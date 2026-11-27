from abc import ABC, abstractmethod
from datetime import datetime
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