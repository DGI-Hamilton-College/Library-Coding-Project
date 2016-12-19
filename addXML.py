import xml.etree.ElementTree as etree
import os
import csv
def idFinder(fileName):
    tree=etree.parse(fileName)
    root=tree.getroot()
    for node in root.iter('{http://www.loc.gov/mods/v3}mods'):
        x=node.find('{http://www.loc.gov/mods/v3}identifier').text
        return x
def addData(parent,field,txt):
    c=etree.SubElement(parent,field)
    c.text=txt
    return(c)
        
        
        
csvsource=open('C:\\Users\\aneslin\\Documents\\Beinecke Index Geographic Metadata - all-auth.csv','r')
reader=csv.reader(csvsource)        
        
myDict={rows[1]:rows[2] for rows in reader}       

#print (myDict['bei-m003l'])  
        
etree.register_namespace('', 'http://www.loc.gov/mods/v3')
nb= {'mods':'http://www.loc.gov/mods/v3',}


for root, dirs, files in os.walk('C:\\Users\\aneslin\\Documents\\aarons_mods_originals2'):
    for things in files:
        #assemble file name from root and filename
      x=(os.path.join(root,things))
      #parse as xml
      tree=etree.parse(x)
      base=tree.getroot()
      a=idFinder(x)
      if a in myDict:
        b=etree.SubElement(base,'{http://www.loc.gov/mods/v3}subject', attrib={'authority':'lcsh'})  
        z=myDict[a].split(";")
       
        for places in z:
            if places !='':
                addData(b,'{http://www.loc.gov/mods/v3}geographic', places)
            else:continue
            tree.write('C:\\Users\\aneslin\\Documents\\testfiles\\{filename}'.format(filename=things))
#            etree.dump(base)
#            print (z,'\n', a,'\n','__________')
        continue
print (base)
                
          
    
