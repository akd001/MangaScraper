import os.path
import urllib
import urllib2
import urlparse
import ConfigParser
from bs4 import BeautifulSoup

mangaName = "naruto"			# enter the part in []: http://www.mangapanda.com/[naruto]/618/2
saveMangaFolder = "/home/username/Desktop/MangaCrawler/Naruto"	#Save path on your system
mangaChapter = 700						#Last chapter to be crawled

def imgLink (mangaChapter, mangaSheet):
	mangaPage = "http://www.mangapanda.com/" + mangaName + "/" + str(mangaChapter) + "/" + str(mangaSheet)
	htmlPage = BeautifulSoup (urllib.urlopen(mangaPage).read())
	if (htmlPage.body.h1.string == "404 Not Found"):
		print "Next Chapter!"
		return None
	divImage1 = htmlPage.body.table.img['src']
	return urlparse.urljoin(mangaPage, divImage1)

def imgSave (imageLink, mangaChapter, mangaSheet):
	imageData = urllib2.urlopen(imageLink).read()
	savePath = os.path.join(saveMangaFolder, str (mangaChapter) + "-" + str(mangaSheet) + ".jpg")
	output = open(savePath, 'wb')
	output.write(imageData)
	output.close()

# To download all the chapters, mention the last chapter number of the manga [mangaChapter (integer)]
for j in range(1, mangaChapter):
	for i in range(1, 100):
		imageLink = imgLink(j, i)
		if imageLink != None:
			print imageLink
			imgSave(imageLink, j, i)
		else:
			break


#To download a single chapter, mention the mangaChapter (integer) in the beginning
# for i in range(1, 100):
# 		imageLink = imgLink(mangaChapter, i)
# 		if imageLink != None:
# 			print imageLink
# 			imgSave(imageLink, mangaChapter, i)
# 		else:
# 			break

print "All done! :)"
