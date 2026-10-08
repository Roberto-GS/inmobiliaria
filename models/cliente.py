# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
import re

class cliente(models.Model):
    _name = 'inmobiliaria.cliente'
    _description = 'inmobiliaria.cliente'

    name = fields.Char(string="NOMBRE Y APELLIDOS", required=True)
    dni = fields.Char(string="DNI", required=True)
    telefono = fields.Char(string="TELÉFONO", required=True)
    email = fields.Char(string="EMAIL", required=True)
    tipo = fields.Selection([('1','Comprador'),('2','Arrendatario')], required=True)
    imagen = fields.Image(string="IMAGEN", max_width=200, max_height=200)

    visita_ids = fields.Many2many(
        'inmobiliaria.visita', 
        'cliente_visita_rel',    
        'cliente_id',            
        'visita_id',             
        string="VISITAS"
    )
    operacion_ids = fields.One2many('inmobiliaria.operacion', 'cliente_id', string="OPERACIONES")

    @api.constrains('name')
    def validarNombre(self):
        for persona in self:
            if persona.name:
                if len(persona.name) < 3 or len(persona.name) > 50 or not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", persona.name):
                    logging.warning(f"Nombre inválido: {persona.name}")
                    raise ValidationError(f"El nombre '{persona.name}' no es válido. Debe tener entre 3 y 50 caracteres y no contener números.")
                else:
                    logging.info("El Nombre del cliente es correcto")

    @api.constrains('dni')
    def validarDni(self):
        for persona in self:
            if persona.dni:
                if not re.match(r"^\d{8}[A-Z]$", persona.dni.upper()):
                    logging.warning(f"DNI incorrecto: {persona.dni}")
                    raise ValidationError(f"El DNI {persona.dni} no tiene un formato válido (8 números y 1 letra).")
                else:
                    logging.info("El DNI del cliente es correcto")

    @api.constrains('telefono')
    def validarTelefono(self):
        for persona in self:
            if persona.telefono:
                if not (persona.telefono.isdigit() and len(persona.telefono) == 9):
                    logging.warning(f"Teléfono incorrecto: {persona.telefono}")
                    raise ValidationError(f"El teléfono {persona.telefono} debe tener 9 dígitos numéricos.")
                else:
                    logging.info("El Teléfono del cliente es correcto")

    @api.constrains('email')
    def validarEmail(self):
        for persona in self:
            if persona.email:
                if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", persona.email):
                    logging.warning(f"Email incorrecto: {persona.email}")
                    raise ValidationError(f"El formato del email {persona.email} es incorrecto.")
                else:
                    logging.info("El Email del cliente es correcto")