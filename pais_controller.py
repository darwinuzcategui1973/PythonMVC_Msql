# -*- coding: utf-8 *-*
from pais import Pais
from pais_view import PaisView
import verifica


class PaisController:

    def __init__(self):
        self.vista = PaisView()
        self.pais_controller()

    def pais_controller(self):
        """Controlador general de País"""
        peticion = self.vista.mostrar_menu()
        self.peticion = int(peticion)

        if self.peticion == 1:
            self.crear_pais_controller()
        elif self.peticion == 2:
            self.listar_paises_controller()
        elif self.peticion == 3:
            self.editar_pais_controller()
        elif self.peticion == 4:
            self.eliminar_pais_controller()

    def crear_pais_controller(self):
        """Controlador para creación de nuevo país"""
        if verifica.inicio():
            (pais_nombre, pais_abbr) = self.vista.crear_pais()
            pais = Pais()
            pais.pais = pais_nombre
            pais.abbr = pais_abbr
            pais.create()
            self.vista.confirmar_creacion()
        self.pais_controller()

    def traer_paises(self):
        """Trae una lista de todos los países"""
        pais = Pais()
        listado = pais.read_all()
        return listado

    def listar_paises_controller(self):
        """Controlador del listado de países"""
        listado = self.traer_paises()
        self.vista.listar_paises(listado)
        self.pais_controller()

    def editar_pais_controller(self):
        """Controlador para editar un país"""
        if verifica.inicio():
            listado = self.traer_paises()
            (id, nombre, abbr) = self.vista.editar_pais(listado)
            pais = Pais()
            pais.id = int(id)
            pais.pais = nombre
            pais.abbr = abbr
            pais.update()
            self.vista.confirmar_editar_pais()
        self.pais_controller()

    def eliminar_pais_controller(self):
        """Controlador para eliminar un país"""
        if verifica.inicio():
            listado = self.traer_paises()
            id = self.vista.eliminar_pais(listado)
            id = id
        
            pais = Pais()
        
            pais.id = int(id)
        
            pais.delete()
            self.vista.confirmar_eliminar_pais()
        self.pais_controller()


controller = PaisController()
