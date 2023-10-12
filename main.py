from pytube import YouTube, Playlist
import segno
import os
import sys
from pathlib import Path

def download_mp4_videos(url: str, outpath: str = "./downloads"):

    yt = YouTube(url)

    yt.streams.filter(file_extension="mp4").get_highest_resolution().download(outpath)

def dw_music(url: str, outpath: str = "./downloads"):
  yt = YouTube(url)
  yt.streams.filter(only_audio=True).first().download(outpath)

def dw_playlist(url: str, outpath: str = "./downloads"):
  playlist = Playlist(url)
  for video in playlist:
    video.streams.filter(only_audio=True).first().download(outpath)

def qrcode(url,name,output="./qrcodes/"):
  try:
      os.makedirs(output)
  except FileExistsError:
      # directory already exists
      pass
  qrcode = segno.make_qr(url)
  qrcode.save(output+name, scale=50)

if __name__ == "__main__":
    # download_mp4_videos("https://www.youtube.com/shorts/QKKvMx_7gdA")
    # dw_music("https://youtu.be/R95ILhksGt8?list=RDGMEMQ1dJ7wXfLlqCjwV0xfSNbAVMR95ILhksGt8")
    # print(dir(Playlist))
    # print(dir(YouTube))
    qrcode("https://youtu.be/bcE6nt7X63A","AA435.png")
    qrcode("https://youtu.be/_hINln5YgBE","WT571.png")
    qrcode("https://youtu.be/rPh7bAlPf5c","AA268.png")
    qrcode("https://youtu.be/ml0rG3GF3ho","AA426 - AA428.png")
    qrcode("https://youtu.be/g5f4Dlaquqc","AA436.png")