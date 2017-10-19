"""
Edit: 001
"""
import csv
import json
import os
import sys

basedirectory=os.getcwd()

xyCSVLocation=basedirectory+"/xytest.csv"
with open(basedirectory+"/config.json", 'r') as configfile:
    cfg = json.load(configfile)

staticAPIkey=cfg['API'].get("googlestatic")
streetViewImageAPIkey=cfg['API'].get("googlestreetview")

size=cfg['config'].get("size")
zoom=cfg['config'].get("zoom")
maptype=cfg['config'].get("maptype")

header="""
<html> 
<head></head>
<body style="width: 100%; height: 100%; margin: 0; padding: 0;"> 

"""  

footer="""
</body>
</html>
"""
       
def getxyfromCSV(CSVLocation, delimiter=","):
    """Reads CSV file with x,y coordinates and stores them in array. Default delimiter=,"""
    with open(CSVLocation) as inputxy:
        xyArray=[]
        csvReader=csv.reader(inputxy, delimiter=delimiter)
        for row in csvReader:
            xyArray.append(','.join(row))
    
    return xyArray

"""Test to print output xy array using CSV file defined in xyCSVLocation above""" 
print "Outputarray" , getxyfromCSV(xyCSVLocation, delimiter=",")
   

def mapBlockGenerator(coordinateArray):
    """pass array of xy values to generator"""
    mapBlock=""
    for xyrecord in coordinateArray: 
        mapBlock=mapBlock+codeGeneratorSingleRecord(xyrecord, size, zoom, maptype, staticAPIkey)        
    
    return mapBlock
    
def mapBlockGeneratorMM(coordinateArray):
    """pass array of xy values to generator"""
    mapBlock=""
    centerxy=coordinateArray[0]
    markerstring=generateMultipleMarkerString(coordinateArray) 
    mapBlock=mapBlock+codeGeneratorSingleRecord(centerxy, size, zoom, maptype, staticAPIkey, markerstring=markerstring)        
    
    return mapBlock

def generateMultipleMarkerString(coordinateArray):
    
    multipleMarkerString=''
    multipleMarkerString=('|').join(inputarray)
    
    return multipleMarkerString

def codeGeneratorSingleRecord(xypair, size, zoom, maptype, apikey, markerstring=''):
    """returns html tag for a single xy record as a string"""   
    staticTagmaptype=xypair+'</br>\n<img src="https://maps.googleapis.com/maps/api/staticmap?maptype='+maptype
    
    staticTagcoords="&center="+xypair
    
    staticTagzoom="&zoom="+zoom
    
    staticTagSize="&size="+size   
    
    if markerstring=='': 
        staticTagend="&markers="+xypair+"&key="+apikey+"\"></img></br></br>\n"
        # print staticTagend
    else: 
        staticTagend="&markers="+markerstring+"&key="+apikey+"\"></img></br></br>\n"
        # print staticTagend
    
    
    singleRecordTag=staticTagmaptype+staticTagcoords+ \
    staticTagzoom+staticTagSize+staticTagend
    
    
    return singleRecordTag
    
def coordinateParser(csvFile):
    coordinateArray=[]
    pass
    return coordinateArray
    
def codeGenerator(header, mapblock, footer):
    finalHTMLblock=header+mapblock+footer
    return finalHTMLblock

if __name__ == '__main__':
    location=sys.argv
    if len(location)>1:
        csvfilelocation=location[1]
        """read csv"""
        inputarray=getxyfromCSV(csvfilelocation)
        """make codeblock"""
        outputfile=basedirectory+"/outputMapFile.html"
        with open(outputfile, 'w') as outputFile:           
            if len(location)>2:
                print "Set to run with multiple markers on one map\nIf multiple markers not visible, please lower magnification in config"
                outputFile.write(codeGenerator(header, mapBlockGeneratorMM(inputarray), footer))
                os.startfile(outputfile)
            
        
            else:
                outputFile.write(codeGenerator(header, mapBlockGenerator(inputarray), footer))
                os.startfile(outputfile)
        
    else: 
        print "specify a CSV file in runtime arguments"
    
