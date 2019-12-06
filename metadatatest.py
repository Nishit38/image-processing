from PIL import Image
import piexif

def metadata(img_path):
  zeroth_ifd = {piexif.ImageIFD.Make: u"DJI",
                piexif.ImageIFD.XResolution: (72, 1),
                piexif.ImageIFD.YResolution: (72, 1),
                piexif.ImageIFD.Software: u"piexif",
                piexif.ImageIFD.Model: u"FC6310",
                }
  exif_ifd = {piexif.ExifIFD.DateTimeOriginal: u"2099:09:29 10:10:10",
              piexif.ExifIFD.LensMake: u"LensMake",
              piexif.ExifIFD.Sharpness: 65535,
              piexif.ExifIFD.ExposureTime : (1,320),
              piexif.ExifIFD.LensSpecification: ((1, 1), (1, 1), (1, 1), (1, 1)),
              piexif.ExifIFD.ISOSpeedRatings : 100,
              piexif.ExifIFD.FocalLength : (9,1),
              piexif.ExifIFD.MeteringMode: 2,
              piexif.ExifIFD.MaxApertureValue: (297,100),
              piexif.ExifIFD.ExposureBiasValue : (0,1) ,
              piexif.ExifIFD.FocalLengthIn35mmFilm : 24,
              # piexif.ExifIFD.ExifVersion : 48,50 ,
              }
  gps_ifd = {piexif.GPSIFD.GPSVersionID: (2, 0, 0, 0),
             piexif.GPSIFD.GPSAltitudeRef: 1,
             piexif.GPSIFD.GPSAltitude: (60,1),
             piexif.GPSIFD.GPSDateStamp: u"1999:99:99 99:99:99",
             piexif.GPSIFD.GPSLatitude : ((22,1),(34,1),(34,1)),
             piexif.GPSIFD.GPSLongitude : ((72,1),(32,1),(22,1))
             }
  first_ifd = {piexif.ImageIFD.Make: u"DJI",
               piexif.ImageIFD.XResolution: (40, 1),
               piexif.ImageIFD.YResolution: (40, 1),
               piexif.ImageIFD.Software: u"piexif"
               }

  exif_dict = {"0th":zeroth_ifd, "Exif":exif_ifd, "GPS":gps_ifd, "1st":first_ifd}
  exif_bytes = piexif.dump(exif_dict)
  im = Image.open(img_path)
  im.save(img_path, exif=exif_bytes)


# https://www.awaresystems.be/imaging/tiff/tifftags/privateifd/exif.html