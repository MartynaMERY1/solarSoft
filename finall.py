#pip install pillow
#pip install opencv-python

import PIL.Image
import PIL.ExifTags
import cv2

def GetGPS(imageName):
    img = PIL.Image.open(imageName)
    exif = {
        PIL.ExifTags.TAGS[k]: v
        for k,v in img._getexif().items()
        if k in PIL.ExifTags.TAGS
    }

    north = exif['GPSInfo'][2]
    east = exif['GPSInfo'][4]

    lat = ((((north[0]*60) + north[1])*60) + north[2])/60/60
    long = ((((east[0]*60) + east[1])*60) + east[2])/60/60

    lat, long = float(lat), float(long)
    return lat,long

def Capture_Event(event, x, y, flags, params):
	if event == cv2.EVENT_LBUTTONDOWN:
		print(f"{x}, {y}")
		
if __name__=="__main__":
    imageName = "DSCN0010.jpg"
    lat, long = GetGPS(imageName)
    print(lat, long)
    img = cv2.imread(imageName, 1)
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', Capture_Event) #called when mause pressed or moved
    cv2.waitKey(0)
