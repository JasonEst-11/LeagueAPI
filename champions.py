import requests

class Champions:
    def __init__(self, name):   
     patchnote = '#########'#live patch note
     url = 'http://ddragon.leagueoflegends.com/cdn/'+patchnote+'/data/en_US/champion/'+name+'.json'
     response = requests.get(url).json()

     data = response['data'][name]['spells']
     
     #q
     self.qname = data[0]['name']
     self.qcd = data[0]['cooldown']
     self.qmana = data[0]['cost']
     #w
     self.wname = data[1]['name']
     self.wcd = data[1]['cooldown']
     self.wmana = data[1]['cost']
     #e
     self.ename = data[2]['name']
     self.ecd = data[2]['cooldown']
     self.emana = data[2]['cost']
     #r
     self.rname = data[3]['name']
     self.rcd = data[3]['cooldown']
     self.rmana = data[3]['cost']
