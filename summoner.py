import requests

class Summoner:
    def __init__(self, name):
      apikey = '###############################'# API key given from the Riot developer portal
      patchnote = '#########'#live patch note

      #get name for to fetch sumID
      url = 'https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+name+'?api_key='+apikey
      response = requests.get(url).json()

      #get id
      self.sumID = response['id']

      #use sumID to fetch rank data
      url2 = 'https://eun1.api.riotgames.com/lol/league/v4/entries/by-summoner/'+self.sumID+'?api_key='+apikey
      response2 = requests.get(url2).json()
      
      jsonarray = response2[0]

      #soloduo & flex status
      self.queuetype = jsonarray['queueType']
      self.div = jsonarray['tier']
      self.rank  = jsonarray['rank']
      self.points = jsonarray['leaguePoints']
      self.wins = jsonarray['wins']
      self.losses = jsonarray['losses']
      self.winrate = "{:.0f}".format((self.wins/(self.wins+self.losses))*100)
      
      #calculate winrate
      try:
        jsonarray2 = response2[1]
        self.queuetype2 = jsonarray2['queueType']
        self.div2 = jsonarray2['tier']
        self.rank2  = jsonarray2['rank']
        self.points2 = jsonarray2['leaguePoints']
        self.wins2 = jsonarray2['wins']
        self.losses2 = jsonarray2['losses']
        self.winrate2 = "{:.0f}".format((self.wins2/(self.wins2+self.losses2))*100)
      except:
        self.queuetype2 = 'Unranked'
        self.div2 = 'None'
        self.rank2  = 'None'
        self.points2 = 'None'
        self.wins2 = 'None'
        self.losses2 = 'None'
        self.winrate2 = 'None'
       
      #get top 3 champion mastery
      url = 'https://eun1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/'+self.sumID+'?api_key='+apikey
      response = requests.get(url).json()
      
      #Top 3 champions sorted by mastery
      chm1 = response[0]
      chm2 = response[1]
      chm3 = response[2]

      #get champion by id
      def set_ch(id):
       url = 'http://ddragon.leagueoflegends.com/cdn/'+patchnote+'/data/en_US/champion.json'
       response = requests.get(url).json()

       champions = response['data']

       for champion in champions:
         chd = champions[''+champion+'']
         if(str(id) == chd['key']):
            return chd['id']
            break

      self.ch1 = set_ch(int(chm1['championId']))
      self.ch2 = set_ch(int(chm2['championId']))
      self.ch3 = set_ch(int(chm3['championId']))
    
    
    