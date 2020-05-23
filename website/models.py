from django.db import models

class Enquiry(models.Model):  

    customer_name = models.CharField(max_length=30)  
    customer_mob = models.CharField(max_length=20)
    customer_time  = models.CharField(max_length=50)
    customer_country  = models.CharField(max_length=50)
 
    

    class Meta:
        db_table = 'enquiry'
        managed =  True










# from django.test import TestCase

# # Create your tests here.
# import mysql.connector 

# db_data = mysql.connector.connect(
#     host = 'localhost',
#     username = 'root',
#     password = 'Soumitri1992#'
# )

# my_curser = db_data.cursor()
# my_curser.execute("select count(*) from test_blr.enquiry")
# my_res = my_curser.fetchall()
# for x in my_res:
#     print(x)
    