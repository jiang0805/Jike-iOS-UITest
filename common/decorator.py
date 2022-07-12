
import time

import allure
import requests
import wda
from functools import wraps
from common.base import Base
from common.log import Log
import os
import imageio
import shutil
from config.read_config import ReadConfig

log = Log()


def _screenshot(name=''):
    if name:
        date_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screenshot_name = name + '-' + date_time + '.PNG'
        path = os.path.join(Base().get_path(), screenshot_name)
    else:
        temp_path = os.path.join(Base().get_path(), 'temp')
        if not os.path.exists(temp_path):
            os.mkdir(temp_path)
        screenshot_name = str(round(time.time() * 1000)) + '.PNG'
        path = os.path.join(temp_path, screenshot_name)

    driver = Base().get_driver()
    driver.screenshot(path)
    return path


def _create_gif():
    """
    生成gif文件，原始图片仅支持png格式
    gif_name ： 字符串，所生成的 gif 文件名，带 .gif 后缀
    path :      需要合成为 gif 的图片所在路径
    duration :  gif 图像时间间隔
    """

    frames = []
    path = os.path.join(Base().get_path(), 'temp')
    if not os.path.exists(path):
        return None
    if not os.listdir(path):
        return None
    else:
        png_files = os.listdir(path)
        image_list = [os.path.join(path, f) for f in png_files]
        list.sort(image_list)
        for image_name in image_list:
            # 读取 png 图像文件
            frames.append(imageio.imread(image_name))
        # 保存为 gif
        gif_name = str(round(time.time() * 1000)) + '.gif'
        gif_path = os.path.join(Base().get_path(), gif_name)
        imageio.mimsave(gif_path, frames, 'GIF', duration=0.6)
        shutil.rmtree(path)
        return gif_path


def add_attach(name=''):
    file_path = _screenshot(name)
    file_name = os.path.basename(file_path)
    with open(file_path, mode='rb') as f:
        file = f.read()
    allure.attach(file, file_name, attachment_type=allure.attachment_type.PNG)


def reset_driver():
    base_page = Base()
    base_page.set_driver()
    base_page.start_app(ReadConfig().get_pkg_name())


def step(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            log.i('--> %s' % func.__qualname__)
            return func(*args, **kwargs)
        except requests.ConnectionError:
            print("ConnectionError")
            reset_driver()
            func(*args, **kwargs)
        except Exception as e:
            log.e('\t<-- %s, %s, %s', func.__qualname__, 'Exception', e)
            raise Exception(e)
        finally:
            time.sleep(1)
            add_attach(func.__qualname__)
            _screenshot()  # 截图

    return wrapper


def case(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            log.d('\n--> %s', func.__qualname__)
            ret = func(*args, **kwargs)
            log.d('<-- %s, %s', func.__qualname__, 'Success')
            return ret
        except wda.WDAElementNotFoundError:
            print("WDAElementNotFoundError")
            log.d('\n--> %s', func.__qualname__)
            ret = func(*args, **kwargs)
            log.d('<-- %s, %s', func.__qualname__, 'Success')
            return ret
        except Exception as e:
            log.e('<-- %s, %s, %s\n', func.__qualname__, 'Exception', e)
            raise Exception(e)
        finally:
            gif_name = _create_gif()  # 生成gif 并删除tmp文件夹
            if gif_name:
                with open(gif_name, mode='rb') as f:
                    file = f.read()
                allure.attach(file, "case.gif", attachment_type=allure.attachment_type.GIF)

    return wrapper


if __name__ == '__main__':
    print(_screenshot("a"))
