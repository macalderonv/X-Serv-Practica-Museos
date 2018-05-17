#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: 850 -*-

import xml.etree.ElementTree as etree
import xml.sax.saxutils as saxutils

def characters(word):
    html_escape_table = {
        "&quot;" : '"',
        "&apos;" : "'",
        "&iexcl" : u'¡',
        "&iquest" : u'¿',
        "&aacute;" : u'á',
        "&iacute;" : u'í',
        "&oacute;" : u'ó',
        "&uacute;" : u'ú',
        "&eacute;" : u'é',
        "&ntilde;" : u'ñ',
        "&Ntilde;" : u'Ñ',
        "&Aacute;" : u'Á',
        "&Iacute;" : u'Í',
        "&Oacute;" : u'Ó',
        "&Uacute;" : u'Ú',
        "&Eacute;" : u'É',
        "&Ocirc;" : u'Ô',
        "&ocirc;" : u"ô",
        "&uuml;" : u'ü',
        "&Uuml;" : u'Ü',
        "&nbsp;" : '\n',
        "&rdquo;" : '"',
        "&ldquo;" : '"',
        "&lsquo;" : "'",
        "&rsquo;" : "'",
        "&ordf;" : 'ª'
    }
    escaped = word.replace(word, html_escape_table[word])
    return escaped

def escape(text):
    try:
        upper = text.find("&")
        lower = text.find(";")
        result = str(text[upper:lower+1])
        beg = text.split(result, 1)[0]
        end = text.split(result, 1)[1]
        middle = characters(result)
        chain = beg + middle + end
    except ValueError:
        chain = text
    return chain

def create_address(name, place, num):
    aux = place + " " + name + " " + num
    text = escape(aux)
    return text

def create_dataBase():
    names = []
    addresses = []
    districs = []
    descriptions = []
    accessibilities = []
    neighs = []
    urls = []
    longs = []
    lats = []
    phones = []
    mails = []

    tree = etree.parse("201132-0-museos.xml")
    root = tree.getroot()
    for child in root:
        for node in child:
            flag_empty_desc = False
            flag_empty_phone = False
            flag_empty_mail = False
            flag_empty_lat = False
            flag_empty_long = False
            flag_empty_neigh = False
            flag_empty_dist = False
            for line in node:
                try:
                    if(line.attrib['nombre'] == 'NOMBRE'):
                        names.append(line.text)
                    if(line.attrib['nombre'] == 'DESCRIPCION-ENTIDAD'):
                        descriptions.append(escape(line.text))
                        flag_empty_desc = True
                    if(line.attrib['nombre'] == 'ACCESIBILIDAD'):
                        accessibilities.append(line.text)
                        if(flag_empty_desc == False):
                            descriptions.append("No disponible.")
                    if(line.attrib['nombre'] == "CONTENT-URL"):
                        urls.append(line.text)
                    flag_empty_num = False
                except TypeError:
                    pass

                for tag in line:
                    if(tag.attrib['nombre'] == 'NOMBRE-VIA'):
                        name = escape(tag.text)
                    if(tag.attrib['nombre'] == 'CLASE-VIAL'):
                        place = tag.text
                    if(tag.attrib['nombre'] == 'NUM'):
                        num = tag.text
                        address = create_address(name, place, num)
                        addresses.append(address)
                        flag_empty_num = True
                    if(tag.attrib['nombre'] == 'BARRIO'):
                        neigh = tag.text
                        flag_empty_neigh = True
                        neighs.append(neigh)
                        if(flag_empty_num == False):
                            num = "S/N"
                            address = create_address(name, place, num)
                            addresses.append(address)
                    if(tag.attrib['nombre'] == 'DISTRITO'):
                        dist = tag.text
                        flag_empty_dist = True
                        districs.append(dist)
                    if(tag.attrib['nombre'] == 'LATITUD'):
                        lats.append(str(tag.text))
                        flag_empty_lat = True
                    if(tag.attrib['nombre'] == "LONGITUD"):
                        longs.append(str(tag.text))
                        flag_empty_long = True
                    if(tag.attrib['nombre'] == 'TELEFONO'):
                        phones.append(str(tag.text))
                        flag_empty_phone = True
                    if(tag.attrib['nombre'] == 'EMAIL'):
                        mails.append(tag.text)
                        flag_empty_mail = True

                if(line.attrib['nombre'] == "TIPO"):
                    if(flag_empty_phone == False):
                        phones.append('S/T')
                    if(flag_empty_mail == False):
                        mails.append('No disponible.')
                    if(flag_empty_lat == False):
                        lats.append('-')
                    if(flag_empty_long == False):
                        longs.append('-')
                    if(flag_empty_dist == False):
                        dist = "NS"
                        districs.append(dist)
                    if(flag_empty_neigh == False):
                        neigh = "NS"
                        neighs.append(neigh)
    #print( districs)
    return names, addresses, districs, neighs, urls, descriptions, accessibilities, phones, mails, lats, longs
  

#create_dataBase()
 
