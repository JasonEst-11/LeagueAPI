import summoner
import champions
import requests
from tabulate import tabulate

name = "#######"#Summoner name 
# Get summoner info by name
try:
   s1 = summoner.Summoner(name)
   #tabulate format for solo & flex
   header = ['Tier','Rank','Points','Wins','Losses','Winrate']
   mydata = [(s1.div,s1.rank,s1.points,s1.wins,s1.losses,s1.winrate)]
   mydata2 = [(s1.div2,s1.rank2,s1.points2,s1.wins2,s1.losses2,s1.winrate2)]
   print(f'{name} \n\n**{s1.queuetype}**\n{tabulate(mydata, headers=header)}\n\n**{s1.queuetype2}**\n{tabulate(mydata2, headers=header)}\n\n**Top 3 Champions**\n\n{s1.ch1}\t{s1.ch2}\t{s1.ch3}')
   print(s1.sumID)
except:
    print('No Summoner found please try again')

#get cooldown by champion name
champion = "######"#champion name
try:
    chcd = champions.Champions(champion)
    print(f'{champion} \n\nQ: {chcd.qname}\n{chcd.qcd}\n{chcd.qmana}\n\nW: {chcd.wname}\n{chcd.wcd}\n{chcd.wmana}\n\nE: {chcd.ename}\n{chcd.ecd}\n{chcd.emana}\n\nR: {chcd.rname}\n{chcd.rcd}\n{chcd.rmana}')
except:
    print('Champion not found please try again')

#get items
url = 'http://ddragon.leagueoflegends.com/cdn/'+'insert patch note'+'/data/en_US/item.json'
response = requests.get(url).json()
data = response['data']
for x in data:
  print('http://ddragon.leagueoflegends.com/cdn/11.24.413.2485/img/item/'+x+'.png')
    
     