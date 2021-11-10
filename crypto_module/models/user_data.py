# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################
from itertools import groupby
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
import requests
from datetime import datetime




class crypto_data(models.Model):

    _name = "crypto.data"


    name = fields.Char(string="name")
    price = fields.Float(string="Price")
    price_date = fields.Datetime(string="Price Date")
    market_cap = fields.Float(string="Market Cap")
    market_cap_dominance = fields.Float(string="market cap Dominance")
    rank = fields.Integer(string="Rank")
    img = fields.Binary(string="Logo")



class token_detail(models.Model):

    _name = "user.data.crypto"


    experience = fields.Selection([('never','Never Invested'),('zero_three','0 To 3 years Of Experience'),('three_more','3+ years Of Experience')],string="Experience")
    risk_amount = fields.Float(string="Risk Amount")
    start_date = fields.Datetime(string="Start Date")
    end_date = fields.Datetime(string="End Date")
    code = fields.Char(string="Code")


    def submit_data(self) :

        url = "https://api.nomics.com/v1/currencies/ticker?key=b1e6e192bca016b2cddfb98b79510f191ad4124f&ids=&interval=1d,30d&convert=EUR&per-page=100&page=1"


        r=requests.get(url)
        data_obj = self.env['crypto.data']

        # data_obj.search([]).unlink()

        for i in r.json() :


            date = datetime.strptime(i.get('price_date'), '%Y-%m-%dT%H:%M:%SZ')


            data_obj.create({

                'name' : i.get('name'),
                'price' : i.get('price'),
                'price_date' : date,

                'market_cap' : i.get('market_cap'),
                'market_cap_dominance' : i.get('market_cap_dominance'),
                'rank' : i.get('rank'),


                })




        action = self.env["ir.actions.act_window"]._for_xml_id("crypto_module.crypto_datq_action_stored")
        

       
        return action

         



    