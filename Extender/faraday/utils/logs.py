#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Faraday Penetration Test IDE - Community Version
Copyright (C) 2013  Infobyte LLC (http://www.infobytesec.com/)
See the file 'doc/LICENSE' for the license information

'''
import logging
import logging.config


logging.config.fileConfig('utils/log.conf')

def getLogger(obj):
    # create logger
    logger = logging.getLogger(obj.__class__.__name__)
    return logger

