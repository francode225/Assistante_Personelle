from googleapiclient.discovery import build
#youtube = build('youtube', 'v3', developerKey='AIzaSyCpjnyVm182r92QoqF3YFvta3A0jfnkykE')
""" def rechercher_video(titre):
    req = youtube.search().list(q=titre, part='id,snippet', maxResults=1)
    res = req.execute()
    video_id = res['items'][0]['id']['videoId']
    return f"https://www.youtube.com/watch?v={video_id}" """