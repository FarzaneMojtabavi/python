from moviepy import editor
video=editor.VideoFileClip('heartClubMusic.mp4')
print('__________________Start__ _ _ ...')
video.audio.write_audiofile('heartClubMusic.mp3')
print('__________________End__ _ _ ...')
video.close()
