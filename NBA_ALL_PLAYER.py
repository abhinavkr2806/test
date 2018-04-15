from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import pandas as pd
driver=webdriver.PhantomJS()

def stars(player_url):
    driver.get(player_url)
    content=driver.page_source
    soup=BeautifulSoup(content,"html.parser")
    First_Name=soup.find("p",{"class":"player-summary__first-name"}).text
    Last_Name=soup.find("p",{"class":"player-summary__last-name"}).text
    Team_Name=soup.find("span",{"class":"player-summary__team-name"}).text
    Height_block=soup.find("a",{"ng-if":"availableStats.current","href":"/players/bio/?sort=PLAYER_HEIGHT_INCHES&dir=1&CF=PLAYER_HEIGHT_INCHES*E*"})
    try:
        Height=Height_block.find("span").text
    except:
        Height="None"
    print(First_Name,Last_Name,Team_Name,Height)
    return(First_Name,Last_Name,Team_Name,Height)


Base_Url="https://stats.nba.com/players/list/"
driver.get("https://stats.nba.com/players/list/")
content=driver.page_source
soup=BeautifulSoup(content,"html.parser")
Section=soup.find_all("section",{"class":"row collapse players-list__section"})
list=[]
for block in Section:
    players=block.find_all("a")
    for player in players:
        link=player["href"]
        url="https://stats.nba.com"
        main_link=url+link
        #print(main_link)
        First_Name,Last_Name,Team_Name,Height=stars(main_link)
        y={"First_Name":First_Name,"Last_Name":Last_Name,"Team_Name":Team_Name,"Height":Height}
        list.append(y)
Data=pd.DataFrame(list)
Data.to_csv("All_Player_Details")