import arcpy

# määritellään polku, jossa bufferoitava tiedosto sijaitsee. Tänne myös valmis analyysi tallennetaan.
arcpy.env.workspace = "C:\Paikalliset työkansiot\Turun täydennysrakentaminen\Asemakaavat vireillä"

# nimetään bufferoitava tiedosto. Ei tietoa miksi pitää olla kaksi kenoviivaa.
tontit = arcpy.env.workspace + "\\Ak_vireilla.shp"

# määritellään metreissä bufferietäisyydet
buffDists = [100,500,1000]

# loopataan aineisto määriteltyjen etäisyyksien avulla ja tallennetaan valmiit shapet.
for buff in buffDists:
	tonttioutput = arcpy.env.workspace + "\\tontti" + str(buff) + ".shp"
	arcpy.analysis.Buffer(tontit, tonttioutput, str(buff)+ " Meters","FULL","ROUND","NONE",None,"PLANAR")


