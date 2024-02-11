import csv

sitecode =input('Enter site code:')

sitecodeXML = './Update_XML_Files/'+sitecode+'.xml'
sitefile = './Update_XML_Files/'+sitecode+'.txt'

descfile = './Update_XML_Files/desc.txt'

def description():
    with open(descfile, 'r') as myfile3:
        for x in myfile3:
            words = x.split()
            if sitecode in words:
                site_desc = x.rstrip("\n")
                return site_desc
                
    myfile3.close()
    
with open(sitecodeXML, 'w') as myfile1, open(sitefile, 'r') as myfile2:

        myfile1.write(f"""<?xml version="#.0" enconding="UTF-8" standalone="yes"?>
        <digitmapFULLTOlist>""")
        
        for row in myfile2:
            myfile1.write("""
            <DigitmapFullTO>
                <notes>"""+description()+"""</notes>
                <deny>false</deny>
                <digitpattern>"""+row.rstrip("\n")+"""<digitpattern>
            </DigitmapFullTO>    
            """)

        myfile1.write("""
</digitmapFullTOlist>
""")
            
myfile1.close()
myfile2.close()