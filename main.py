import sys
from vkapi import VkApiUser
from yaapi import YaDiskUser

VK_TOKEN = ''
VK_API_VERSION = '5.131'
YANDEX_DISK_TOKEN = ''

vk_user_id = input('Введите ID пользователя Вконтакте: ')
if not vk_user_id.isdecimal():
    print("Ошибка! Не корректный ввод!")
    sys.exit()
else:
    vk_user_id = int(vk_user_id)
    vkuser = VkApiUser(VK_TOKEN, VK_API_VERSION)
    album_id = vkuser.get_albums(vk_user_id)
    photos_count = input('Введите число фотографий, которые вы хотите сохранить на Яндекс.Диск: ')
    if not photos_count.isdecimal():
        print("Не корректный ввод! Будет сохранено 5 фотографий.")
        vkuser = VkApiUser(VK_TOKEN, VK_API_VERSION)
        urls_dict = vkuser.get_photos(vk_user_id, album_id)
        yadiskuser = YaDiskUser(YANDEX_DISK_TOKEN)
        yadiskuser.upload(urls_dict, vk_user_id)
    else:
        photos_count = int(photos_count)
        vkuser = VkApiUser(VK_TOKEN, VK_API_VERSION)
        urls_dict = vkuser.get_photos(vk_user_id, album_id, photos_count)
        yadiskuser = YaDiskUser(YANDEX_DISK_TOKEN)
        yadiskuser.upload(urls_dict, vk_user_id)