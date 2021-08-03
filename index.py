from flask import redirect, render_template, Flask, request, url_for
import re,requests

app = Flask(__name__)


CONFIG_SEIGNEUR ={
    'artist' : 'DEEPBLU.',
    'title'  : 'Seigneur',
    'icon'   : 'https://images.genius.com/455d88fd1f1071cb208a0979a7f6a0d9.1000x1000x1.jpg',
    'description' : "Seigneur : DEEPBLU.'s new Single. Out on All Platforms.",
    'website' : 'http://blu.intellx.co.in//seigneur'
}

CONFIG_MM ={
    'artist' : 'DEEPBLU.',
    'title'  : 'The Zone of Methodical Madness between Your Soul and I',
    'icon'   : 'https://images.genius.com/5b6728f9318ef93de2e4652f525b0cb0.1000x1000x1.jpg',
    'description' : "The Zone of Methodical Madness between Your Soul and I by DEEPBLU. on all platforms.",
    'website' : 'http://blu.intellx.co.in//mm'
}

CONFIG_MMSR ={
    'artist' : 'DEEPBLU.',
    'title'  : 'The Zone of Methodical Madness between Your Soul and I (Slowed+Reverb)',
    'icon'   : 'https://m.media-amazon.com/images/I/61BjlTIceiL._SS500_.jpg',
    'description' : "The Zone of Methodical Madness between Your Soul and I (Slowed+Reverb) by DEEPBLU. on all platforms.",
    'website' : 'http://blu.intellx.co.in//mm/snr'
}

CONFIG_MAIN ={
    'artist' : 'DEEPBLU.',
    'title'  : 'Musical Artist',
    'icon'   : 'https://i.imgur.com/jDEfZtp.jpg',
    'description' : "DEEPBLU. : A Musical Artist on All Streaming Platforms",
    'website' : 'http://blu.intellx.co.in//'
}

CONFIG_SOCIALS ={
    'artist' : 'DEEPBLU.',
    'title'  : 'Social Media',
    'icon'   : 'https://i.imgur.com/jDEfZtp.jpg',
    'description' : "DEEPBLU. : A Musical Artist on All Social Media",
    'website' : 'http://blu.intellx.co.in//'
}

CONFIG_WW ={
    'artist' : 'Saaya and DEEPBLU.',
    'title'  : 'Wicked World',
    'icon'   : 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/f945765d-0c52-449c-920c-38cafa896f17/db72rau-f5a5a974-3488-4361-8336-dacc1cb29ff2.jpg/v1/fill/w_875,h_913,q_70,strp/black_rain_by_blackbirdmotel_db72rau-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3siaGVpZ2h0IjoiPD0xMDY4IiwicGF0aCI6IlwvZlwvZjk0NTc2NWQtMGM1Mi00NDljLTkyMGMtMzhjYWZhODk2ZjE3XC9kYjcycmF1LWY1YTVhOTc0LTM0ODgtNDM2MS04MzM2LWRhY2MxY2IyOWZmMi5qcGciLCJ3aWR0aCI6Ijw9MTAyNCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.noxPMxo14PrngvHFH-AykIjqrTl5oUKFz0MP5mbWqHU',
    'description' : "Wicked World : Saaya's new Single. Out on All Platforms.",
    'website' : 'http://blu.intellx.co.in//ww'
}

CONFIG_INTRO ={
    'artist' : 'DEEPBLU. ft.J3ROM3, Abi',
    'title'  : 'Introspection',
    'icon'   : 'https://images.genius.com/670fbf396cafb2c7f56e565c2d02cd6e.1000x1000x1.jpg',
    'description' : "Introspection : DEEPBLU.'s new Single. Out on All Platforms.",
    'website' : 'http://blu.intellx.co.in//introspection'
}


@app.route('/')
def home():
  mob="false"
  browser = request.user_agent.browser
  version = request.user_agent.version and int(request.user_agent.version.split('.')[0])
  platform = request.user_agent.platform
  uas = request.user_agent.string
  if browser and version:
    if (browser == 'msie' and version < 9) \
    or (browser == 'firefox' and version < 4) \
    or (platform == 'android' and version < 534) \
    or (platform == 'iphone' and version < 7000) \
    or ((platform == 'macos' or platform == 'windows') and browser == 'safari' and not re.search('Mobile', uas) and version < 534) \
    or (re.search('iPad', uas) and browser == 'safari' and version < 7000) \
    or (platform == 'windows' and re.search('Windows Phone OS', uas)) \
    or (browser == 'opera') \
    or (re.search('BlackBerry', uas)):
        mob="true"
  metass = render_template('meta.html',config=CONFIG_MAIN,mis=1)
  return render_template("index.html",metas=metass)

@app.route('/social')
def social():
    metass = render_template('meta.html',config=CONFIG_SOCIALS,mis=0.5)
    return render_template("mobile.html",metas=metass)

@app.route('/data',methods=['POST','GET'])
def datanalyse():
    j = {'data' : dict(request.form)}
    data = (requests.get(f'https://ipapi.co/{j["data"]["ip"]}/json/')).json()
    print(requests.post('https://deepblu.pythonanywhere.com/data', data = data).content)
    return 'OK'

@app.route('/google')
def findmeongoogle():
    return redirect('https://g.co/kgs/Y7kJKo')

'''
ERA 1 : THE ZONE OF METHODICAL MADNESS
'''
@app.route('/mm/snr')
def snr():
    metas = render_template('meta.html',config=CONFIG_MMSR,mis=0.5)
    return render_template("snr.html",metas=metas)

@app.route('/newmania')
def newmania():
    return redirect(url_for('youtube'))

@app.route('/mm')
def mmadness():
    metas = render_template('meta.html',config=CONFIG_MM,mis=0.5)
    return render_template("mmadness.html",metas=metas)

@app.route('/mm/youtube')
def youtube():
    return redirect('https://www.youtube.com/playlist?list=OLAK5uy_mP4ADdDD6mdKTsPP4fY79ELsnG-CEb7aw')

@app.route('/mm/spotify')
def spotify():
    return redirect('https://open.spotify.com/album/52nexCl7gJMzSx0lTBLBD0')

@app.route('/mm/applemusic')
def applemusic():
    return redirect('https://music.apple.com/us/album/the-zone-of-methodical-madness-between-your-soul-and-i/1529448313')

@app.route('/mm/youtubemusic')
def youtubemusic():
    return redirect('https://music.youtube.com/playlist?list=OLAK5uy_mP4ADdDD6mdKTsPP4fY79ELsnG-CEb7aw')

@app.route('/mm/amazon')
def amazon():
    return redirect('https://www.amazon.com/Zone-Methodical-Madness-between-Your/dp/B08GSRVHXZ/ref=sr_1_1?dchild=1&keywords=the+zone+of+methodical+madness+between+your+soul+and+i&qid=1600750004&s=dmusic&sr=1-1')

@app.route('/mm/anghami')
def anghami():
    return redirect('https://play.anghami.com/album/1014849352')

@app.route('/mm/tidal')
def tidal():
    return redirect('https://listen.tidal.com/album/153437766')

@app.route('/mm/deezer')
def deezer():
    return redirect('https://www.deezer.com/us/album/169775772')

@app.route('/thezone')
def thezone():
    return '''
    <html> <head> <link rel='icon' href='https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/f945765d-0c52-449c-920c-38cafa896f17/db72rau-f5a5a974-3488-4361-8336-dacc1cb29ff2.jpg/v1/fill/w_875,h_913,q_70,strp/black_rain_by_blackbirdmotel_db72rau-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3siaGVpZ2h0IjoiPD0xMDY4IiwicGF0aCI6IlwvZlwvZjk0NTc2NWQtMGM1Mi00NDljLTkyMGMtMzhjYWZhODk2ZjE3XC9kYjcycmF1LWY1YTVhOTc0LTM0ODgtNDM2MS04MzM2LWRhY2MxY2IyOWZmMi5qcGciLCJ3aWR0aCI6Ijw9MTAyNCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.noxPMxo14PrngvHFH-AykIjqrTl5oUKFz0MP5mbWqHU' type='image/jpeg'/ > <meta charset="UTF-8" /> <meta name="viewport" content="width=device-width, initial-scale=1.0" /> <title>DEEPBLU. &mdash; THE ZONE OF METHODICAL MADNESS BETWEEN YOUR SOUL I</title> </head> <body style="background-color:black;overflow:hidden;"> <iframe width="100%" height="100%" style="width:100%;height:100%; border: none;" src="https://harbor.naker.io/story/5f5373a7498f6c00049ea19c/" frameBorder="0" frameborder="0" hspace="0" vspace="0" marginheight="0" marginwidth="0"></iframe> </body> </html>
    '''
@app.route('/mm/tracklist')
def tracklist():
    return redirect("https://genius.com/albums/Deepblu/The-zone-of-methodical-madness-between-your-soul-and-i")

@app.route('/mm/buy')
def purchase():
    return redirect(url_for('amazon'))

'''
ERA 2 (PART 1) : SEIGNEUR
'''

@app.route('/seigneur')
def mainseigneur():
    metass = render_template('meta.html',config=CONFIG_SEIGNEUR,mis=0.5)
    return render_template("seigneur.html",metas=metass)

@app.route('/seigneur/snr')
def snrseigneur():
    metas = render_template('meta.html',config=CONFIG_MMSR,mis=0.5)
    return render_template("snr.html",metas=metas)

@app.route('/seigneur/youtube')
def youtubeseigneur():
    return redirect('https://www.youtube.com/watch?v=BhFmNao5Txo')

@app.route('/seigneur/spotify')
def spotifyseigneur():
    return redirect('https://open.spotify.com/album/2vT0mpdMlf8OpLx2Cw7ZJe')

@app.route('/seigneur/applemusic')
def applemusicseigneur():
    return redirect('https://music.apple.com/us/album/seigneur/1543721206?i=1543721207')

@app.route('/seigneur/youtubemusic')
def youtubemusicseigneur():
    return redirect('https://music.youtube.com/playlist?list=OLAK5uy_lEdIeJFi_yDHbVgP8gX4Rp-nbCli2kR84')

@app.route('/seigneur/amazon')
def amazonseigneur():
    return redirect('https://www.amazon.com/Seigneur/dp/B08PVZJMJW/ref=sr_1_4?dchild=1&keywords=DEEPBLU.&qid=1616543008&s=dmusic&search-type=ss&sr=1-4')

@app.route('/seigneur/anghami')
def anghamiseigneur():
    return redirect('https://play.anghami.com/song/93796098')

@app.route('/seigneur/tidal')
def tidalseigneur():
    return redirect('https://listen.tidal.com/album/165279945')

@app.route('/seigneur/deezer')
def deezerseigneur():
    return redirect('https://www.deezer.com/us/album/191521072')

@app.route('/seigneur/tracklist')
def tracklistseigneur():
    return redirect("https://genius.com/Deepblu-seigneur-lyrics")



'''
ERA 2 (PART 2) : WICKED WORLD
'''

@app.route('/ww')
def mainww():
    try:
        ip=dict(request.headers)['X-Forwarded-For']
    except:
        ip=dict(request.headers).get('X-Real-Ip')
    data = (requests.get(f'https://ipapi.co/{str(ip)}/json/')).json()
    print(requests.post('https://deepblu.pythonanywhere.com/data', data = data).content)
    metass = render_template('meta.html',config=CONFIG_WW,mis=0.5)
    return render_template("ww.html",metas=metass)

@app.route('/ww/snr')
def snrww():
    return redirect("http://blu.intellx.co.in//youtube")

@app.route('/ww/youtube')
def youtubeww():
    return redirect('https://www.youtube.com/watch?v=hhWhtkWuZbk&list=PL2UBu4Yv1_DMQfWCu3rDYP7KTJTGFlCz4&index=4&pbjreload=101')

@app.route('/ww/spotify')
def spotifyww():
    return redirect('https://open.spotify.com/album/1DA1fNtKXRKlkS9VkNgGRY')

@app.route('/ww/applemusic')
def applemusicww():
    return redirect('https://music.apple.com/us/album/wicked-world/1558368277?i=1558368278')

@app.route('/ww/youtubemusic')
def youtubemusicww():
    return redirect('https://music.youtube.com/watch?v=PD0FakwZI4M&list=RDAMVMPD0FakwZI4M')

@app.route('/ww/amazon')
def amazonww():
    return redirect('https://www.amazon.com/Wicked-World-SAAYA/dp/B08W8NDZX7/ref=sr_1_2?dchild=1&keywords=DEEPBLU.&qid=1613002900&s=dmusic&search-type=ss&sr=1-2')

@app.route('/ww/anghami')
def anghamiww():
    return redirect('https://play.anghami.com/song/99151335')

@app.route('/ww/tidal')
def tidalww():
    return redirect(url_for('mainww'))

@app.route('/ww/deezer')
def deezerww():
    return redirect(url_for('mainww'))

@app.route('/ww/whatsapp')
def whatsappshareww():
    return redirect('https://wa.me/?text=Listen%20to%20DEEPBLU.%20on%20all%20platforms%20at%20http://blu.intellx.co.in//')

@app.route('/ww/twitter')
def twittershareww():
    return redirect('https://twitter.com/intent/tweet?url=Listen%20to%20Saaya%27s%20New%20Single%20%22Wicked%20World%22%20(prod.%20DEEPBLU.)%20on%20all%20platforms%20at%20http://blu.intellx.co.in//ww')

@app.route('/ww/tracklist')
def tracklistww():
    return redirect("https://genius.com/Saaya-wicked-world-lyrics")


@app.route('/ww/genius')
def geniustracklist():
    return redirect(url_for('tracklistww'))

@app.route('/ww/buy')
def purchaseww():
    return redirect(url_for('amazonww'))

@app.route('/ww/listen')
def listen():
    return redirect(url_for('mainww'))


'''
ERA 2 (PART 3) : INTROSPECTION
'''

@app.route('/introspection')
def mainintro():
    try:
        ip=dict(request.headers)['X-Forwarded-For']
    except:
        ip=dict(request.headers).get('X-Real-Ip')
    data = (requests.get(f'https://ipapi.co/{str(ip)}/json/')).json()
    print(requests.post('https://deepblu.pythonanywhere.com/data', data = data).content)
    metass = render_template('meta.html',config=CONFIG_INTRO,mis=0.5)
    return render_template("intro.html",metas=metass)

@app.route('/youtube')
def youtubeintro():
    return redirect('https://www.youtube.com/watch?v=ynDWHUKBX7U&list=PL2UBu4Yv1_DMQfWCu3rDYP7KTJTGFlCz4&index=6')

@app.route('/spotify')
def spotifyintro():
    return redirect('https://open.spotify.com/album/6Wes3vOMDvIdKbQ2vOg0Am')

@app.route('/amazon')
def amazonintro():
    return redirect('https://www.amazon.com/Introspection-feat-J3ROM3-DEEPBLU/dp/B091BNJBKY/ref=sr_1_1?dchild=1&keywords=DEEPBLU.&qid=1617610281&s=dmusic&sr=1-1')

@app.route('/anghami')
def anghamiintro():
    return redirect('https://play.anghami.com/song/106311847')

@app.route('/genius')
def geniusintro():
    return redirect("https://genius.com/Deepblu-introspection-lyrics")



'''
SUBSCRIPTION
'''

@app.route('/sw')
def saveworld():
    return redirect(url_for('subscribe'))

@app.route('/subscribe')
def subscribe():
    metass = render_template('meta.html',config=CONFIG_WW,mis=1)
    return render_template("subscribe.html",metas=metass)

@app.route('/subscribe/submit',methods=['POST'])
def subscriptionmade():
  mob="false"
  browser = request.user_agent.browser
  version = request.user_agent.version and int(request.user_agent.version.split('.')[0])
  platform = request.user_agent.platform
  uas = request.user_agent.string
  if browser and version:
    if (browser == 'msie' and version < 9) \
    or (browser == 'firefox' and version < 4) \
    or (platform == 'android' and version < 534) \
    or (platform == 'iphone' and version < 7000) \
    or ((platform == 'macos' or platform == 'windows') and browser == 'safari' and not re.search('Mobile', uas) and version < 534) \
    or (re.search('iPad', uas) and browser == 'safari' and version < 7000) \
    or (platform == 'windows' and re.search('Windows Phone OS', uas)) \
    or (browser == 'opera') \
    or (re.search('BlackBerry', uas)):
        mob="true"
  try:
        ip=dict(request.headers)['X-Forwarded-For']
  except:
        ip=dict(request.headers).get('X-Real-Ip')
  ipdataa = (requests.get(f'https://ipapi.co/{ip}/json/')).json()
  data = {'name':request.form.get('name'),
          'email':request.form.get('email'),
          'instagram':request.form.get('instagram'),
          'mobile':mob,
          'ip':ip,
          'ip-data':str(ipdataa).replace("'",'"').replace('True','"True"').replace('False','"False"').replace('None','"None"')}
  print(requests.post('http://deepblusavee.eu.pythonanywhere.com/', data = data).content)
  return redirect(url_for('home'))


@app.route('/xobeatz')
def xobeatz():
    return redirect("https://youtu.be/ARPEG0UH6zw")

@app.route('/meet')
def gmeet():
    return redirect("https://meet.google.com/vmm-ibgc-hbh")

@app.errorhandler(404)
def page_not_found(e):
    metass = render_template('meta.html',config=CONFIG_MAIN,mis=0.8)
    return render_template("404.html",metas=metass)



if __name__=="__main__":
    app.run(
        port=5000,
        host='0.0.0.0',
        use_evalex=True,
        threaded=True,
        passthrough_errors=False
        )