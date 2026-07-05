"""
Styles package initialization.
"""

from .theme import NORTHERN_LIGHTS_COLORS, GLOBAL_CSS
from .visual_system import get_unified_card_styles, get_unified_text_styles

__all__ = [
    "NORTHERN_LIGHTS_COLORS", 
    "GLOBAL_CSS", 
    "get_unified_card_styles", 
    "get_unified_text_styles"
]
