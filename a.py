import youtube_dl

# ダウンロードしたい動画のURLを入力
URL_movie = "https://www.youtube.com/watch?v=U_rWZK_8vUY"
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([URL_movie])
