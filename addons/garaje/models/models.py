#Imports
from odoo import models, fields, api
from dateutil.relativedelta import *
from datetime import date


#Definimos modelo aparcamiento
class aparcamiento(models.Model):

    #Nombre objeto y descripciones
    _name = 'garaje.aparcamiento'
    _description = 'Permite definir las caracteristicas de un aparcamiento'

    #Valores de la tabla
    name = fields.Char('Dirección', required=True)
    plazas = fields.Integer(string='Plazas', required = True)

    #Relacion entre tablas
    coche_ids = fields.One2many('garaje.coche', 'aparcamiento_id', string='Lista Coches')

#Definimos modelo coche
class coche(models.Model):

    #Nombre objeto y descripciones
    _name = 'garaje.coche'
    _description = 'Permite definir las caracteristicas de un coche'
    _order = 'name'

    #Valores de la tabla
    name = fields.Char(string='Matricula', required = True, size = 7)
    modelo = fields.Char(string='Modelo', required = True) 
    construido = fields.Date(string='Fecha de contrucción')
    consumo = fields.Float('Consumo', (4,1), default=0.0)
    anios = fields.Integer('Años', compute='_get_anios' )
    descripcion = fields.Text('Descripcion')
    averiado = fields.Boolean(string='Averiado', default=False)

    #Relacion entre tablas
    aparcamiento_id = fields.Many2one('garaje.aparcamiento', string='Aparcamiento')
    mantenimiento_ids = fields.Many2many('garaje.mantenimiento',string='Mantenimientos')


    #Metodo calcular años
    @api.depends('construido')
    def _get_anios (self):
        for coche in self:
            hoy = date.today()
            coche.anios= relativedelta(hoy, coche.construido).years


#Definimos modelo mantenimiento
class mantenimiento(models.Model):
    _name = 'garaje.mantenimiento'
    _description = 'Permite definir las caracteristicas de un coche'
    _order = 'fecha'

    #name = fields.Char()
    fecha = fields.Date('Fecha', required = True, default = fields.Date.today())
    tipo = fields.Selection(string='Tipo', selection=[('l','lavar'),('r','revision'),('m','mecanica'),('p','pintura')], default = 'l')
    coste = fields.Float('Coste', (8,2), help='Coste total del mantenimiento')

    #Relacion entre tablas
    coche_ids = fields.Many2many('garaje.coche', string='Coches')
