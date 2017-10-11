import os
import csv
import sys

xyCSVLocation="C:xytest.csv"

staticAPIkey=""
streetViewImageAPIkey=""

size="640x400"
zoom="18"
maptype="hybrid"

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

def codeGeneratorSingleRecord(xypair, size, zoom, maptype, apikey):
    """returns html tag for a single xy record as a string"""   
    staticTagmaptype='<img src="https://maps.googleapis.com/maps/api/staticmap?maptype='+maptype
    
    staticTagcoords="&center="+xypair
    
    staticTagzoom="&zoom="+zoom
    
    staticTagSize="&size="+size
    
    
    staticTagend="&markers="+xypair+"&key="+apikey+"\"></img></br>"
    
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
        #print "codeblock", codeGenerator(header, mapBlockGenerator(inputarray), footer)
        outputfile="C:/Users/liju/Desktop/python/js/newjstest.html"
        with open(outputfile, 'w') as outputFile:
            outputFile.write(codeGenerator(header, mapBlockGenerator(inputarray), footer))
        #for i in inputlist: outputFile.write(i.encode("utf8")+"\n")
            os.startfile(outputfile)
        
    else: 
        print "specify a CSV file in runtime arguments"
    
