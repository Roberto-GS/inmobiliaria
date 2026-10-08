# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date
import logging
import re

_logger = logging.getLogger(__name__)

class visita(models.Model):
    _name = 'inmobiliaria.visita'
    _description = 'inmobiliaria.visita'

    name = fields.Char(string="ID", required=True)
    fecha = fields.Date(string="FECHA", default=fields.Date.today, required=True)
    comentarios = fields.Char(string="COMENTARIOS")
    interes = fields.Selection([('1','Bajo'),('2','Medio'), ('3','Alto')], required=True, default='2')

    casa_id = fields.Many2one('inmobiliaria.casa', string="INMUEBLE", required=True)
    cliente_ids = fields.Many2many(
        'inmobiliaria.cliente', 
        'cliente_visita_rel',    
        'visita_id', 
        'cliente_id', 
        string="CLIENTES"
    )

    @api.constrains('name')
    def validarName(self):
        for vi in self:
            if vi.name:
                # Debe empezar por 'V' seguido de uno o más números
                if not re.match(r"^V\d+$", vi.name):
                    logging.warning(f"ID de la visita es inválido: {vi.name}")
                    raise ValidationError(f"El ID '{vi.name}' no es válido. Debe empezar por 'V' seguido de números (Ej: V123)")
                else:
                    logging.info("El ID de la visita es correcto")

    @api.constrains('fecha')
    def validarFecha(self):
        for vi in self:
            if vi.fecha:
                if vi.fecha < date(2020, 1, 1):
                    logging.warning(f"Fecha de visita demasiado antigua: {vi.fecha}")
                    raise ValidationError("La fecha de la visita no parece válida (demasiado antigua).")
                else:
                    logging.info("La fecha de la visita es correcta")

    @api.constrains('cliente_ids')
    def validarClientes(self):
        for vi in self:
            # Validar que al menos haya un cliente en la visita
            if not vi.cliente_ids:
                logging.warning("Intento de crear visita sin clientes")
                raise ValidationError("Debe asignar al menos un cliente a la visita.")
            else:
                logging.info(f"Visita con {len(vi.cliente_ids)} clientes validada")