import argparse


parser = argparse.ArgumentParser(description='Edit ID3v1 Tags',add_help=True)

parser.add_argument("-p",action ="store",dest='filepath',help="Provide complete path of mp3 file")
parser.add_argument("-t",action ="store",dest='Title',help="Provide title for the track")
parser.add_argument("-a",action ="store",dest='Artist',help="Provide artist for the track")
parser.add_argument("-al",action ="store",dest='Album',help="Provide album for the track")
parser.add_argument("-y",action ="store",dest='Year',help="Provide Year for the track")
parser.add_argument("-g",action ="store",dest='Genre_Code',help="Provide genre_code for the track")

output = parser.parse_args()

class editMp3Tag():

        def __init__(self,filepath):

                self.f = open(filepath,"r+b")

        def writeTag(self,seek_pos,content):
                self.f.seek(seek_pos,2)
                self.f.write(content)


        def editTitleTag(self,Title):

                if Title is not None:

                        if len(Title)<=30:
                                self.handleTag(Title,-125)

                        else:
                                print "length of title is greater than 30 bytes."


        def editAlbumTag(self,Album_Name):

                if Album_Name is not None:

                        if len(Album_Name) <= 30:
                                self.handleTag(Album_Name,-65)

                        else:
                                print "length of album is greater than 30 bytes."



        def editArtistTag(self,Artist_Name):

                if Artist_Name is not None:

                        if len(Artist_Name) <= 30:
                                self.handleTag(Artist_Name,-95)

                        else:
                                print "length of artist is greater than 30 bytes."



        def editYearTag(self,Year):

                if Year is not None:

                        if len(Year) <= 4:
                                self.handleTag(Year,-35)
                        else:
                                print "length of year is greater than 4 bytes."



        def editGenreTag(self,Genre_Code):

                if Genre_Code is not None:

                        if len(Genre_Code)==1:
                                self.handleTag(Genre_Code,-2)

                        else:
                                print "Length of Genre_Code is greater than 1 bytes."



        def closeFile(self):
                self.f.close()


        def generateNull(self,data):
                total_count = 30
                if data is not None:

                        initial_count = len(data)
                        difference = total_count - initial_count
                        diff = "\x00" * difference
                        return diff


        def handleTag(self,tag,pos):

               tag += self.generateNull(tag)
               print tag
               self.writeTag(pos,tag)


edittag = editMp3Tag(output.filepath)

edittag.editTitleTag(output.Title)
edittag.editAlbumTag(output.Album)
edittag.editArtistTag(output.Artist)
edittag.editYearTag(output.Year)
edittag.editGenreTag(output.Genre_Code)
edittag.closeFile()


