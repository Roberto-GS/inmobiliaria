# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date, timedelta
import logging
import re

_logger = logging.getLogger(__name__)

class operacion(models.Model):
    _name = 'inmobiliaria.operacion'
    _description = 'inmobiliaria.operacion'

    name = fields.Char(string="ID", required=True)
    tipo = fields.Selection([('1','Venta'),('2','Alquiler')], required=True, default='1')
    precioFinal = fields.Float(string="PRECIO FINAL", required=True, default=0.0)
    fecha = fields.Date(string="FECHA", default=fields.Date.today, required=True)
    nota = fields.Char(string="NOTA")
    estado = fields.Selection([
        ('1','Borrador'),
        ('2','Confirmada'), 
        ('3','Cancelada')
    ], required=True, default='1')

    casa_id = fields.Many2one('inmobiliaria.casa', string="INMUEBLE", required=True)
    cliente_id = fields.Many2one('inmobiliaria.cliente', string="CLIENTE")

    @api.constrains('name')
    def validarName(self):
        for op in self:
            if op.name:
                # Debe empezar por 'O' seguido de uno o más números
                if not re.match(r"^O\d+$", op.name):
                    logging.warning(f"ID de la operación inválido: {op.name}")
                    raise ValidationError(f"El ID '{op.name}' no es válido. Debe empezar por 'O' seguida de números (Ej: O123).")
                else:
                    logging.info("El ID de la operación es correcto")

    @api.constrains('precioFinal')
    def validarPrecio(self):
        for op in self:
            if op.precioFinal < 0:
                logging.warning(f"Precio negativo detectado: {op.precioFinal}")
                raise ValidationError("El precio final no puede ser un valor negativo.")
            else:
                logging.info("El Precio Final es correcto")

    @api.constrains('fecha')
    def validarFecha(self):
        for op in self:
            if op.fecha:
                hoy = date.today()
                limite_futuro = hoy + timedelta(days=365)
                
                if op.fecha > limite_futuro:
                    logging.warning(f"Fecha fuera de rango futuro: {op.fecha}")
                    raise ValidationError(f"La fecha no puede ser superior a un año desde hoy (Límite: {limite_futuro}).")
                else:
                    logging.info("La Fecha de la operación es correcta")
    
    @api.constrains('cliente_id')
    def validarClienteAsignado(self):
        for op in self:
            if not op.cliente_id:
                logging.warning(f"Intento de crear operación {op.name} sin cliente")
                raise ValidationError("Debe seleccionar un cliente para registrar la operación.")
            else:
                logging.info(f"Cliente {op.cliente_id.name} asignado correctamente a la operación {op.name}")