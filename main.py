import requests
import json
import time
from discord_webhook import DiscordWebhook, DiscordEmbed
import datetime

def send_webhook(id, image, link, releasetime, color, name, brand, gender, sku):
     webhook_url = 'https://discordapp.com/api/webhooks/670385182242766922/Xd-fxD7f3wUqNFts80QwcZkBGzMl5bqhw4YdszjWRciC2iBK14pVPJyiUidfKGINK3mC'
     hook = DiscordWebhook(url=webhook_url, username="SOLEITARY AIO", avatar_url='https://i.imgur.com/ET9O2Xh.png')
     color=12632256

     embed = DiscordEmbed(
        title = '**New Product Loaded**',
        color=color,
        url='https://twitter.com/SOLEITARY'
       )
     embed.set_footer(text=f'SOLEITARY AIO',icon_url='https://i.imgur.com/ET9O2Xh.png')
     embed.add_embed_field(name='Name', value=f'{name}')
     embed.add_embed_field(name='Brand', value=f'{brand}')
     embed.add_embed_field(name='PID', value=f'{id}', inline=False)
     embed.set_image(url=f'{image}')
     embed.add_embed_field(name='Link', value=f'{link}', inline=False)
     embed.add_embed_field(name='Release Time', value=f'{releasetime}', inline=False)
     embed.add_embed_field(name='Colour', value=f'{color}', inline=False)
     embed.add_embed_field(name='SKU', value=f'{sku}', inline=False)
     hook.add_embed(embed)
     hook.execute()


url = 'https://www.footlocker.co.uk/INTERSHOP/static/WFS/Footlocker-Site/-/Footlocker/en_US/Release-Calendar/Launchcalendar/launchdata/launchcalendar_feed_all.json'

headers = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Referer': '',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest'
}

print('Starting')

items = []

def main():
    while True:
        r = requests.get(url, headers=headers)
        data = json.loads(r.text)
        for x in range(len(data)):
            try:
                id = data[x]['id']
                if id not in items:
                    items.append(id)
                    image = data[x]['image']
                    deeplinks = data[x]['deepLinks']
                    locale = deeplinks[4]['locale']
                    link = deeplinks[4]['link']
                    releasetime = data[x]['releaseDatetime']
                    color = data[x]['colors']
                    name = data[x]['name']
                    brand = data[x]['brand']
                    gender = data[x]['gender']
                    sku = data[x]['manufacturerSku']
                    print(f'Found New Product: {id}')
                    send_webhook(id, image, link, releasetime, color, name, brand, gender, sku)
                    time.sleep(3)
                else:
                    print('No New Items Found')
                    main()
            except KeyError:
                print('Key Error, error with JSON')
            except Exception as e:
                print('Unexpected error: {}'.format(e))

main()

'''
f'Found: {id}, {image}, {locale}, {link},{color},{name},{brand},{gender},{sku}'
'''
