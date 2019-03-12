# -*- coding: utf-8 *-*


class PaisView:

    def __init__(self):
        self.tab1 = "    "
        self.tab2 = "    " * 2
        self.tab3 = "    " * 3
        self.txt_opt = "%sElija una opción: " % self.tab2
        self.txt_pais = "%sPaís: " % self.tab3
        self.txt_abbr = "%sAbreviatura: " % self.tab3
        self.txt_id = "%sID de país: " % self.tab3
        pass

    def mostrar_menu(self):
        """Vista del menú de opciones"""

        menu = """
        Menú del Gestor de Países
            (1) Crear un país
            (2) Ver listado de países
            (3) Editar un país
            (4) Eliminar un país

            (0) Salir

        """
        print (menu)

        opcion = input(self.txt_opt)
        return opcion

    def crear_pais(self):
        """Vista del formulario para crear nuevo país"""

        print ("""
        CREAR UN NUEVO PAÍS
        """)
        pais = input(self.txt_pais)
        abbr = input(self.txt_abbr)
        return (pais, abbr)

    def confirmar_creacion(self):
        """Vista de confirmación de creación de nuevo país"""

        print ("""
        País creado con éxito!
        """)

    def listar_paises(self, listado):
        """Vista para el listado de países"""

        print ("""
            LISTADO DE PAÍSES:
        """)
        for row in listado:
            id = row[0]
            pais = row[1]
            abbr = row[2]
            print ( "%s[%d] %s (%s)" % (self.tab3, id, pais, abbr) )

    def editar_pais(self, listado):
        """Vista del formulario para editar un país"""

        self.listar_paises(listado)
        print ("\n\n")
        id = input(self.txt_id)
        print ("\n")
        pais = input(self.txt_pais)
        abbr = input(self.txt_abbr)
        return (int(id), pais, abbr)

    def confirmar_editar_pais(self):
        """Vista de confirmación de edición"""

        print ("""
        País editado correctamente.
        """)

    def eliminar_pais(self, listado):
        """Vista de formulario para eliminar país"""

        self.listar_paises(listado)
        print ("\n\n")
        id = input(self.txt_id)
        print ("\n")
        return int(id)

    def confirmar_eliminar_pais(self):
        """Vista de cofirmación eliminar país"""
        print ("""
        País eliminado correctamente.
        """)
