#!/usr/bin/env python3
# coding: utf-8

from kodi_six import xbmc, xbmcaddon

addon = xbmcaddon.Addon()
path = addon.getAddonInfo('path')

some_string = u"Hello World"
xbmc.log(some_string)
