""" Работа со звуком """

import pygame
from os import path
from .constants import *
from .resource_path import *


def get_audio_path(name: str):
    return resource_path(path.join('resources', 'audio', name))


# Файлы со звуком
audio = {
    'music': get_audio_path('music.mp3'),
    'enemy_laser': get_audio_path('enemy_laser.ogg'),
    'enemy_explosion': get_audio_path('enemy_explosion.ogg'),
    'player_damage': get_audio_path('player_damage.ogg'),
    'powerup': get_audio_path('powerup.ogg')
}

# Каналы звука для каждого типа
channels = {
    'music': 1,
    'enemy_laser': 2,
    'enemy_explosion': 3,
    'player_damage': 4,
    'powerup': 5
}


def play(name: str) -> None:
    """ Воспроизвести определённый звук """
    mixerChannel = pygame.mixer.Channel(channels[name])
    sound = pygame.mixer.Sound(audio[name])
    if name == 'music':
        sound.set_volume(0.5)
    mixerChannel.play(sound)


def update_music() -> None:
    """ Убедиться, что музыка играет """
    music_channel = pygame.mixer.Channel(channels['music'])
    if not music_channel.get_busy():
        play('music')


def stop(name: str) -> None:
    """ Остановить воспроизведение звука """
    mixerChannel = pygame.mixer.Channel(channels[name])
    mixerChannel.stop()
