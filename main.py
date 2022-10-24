from vk_api import VkApi, audio, exceptions, AuthError
from tools import *
from config import *


def auth_handler() -> tuple[str, bool]:
    key = input('Enter secret key from message: ')
    remember_device = False
    return key, remember_device


def main() -> None:
    session = VkApi(me_login, me_password, auth_handler=auth_handler)

    try:
        session.auth()
    except AuthError as error:
        print('Error', error)

    vk_music = audio.VkAudio(session)

    now = get_now()
    count = 1
    
    for track in vk_music.get(owner_id=me_id):
        try:
            write_txt('VK music', 'a', now, count, f'{track["title"]} - {track["artist"]}')
            write_csv('VK music', 'a', now, count, track['title'], track['artist'])
        except Exception as ex:
            print('Error', count, ex)
            write_txt('VK music', 'a', now, count, 'Error')
            write_csv('VK music', 'a', now, count, 'Error', 'Error')
        count += 1
        

if __name__ == '__main__':
    main()
