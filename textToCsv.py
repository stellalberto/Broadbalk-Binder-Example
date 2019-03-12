'''
Created on 8 Mar 2019

@author: stellaa
'''
import csv
import configparser


def convertToCsv():
    with open(srcdocs, 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split("|") for line in stripped if line)
#         with open(outfile, 'w') as out_file:
        writer = csv.writer(outfile)
        writer.writerow(('Experiment', 'Year', 'Crop Section','Info'))
        writer.writerows(lines)
        

config = configparser.ConfigParser()        
config.read('config.ini')
outfile = open(config['EXPERIMENT']['outfile'], "w", newline='')
srcdocs = config['EXPERIMENT']['srcdocs']
convertToCsv()
