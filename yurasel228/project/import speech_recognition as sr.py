import speech_recognition as sr
import spotipy
import spotipy.util as util
import os
import sys

#дані доступу до Spotify
SPOTIPY_USERNAME = ''
SPOTIPY_CLIENT_ID = ''
SPOTIPY_CLIENT_SECRET = ''
SPOTIPY_REDIRECT_URI = ''

def voice_assistant():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Скажіть щось...")
        audio = r.listen(source, phrase_time_limit=5)

    try:
        command = r.recognize_google(audio, language="uk-UA,en-US,ru-RU").lower()
        print("Ви сказали: " + command)
        if "відтвори" in command or "play" in command or "играй" in command:
            # отримання токена доступу до Spotify
            token = util.prompt_for_user_token(SPOTIPY_USERNAME, scope='user-read-playback-state,user-modify-playback-state', client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)
            if token:
                # підключення до Spotify API
                sp = spotipy.Spotify(auth=token)
                # визначення назви пісні
                song_name = ""
                if "відтвори" in command:
                    song_name = command.replace("відтвори", "").strip()
                elif "play" in command:
                    song_name = command.replace("play", "").strip()
                elif "играй" in command:
                    song_name = command.replace("играй", "").strip()

                # отримання URI першої знайденої пісні за запитом
                result = sp.search(q=song_name, type='track', limit=1)
                song_uri = result['tracks']['items'][0]['uri']
                # відтворення пісні
                sp.start_playback(uris=[song_uri])
                print("Починаю відтворення пісні: " + result['tracks']['items'][0]['name'])
                sys.exit(0)
            else:
                print("Неможливо отримати токен доступу до Spotify")
                sys.exit(1)

    except sr.UnknownValueError:
        print("не зміг розпізнати вашу команду")
        sys.exit(1)
    except sr.RequestError as e:
        print("Помилка: {0}".format(e))
        sys.exit(1)

if __name__ == '__main__':
    voice_assistant()