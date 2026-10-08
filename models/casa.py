# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
import re

_logger = logging.getLogger(__name__)

class casa(models.Model):
   _name = 'inmobiliaria.casa'
   _description = 'inmobiliaria.casa'

   name = fields.Char(string="CÓDIGO", required=True)
   valor = fields.Float(string="VALOR", required=True, default=0.0)
   estimacionValor = fields.Float(string="VALOR ESTIMADO", compute="HacerEstimacionValor", readonly=True, store=True)
   metros2 = fields.Float(string="METROS", required=True)
   numServicios = fields.Integer(string="BAÑOS", required=True)
   numHabitaciones = fields.Integer(string="DORMITORIOS", required=True)
   estado = fields.Boolean(string="BUEN ESTADO", required=True)
   tipo = fields.Selection([('1','Casa'),('2','Piso'),('3','Oficinas')], required=True)
   nota = fields.Char(string="NOTA")
   imagen = fields.Image(string="IMAGEN", max_width=200, max_height=200)

   propietario_id = fields.Many2one('inmobiliaria.propietario', string="PROPIETARIO")
   ubicacion_id = fields.Many2one('inmobiliaria.ubicacion', string="UBICACIÓN", required=True)
   operacion_ids = fields.One2many('inmobiliaria.operacion', 'casa_id', string="OPERACIONES")
   visita_ids = fields.One2many('inmobiliaria.visita', 'casa_id', string="VISITAS")

   @api.depends('metros2', 'numServicios', 'numHabitaciones', 'estado')
   def HacerEstimacionValor(self):
       for casa in self:
           estimacion = (casa.metros2 * 2000) + (casa.numHabitaciones * 10000) + (casa.numServicios * 5000)
           if casa.estado:
               estimacion = estimacion * 1.05
           else:
               estimacion = estimacion * 0.95
           casa.estimacionValor = estimacion
  
   @api.constrains('valor', 'estimacionValor')
   def _validar_valor_mercado(self):
        for casa in self:
            maximo = casa.estimacionValor * 1.50
            minimo = casa.estimacionValor * 0.50
            if casa.valor < minimo or casa.valor > maximo:
                logging.warning(f"El valor de una casa con estas características debe de estar entre {minimo} € y {maximo} €")
                raise ValidationError(f"El valor de una casa con estas características debe de estar entre {minimo} € y {maximo} €")
            else:
                logging.info("El Valor de la casa es correcto")

   @api.constrains('name')
   def validarCOD(self):
       for casa in self:
           if not casa.name or len(casa.name) != 6:
               logging.warning(f"El código {casa.name} tiene una longitud incorrecta")
               raise ValidationError("El código debe tener exactamente 6 caracteres.")
           if not re.match(r"^[A-Z]\d{5}$", casa.name):
               logging.warning(f"El código {casa.name} no cumple el formato Letra + 5 Números")
               raise ValidationError("Formato de código erróneo: Una letra seguida de 5 números (Ej: A12345).")
           logging.info(f"El código {casa.name} es correcto")

   @api.constrains('numHabitaciones', 'tipo')
   def validarDormitorios(self):
       for casa in self:
           if casa.tipo == '3' and casa.numHabitaciones != 0:
               logging.warning("Intento de asignar dormitorios a una oficina")
               raise ValidationError("Una oficina no puede tener dormitorios.")
           else:
               logging.info("El número de dormitorios para el tipo seleccionado es correcto")

   @api.constrains('metros2')
   def validarM2(self):
       for casa in self:
           if casa.metros2 < 35:
               logging.warning(f"Superficie insuficiente: {casa.metros2} m2")
               raise ValidationError("Los metros cuadrados mínimos son 35 m2.")
           else:
               logging.info("La superficie en m2 es correcta")