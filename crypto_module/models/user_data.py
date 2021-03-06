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


class crypto_data_date(models.Model):
    _name = "crypto.data.date"

    price = fields.Float(string="Price")
    price_date = fields.Datetime(string="Price Date")
    crypto_id = fields.Many2one('crypto.data',string="crypto Id")
    name= fields.Char(string="Name")



class crypto_data(models.Model):

    _name = "crypto.data"


    name = fields.Char(string="Name")
    price = fields.Float(string="Price")
    price_date = fields.Datetime(string="Price Date")
    market_cap = fields.Float(string="Market Cap")
    market_cap_dominance = fields.Float(string="market cap Dominance")
    rank = fields.Integer(string="Rank")
    img = fields.Binary(string="Logo")
    price_ids = fields.One2many('crypto.data.date','crypto_id',string="Price History")
    id_code = fields.Char(string="Code")


    start_date = fields.Datetime(string="Start Date")
    end_date = fields.Datetime(string="End Date")



    def view_graph(self):

        action = self.env["ir.actions.act_window"]._for_xml_id("crypto_module.date_action_view_order_graph_date")
        action['domain'] = [('id','in',self.price_ids.ids)]
        return action




    def calculate_price_date(self) :

        url_date = "https://api.nomics.com/v1/exchange-rates/history?key=b1e6e192bca016b2cddfb98b79510f191ad4124f&currency="+self.id_code+"&start=2020-04-14T00%3A00%3A00Z&end=2021-05-14T00%3A00%3A00Z"


        d=requests.get(url_date)

        print ("dddddddddd",d)


        print ("=============",d.json())

        for j in d.json() :

            rate = float(j.get('rate'))
            time = j.get('timestamp')

            date_rate = datetime.strptime(time, '%Y-%m-%dT%H:%M:%SZ')


            self.env['crypto.data.date'].create({'price': rate,'price_date' : date_rate ,'crypto_id' : self.id,'name' : self.name})


        print ("======not=========",self.name)

        return






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

        data_obj.search([]).unlink()

        for i in r.json() :


            date = datetime.strptime(i.get('price_date'), '%Y-%m-%dT%H:%M:%SZ')


            record = data_obj.create({

                'name' : i.get('name'),
                'price' : i.get('price'),
                'price_date' : date,
                'id_code':i.get('id'),
                'market_cap' : i.get('market_cap'),
                'market_cap_dominance' : i.get('market_cap_dominance'),
                'rank' : i.get('rank'),
                'start_date' : self.start_date,
                'end_date' : self.end_date


                })



            





             


        action = self.env["ir.actions.act_window"]._for_xml_id("crypto_module.crypto_datq_action_stored")
        

       
        return action

         



    