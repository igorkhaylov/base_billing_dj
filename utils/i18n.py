import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)

from utils.localization import Localization

locales_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'locales/')

i18n = Localization(default_language='ru', locales_path=locales_folder)
