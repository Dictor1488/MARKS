# -*- coding: utf-8 -*-
"""Preserve the single INQ Marks badgeStyle before the main module is imported.

World of Tanks loads mod_*.pyc modules by filename.  This module deliberately
sorts before mod_inq_marks.py and prepares a temporary legacy-compatible view
of the config.  The runtime rules module converts it back to the public
single-key format after the main module has finished importing.
"""

import json
import os


_CONFIG_FILE = os.path.normpath(
    os.path.join(os.getcwd(), 'mods', 'configs', 'inq', 'marks', 'marks.json')
)
_VALID_STYLES = ('classic', 'compact', 'polaroid', 'neer', 'minimal')
_GARAGE_STYLES = ('classic', 'compact', 'polaroid')

_GARAGE_STYLE_NAMES = {
    'classic': 'garage style 1',
    'compact': 'garage style 2',
    'polaroid': 'garage style 3',
}
_BATTLE_STYLE_NAMES = {
    'classic': 'battle style 1',
    'compact': 'battle style 2',
    'polaroid': 'battle style 3',
    'neer': 'battle style 4',
    'minimal': 'battle style 5',
}


def _safeLower(value):
    if value is None:
        return ''
    try:
        return unicode(value).lower()
    except Exception:
        try:
            return str(value).lower()
        except Exception:
            return ''


def _prepareConfig():
    if not os.path.isfile(_CONFIG_FILE):
        return

    try:
        with open(_CONFIG_FILE, 'rb') as stream:
            loaded = json.load(stream)
    except Exception:
        return

    if not isinstance(loaded, dict):
        return

    style = _safeLower(loaded.get('badgeStyle'))
    if style not in _VALID_STYLES:
        return

    compatibility = {
        'garageBadgeStyle': style if style in _GARAGE_STYLES else 'classic',
        'battleBadgeStyle': style,
        'garageBadgeStyles': dict(_GARAGE_STYLE_NAMES),
        'battleBadgeStyles': dict(_BATTLE_STYLE_NAMES),
    }

    try:
        with open(_CONFIG_FILE, 'wb') as stream:
            json.dump(compatibility, stream, indent=4, sort_keys=True)
    except Exception:
        pass


_prepareConfig()
