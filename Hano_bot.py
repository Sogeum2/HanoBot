import discord
import os

from selenium import webdriver

client = discord.Client()

driver_options = webdriver.ChromeOptions()
driver_options.add_argument('headless')
driver_options.add_argument('--disable-gpu')
driver_options.add_argument('lang=ko_KR')

driver = webdriver.Chrome('/app/.chromedriver/bin/chromedriver.exe', chrome_options=driver_options)
driver.get('https://archeage.xlgames.com/play/worldinfo/EANNA/');

arche_point = "20개"

@client.event
async def on_ready():

    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):

    global driver
    global driver_options
    global arche_point
    if message.content.startswith('?test'):
        await message.channel.send("test")
    if message.content.startswith('?채권'):
        temp = []
        for x in range(1, 5):
            if x > 1:
                temp.append(' ')
            search_box = driver.find_element_by_xpath('//*[@id=\"container-common\"]/div/div/div/div[8]/table[1]/tbody/tr[' + str(x) + ']/th')
            temp.append(search_box.text)
            for y in range(1, 3):
                for z in range(1, 5):
                    try:
                        search_box = driver.find_element_by_xpath("//*[@id=\"container-common\"]/div/div/div/div[8]/table["+ str(y) + "]/tbody/tr[" + str(x) + "]/td/ul/li[" + str(z) + "]")
                        if arche_point in search_box.text:
                            temp.append(search_box.text)
                    except:
                        print('x')

        await message.channel.send("\n".join(temp))
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
