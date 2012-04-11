import sys

class Mp3TagReader():


        def __init__(self, filepath):
                f = open(filepath, "rb")
                f.seek(-128, 2)
                self.TagContent = f.read(128)
                f.close()



        def stripnull(self, Content):
                return str(Content.replace("\x00", ""))



        def readFirstTag(self):
                return self.TagContent[:3]



        def mp3Title(self):
                title = self.TagContent[3:33]
                return self.stripnull(title).strip()


        def mp3Artist(self):
                artist = self.TagContent[33:63]
                return self.stripnull(artist).strip()


        def mp3Album(self):
                album = self.TagContent[63:93]
                return self.stripnull(album).strip()


        def mp3Year(self):
                year = self.TagContent[93:97]
                return self.stripnull(year).strip()


        def mp3genre(self):
                genre_code = self.TagContent[127:128]
                return ord(genre_code)


        @staticmethod
        def checkdata(str_repr, data):
                if data is not None and len(str(data)) != 0:
                        print "{0} is: {1}".format(str_repr, data)

                else:
                        print "{0} is: check metadata".format(str_repr)



t = Mp3TagReader("D:\\3 - Amon Amarth - Guardians of Asgaard.mp3")
#t = Mp3TagReader(r"E:\\SONGS AND VIDEOS\\SONGS\ENGLISH\\20. Pentagram - For Those Who Died Alone.mp3")
#t = Mp3TagReader(sys.argv[1])

if t.readFirstTag() == "TAG":

        Mp3TagReader.checkdata("Title", t.mp3Title())
        Mp3TagReader.checkdata("Artist", t.mp3Artist())
        Mp3TagReader.checkdata("Album", t.mp3Album())
        Mp3TagReader.checkdata("Year", t.mp3Year())
        Mp3TagReader.checkdata("Genre Code", t.mp3genre())
