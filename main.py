import requests, random

token = ''
urls = {
'idk': 'message endpoint here',
}

print('where do u wanna vamp translate?\n')
for key in urls.keys():
    print(f'[{list(urls.keys()).index(key)}]: {key}')

url = urls[list(urls.keys())[int(input('\n[*]: '))]]

def vamp_translate():
    translated = ''
    capped=''
    totrans = input('[msg]: ')
    symbols=list('!*+^!*+^')
    replace = {
    'this': ['dis','dis'],
    'that': ['dat','dat'],
    'you': ['yu', 'uu'],
    'fuck': ['fukk','fukk'],
    'hoe': ['ho','ho'],
    'c': ['k', 'x', 'c', 'c', 'c'],
    'e': ['3', 'e', 'e'],
    'o': ['0', 'o','o'],
    ' a ': [' ah '],
    'i': ['i'],
    'kill':['murk','murk'],
    'nigga': ['nikka','nikka'],
    'niggas':['niggaz','niggaz']}
    phrases = [' SLATT !', ' +@MEH', ' ! SRT8 !', ' StOp BrEaThInG !*', 'YUNGX4NH03']

    translated = totrans
    for key in replace.keys():
        translated=translated.replace(key, replace[key][random.randint(0,len(replace[key])-1)])
    translated=translated+''.join([symbols[random.randint(0,7)] for _ in range(random.randint(2,4))])
    translated = translated + phrases[random.randint(0,4)]
    for _ in translated:
        capped=capped+[_.lower(),_.capitalize(),_.lower(),_.capitalize(),_.lower(),_.lower()][random.randint(0,5)]
    requests.post(url, headers={'Authorization':token},json={"content":capped})
    vamp_translate()

vamp_translate()
