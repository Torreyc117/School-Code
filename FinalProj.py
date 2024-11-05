import sqlite3
import FinalProjFunctions
#create database
CONNECTION = sqlite3.connect('FinalProject.sqlite3')

#instantia a cursor object
cursor = CONNECTION.cursor()

#create table
cursor.execute('DROP TABLE IF EXISTS IPAddress')
cursor.execute('CREATE TABLE IPAddress (IPAddressID,IPAddressText)')

cursor.execute('DROP TABLE IF EXISTS EventMessage')
cursor.execute('CREATE TABLE EventMessage (MessageText,MessageOccurance)')

FinalProjFunctions.showMenu()
