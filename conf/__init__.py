#!/usr/bin/env python
# coding: utf-8

import os

from mars.conf.default import *

env_name = os.environ.get('ENV_NAME')

if env_name == 'prod':
    from mars.conf.prod import *

try:
    from mars.conf.local import *
except ImportError:
    pass
