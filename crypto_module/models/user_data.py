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


        for i in r.json() :

            print ("=====iiii============",i)


        return 



    