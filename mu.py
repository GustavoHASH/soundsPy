import os
from pytube import YouTube

# URL do vídeo que será baixado
url = "https://www.youtube.com/watch?v=CJ2m3UcLBa0"

# Cria um objeto da classe YouTube com a URL do vídeo
yt = YouTube(url)

# Filtra as streams que contém apenas áudio e seleciona a com a maior taxa de bits
stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()

# Cria a pasta "download" caso ela ainda não exista
if not os.path.exists('download'):
    os.makedirs('download')

# Baixa o áudio do vídeo para a pasta "download"
stream.download(output_path='download')
