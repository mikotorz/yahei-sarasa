import shutil as fs
import requests as req
import py7zr as sz
import auto_configs as conf
import os
import json
import wget

API_URL = 'https://api.github.com/repos/IBM/plex/releases/tags/%40ibm%2Fplex-sans-sc%401.1.0'


def get_latest():
    response = req.get(API_URL)
    details = json.loads(response.content)

    name = ('sc' + '.zip')

    assets = details['assets']
    for asset in assets:
        if (asset['name'] == name):
            return asset['browser_download_url']


def clear_dir(directory):
    if (os.path.exists(directory)):
        fs.rmtree(directory)
    os.makedirs(directory)


def download(url):
    filename = url.split('/')[-1]
    path = conf.TEMP_DIR + '/' + filename

    wget.download(url, path)

    return path


def unzip(path):
    with sz.SevenZipFile(path, mode='r') as zip_file:
        zip_file.extractall(path=conf.TEMP_DIR)
