# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import json
from dataclasses import dataclass
from typing import List

import pkg_resources


@dataclass
class Config:
    languages: List[str]
    greetings: List[str]


def load_config() -> Config:
    config_json = pkg_resources.resource_string(__name__, "config.json").decode()
    data = json.loads(config_json)
    config = Config(languages=data["languages"], greetings=data["greetings"])
    return config
