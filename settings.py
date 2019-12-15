from decouple import AutoConfig

from utils.constants import BASE_DIR, CONFIG_DIR


config = AutoConfig(search_path=BASE_DIR.joinpath(CONFIG_DIR))
