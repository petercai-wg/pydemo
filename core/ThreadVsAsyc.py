import requests
import time
import concurrent.futures
import os

import aiohttp
import aiofiles
from contextlib import closing
import asyncio

images_dir = 'C:/tmp/images/'
CHUNK_SIZE = 20 * 1024 * 1024

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c'
]


async def as_download_image(img_url: str):

    print("starting to download " + img_url)
    img_name = img_url.split('/')[3]

    async with aiohttp.ClientSession() as session:
        response = await session.get(img_url)
        assert response.status == 200
        f = await aiofiles.open(images_dir + img_name + 'jpg',  mode='wb')
        await f.write(await response.read())
        await f.close()
        print(img_name + ' was downloaded')


def asyc_download():
    print("staring asyc_donwload...")
    print(img_urls)

    start = time.perf_counter()

    tasks = [asyncio.ensure_future(as_download_image(url)) for url in img_urls]

    loop = asyncio.get_event_loop()

    loop.run_until_complete(asyncio.wait(tasks))

    # for t in tasks:
    #     print(t.result)

    print(f'Finished in { time.perf_counter() - start} seconds')


def download_image(img_url):
    print(f'start downloading {img_url} ...')
    img_bytes = requests.get(img_url).content

    img_name = img_url.split('/')[3]

    with open(images_dir + img_name + 'jpg', 'wb') as img_file:
        img_file.write(img_bytes)
        return img_name + ' was downloaded'


def thread_download():
    print("staring threaddownload")
    print(img_urls)
    start = time.perf_counter()

    # threads = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # executor.map(download_image, img_urls)
        threads = [executor.submit(download_image,  url)
                   for url in img_urls]

        for f in concurrent.futures.as_completed(threads):
            print(f.result())

    print(f'Finished in { time.perf_counter() - start} seconds')


def cleanImageDir():
    for f in os.listdir(images_dir):
        os.remove(os.path.join(images_dir, f))


cleanImageDir()
thread_download()

# asyc_download()
