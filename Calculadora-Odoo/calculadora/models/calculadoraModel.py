# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class CalculadoraModulo(models.Model):
    _name = "calculadora.modulo"
    _inherit = ["mail.thread"]
    _description = "Calculadora Odoo"

    num1 = fields.Float(string="Numero 1", required=True, tracking=True)
    op = fields.Selection([('suma','Suma(+)'),('resta','Resta(-)'),
                           ('multiplicar','Multiplicar(*)'),('dividir','Dividir(/)')], required = True,
                          default='suma', traking = True, string= "Operacion")
    num2 = fields.Float(string="Numero 2", required=True,
                        tracking=True, help="Recuerde no dividir entre 0")
    res = fields.Float(string="Resultado", compute='_calcula_resultado', tracking=True)

    @api.onchange('op','num2')
    def compruebaDivision(self):
        if self.op == 'dividir' and self.num2 == 0:
            xx = 1
            self.update({'num2':xx})

    def total_resultado(self):
        resultado = 0
        for total in self:
            print(total.res)
            resultado +=total.res

        mensaje = f'Total de resultados:{resultado}\n'
        raise ValidationError(mensaje)


    def _calcula_resultado(self):
        self.res = 0
        for captura in self:
            if captura.op == 'suma':
                res = captura.num1 + captura.num2
                captura.res = res

            elif captura.op == 'resta':
                res = captura.num1 - captura.num2
                captura.res = res

            elif captura.op == 'multiplicar':
                res = captura.num1 * captura.num2
                captura.res = res

            elif captura.op == 'dividir':
                res = captura.num1 / captura.num2
                captura.res = res









