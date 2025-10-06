from dynaconf import Dynaconf
from pathlib import Path
from os.path import join

BASE_PATH = str(Path(__file__).parent)

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=[
        join(BASE_PATH, "base_settings.ini"),
        join(BASE_PATH, "base_secrets.ini")
    ],
    load_dotenv=True,
    environments=False
)