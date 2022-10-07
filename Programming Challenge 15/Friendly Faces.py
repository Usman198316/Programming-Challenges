import csv
from pathlib import Path
import urllib.request
import html

csv_file = Path("south.csv")


def read_csv(csv_file):
    
    csv_contents = []
    with open(csv_file) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            csv_contents.append(row)
    return csv_contents
    
    
def read_html(html_file):

    with open (html_file) as htmlfile:
        html = htmlfile.read()
    print(html)
    return html
        
        
            
def process(csv, html):
    Lposition
    Hposition = html.find('<h2 class="el__heading">')
    Nposition = html.find('')
    
    count = 1
    

    
    ## replace link1...link5 in html with corresponding values fronm csv
    ## Similarly do for initials1...intitials5 and name1...name5

def write_html(path, html):
    print("World")
    ## write the new contents into an html file


if __name__ == "__main__":
    csv = read_csv("south.csv")
    html = read_html("south.html")
    html = process(csv, html)
    write_html("south_final.html", html)
