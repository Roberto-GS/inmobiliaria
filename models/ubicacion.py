# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
import re

_logger = logging.getLogger(__name__)

class ubicacion(models.Model):
    _name = 'inmobiliaria.ubicacion'
    _description = 'Ubicación Geográfica'

    name = fields.Char(string="CIUDAD", required=True)
    provincia = fields.Char(string="PROVINCIA", required=True)

    casa_ids = fields.One2many('inmobiliaria.casa', 'ubicacion_id', string="LISTA DE CASAS")

    @api.constrains('name')
    def validarCiudad(self):
        for loc in self:
            if loc.name:
                # Longitud entre 3 y 30 y solo letras/espacios
                if len(loc.name) < 3 or len(loc.name) > 30 or not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", loc.name):
                    logging.warning(f"Ciudad inválida: {loc.name}. Debe tener entre 3-30 caracteres y sin números.")
                    raise ValidationError(f"La ciudad '{loc.name}' no es válida. Debe tener entre 3 y 30 caracteres y no contener números.")
                else:
                    logging.info("El Nombre de la Ciudad es correcto")
    
    @api.constrains('provincia')
    def validarProvincia(self):
        for loc in self:
            if loc.provincia:
                # Longitud entre 3 y 30 y solo letras/espacios
                if len(loc.provincia) < 3 or len(loc.provincia) > 30 or not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", loc.provincia):
                    logging.warning(f"Provincia inválida: {loc.provincia}. Debe tener entre 3-30 caracteres y sin números.")
                    raise ValidationError(f"La provincia '{loc.provincia}' no es válida. Debe tener entre 3 y 30 caracteres y no contener números.")
                else:
                    logging.info("La Provincia es correcta")