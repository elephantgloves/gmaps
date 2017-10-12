import json
import os
with open('C:/Users/liju/Desktop/python/js/gmapsAPI/config.json', 'r') as configfile:
    cfg = json.load(configfile)

for a in cfg:
    print a
print(cfg['API']).get("googlestatic")

print os.getcwd()


#import yaml
#with open("C:/Users/liju/Desktop/python/js/gmapsAPI/config.yml", 'r') as configfile:
#    cfg = yaml.load(configfile)
#
#for section in cfg:
#    print(section)
#
#print(cfg['API'])
#print(cfg['config'])
#print cfg['API'].get("googlestatic")
##print yaml.dump(cfg)