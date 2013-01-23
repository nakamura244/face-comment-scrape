# -*- coding: utf-8 -*-
from ameblo_face.db_model import *


class Service:
 
     #def __init__():
     
     def get_talent_id(self, name):
         talent = session.query(Talent).filter(Talent.name == name).first()
         return talent if talent else 0
 
     def get_photo_id(self, img_file):
         photo = session.query(Photo).filter(Photo.img_file == img_file).first()
         return photo if photo else 0
#     def get_shop_id(self, shop_key):
#         obj_shop = session.query(MasterShop).filter(MasterShop.shop_key == shop_key).first()
#         return obj_shop.shop_id
# 
#     def get_category_id(self, category_sub_key):
#         obj_category = session.query(MasterCategory).filter(MasterCategory.category_sub_key == category_sub_key).first()
#         return obj_category.category_id
# 
#     def check_product(self, url, shop_id, category_id):
#         obj_product = session.query(Product).filter(and_(Product.detail_url==url,Product.shop_id==shop_id,
#                       Product.category_id==category_id)).first()
#         return obj_produt
 
