import os

from dynaconf import Dynaconf

from shared.logger import log

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
config_file_path = os.path.join(root_dir, 'config.yaml')

settings = Dynaconf(
    envvar_prefix="APP",
    settings_files=[config_file_path],
)

log.info(f"Loaded config file: {config_file_path}")
