import urllib.request
import html

def readWebsite(url):
    mybytes = url.read() #read html file as bytes
    mystr = mybytes.decode("utf-8") #decode bytes to a string
    mystr = html.unescape(mystr) #for special characters
    return mystr

def getSong(mystr):
    position = mystr.find('<div class="title">')  #looking for title html tag
    positionA = mystr.find('<div class="artist">')
    count = 1
    while position != -1 and count <= 10: #-1 returned if html tag not found
        start = mystr.find(">",position+len('<div class="title">')) # find first ">" after html title tag
        stop = mystr.find("<", start)
        startA = mystr.find(">",positionA+len('<div class="artist">')) # find first ">" after html title tag
        stopA = mystr.find("<", startA)       
        print(f"{count}.{mystr[start+1:stop]} by {mystr[startA+1:stopA]}")
        position = mystr.find('<div class="title">', stop)
        positionA = mystr.find('<div class="artist">', stopA)  
        count += 1

def getArtist(mystr):
    position = mystr.find('<div class="artist">')  #looking for title html tag
    count = 1
    while position != -1 and count <= 10: #-1 returned if html tag not found
        start = mystr.find(">",position+len('<div class="artist">')) # find first ">" after html title tag
        stop = mystr.find("<", start)
        print(f"{count}.{mystr[start+1:stop]}")
        position = mystr.find('<div class="artist">', stop)          
        count += 1
        
  
    
if __name__ == "__main__":
    fp = urllib.request.urlopen("https://www.officialcharts.com/charts/singles-chart/")
    web_str = readWebsite(fp)
    getSong(web_str)

    
        
    
