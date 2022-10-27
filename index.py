import youtube_dl as yt
import os

print('\n\n============YOUTUBE DOWNLOADER============\n\n')

print('Quantidade de items que deseja baixar:\n\n1 - Apenas 1\n\n2 - Mais de dois\n\n')

choice = input('[ESCOLHA]: ')

# print('\n\nFormato no qual deseja baixar (não funcionando ainda):\n\n1 - MP3\n\n2 - MP4\n\n')

# whichFormat = input('[FORMATO]: ')
# downloadFormat = ''

# if whichFormat == '1':
#     downloadFormat = 'mp3'
# else:
#     downloadFormat = 'mp4'

if choice == '1':
    print('\n\nInsira o link\n\nExemplo:\n\nhttps://youtube.com/\n')
    link = input('[LINK]: ')
    with yt.YoutubeDL() as ydl:
        ydl.download([link])
else:
    print('Insira os links\n\nExemplo:\n\nlink1,link2,link3,link4...\n')
    links = input('[INPUT]: ')
    if ',' not in links:
        print('Use vírgula nos separadores do link')
        os._exit(os.X_OK)
    with yt.YoutubeDL() as ydl:
        ydl.download(links.split(','))


