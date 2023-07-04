#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/1Danish-00/CompressorBot/blob/main/License> .

from . import *

try:
    APP_ID = config("APP_ID", default=7774029 , cast=int)
    API_HASH = config("API_HASH" , "531dbf42d387514dc43da07db9f2dc8f")
    BOT_TOKEN = config("BOT_TOKEN" , "5316639488:AAEiy0MI7CnlIgbXK8E12XSfGNUGDorrXNo")
    OWNER = config("OWNER_ID", default=1654867043, cast=int)
    LOG = config("LOG_CHANNEL", default=-1806252657 , cast=int)
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
