#!/usr/bin/python

# GNU Public License
# Date 19/10/2016
# Author : Muhammad Dzikri Ramdhani / kiddies

# This tools is used to parse mod_security log on nginx
# Tested Environtment
# OS			: Ubuntu 16.06 Xenial
# Nginx Version		: 1.8.0
# Mod_security

# Regex to get id 		\[id(.*?)\]
# Regex to get severity 	\[severity(.*?)\]
# Regex to get msg 		\[msg(.*?)\]
# Regex to get Date 		\d+\/\d+\/\d+
# Regex to get Time 		\s\d+\:\d+\:\d+
# Regex to get client		\[client(.*?)\]

# Module were used
import re
import time

# Opening file
fo = open('error.log','r')

# Regular Expresion for getting specific data
getDate = re.compile(r'\d+\/\d+\/\d+')
getTime = re.compile(r'\s\d+\:\d+\:\d+')
getMSG = re.compile(r'\[msg(.*?)\]')
getID = re.compile(r'\[id(.*?)\]')
getSeverity = re.compile(r'\[severity(.*?)\]')
getClient = re.compile(r'\[client(.*?)\]')

# Loop for getting data
for baca in fo: 
    textDate = getDate.findall(baca)
    textTime = getTime.findall(baca)
    textID = getID.findall(baca)
    textSVRT = getSeverity.findall(baca)
    textMSG = getMSG.findall(baca)
    textClient = getClient.findall(baca)

    # Condition for printout data
    if (textDate and textTime and textID and textSVRT and textMSG and textClient):
        for tDate in textDate:
            print tDate
        for tTime in textTime:
            print tTime
        for tID in textID:
            print tID
        for tSVRT in textSVRT:
            print tSVRT
        for tMSG in textMSG:
            print tMSG
        for tClient in textClient:
            print tClient
    time.sleep(0.5)
fo.close()
