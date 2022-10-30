import sys
from vkapi import VkApiUser
from yaapi import YaDiskUser

VK_TOKEN = 'vk1.a.s6NcFq0gank-k2XT2w5DBVwrUlZe1JkppjGAg_PvMmntJBv2xhykgudznA3q6dUpMfRSOdlnowDO6iPp31qp4R8I4Rxxpxqel8WKb--0QRrCPP0WBR6wlPRmntEWSHSwXTMCKZy3LagJNNaqFK01QMMD_jXvS5rfZxuhgfZf5UWYM8ChOnbSs4DtfA6FVgL9RcHTqZa2lBlfkk7_LjWQ6w'
VK_API_VERSION = '5.131'
YANDEX_DISK_TOKEN = 'y0_AgAAAABWnbrJAADLWwAAAADRCiGlTDR6JPl-S0qL6uTSZ0l_u0Lm39g'

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