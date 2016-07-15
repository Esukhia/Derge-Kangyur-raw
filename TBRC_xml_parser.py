from bs4 import BeautifulSoup as Soup
import re
import os

os.chdir('/media/drupchen/42DE16ECDE16D7CD/Users/Hélios/Documents/eTexts-ALL-TEI-20150112/db/eTextsChunked/Various')

for Folder in os.listdir('.'):
    if not Folder.startswith('_'):
        print(Folder)
        for File in os.listdir(Folder):
            if not File.startswith('_'):
                print('\t\t', File)
                for Fich in os.listdir(Folder+'/'+File):
                    if not Fich.startswith('_'):
                        with open(Folder+'/'+File+'/'+Fich, 'r', -1, 'utf-8-sig') as f:
                            volume = f.read()
                        soup = Soup(volume, 'lxml')
                        output = ''
                        for page in soup.find_all('tei:p'):
                            text = re.sub(r'\<[^>]+\>', r'', str(page))
                            output += text + '\n'
                        with open('../txt/'+'{}.txt'.format(File), 'w', -1, 'utf-8-sig') as f:
                            f.write\
                                (output)