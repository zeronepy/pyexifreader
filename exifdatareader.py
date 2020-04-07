from exif import Image
print("PROGRAMMED BY : 01011000 for SpyHackerZ Members")
ipath = input("IMAGE NAME in 'THIS FOLDER' : ")
with open(ipath,"rb") as imagefile:
    i = Image(imagefile)
tarih = i.datetime
aci = i.gps_img_direction

kordinat = i.gps_latitude ," N  - ",i.gps_longitude,"E "
yazilim = i.software
model = i.model
distance = i.subject_distance

print("DATE : ", tarih,"\n",'COMPASS :',aci,"\n","GPS COORDINATE :",kordinat,"\n","SOFTWARE : ",yazilim,"\n","PHONE MODEL:",model,"\n","SUBJECT DISTANCE 'METRIC' :",distance)