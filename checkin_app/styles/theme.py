"""
Theme definitions for the Northern Lights visual identity.
"""

# Northern Lights Color Palette
# Deep dark midnight blue/black, vibrant aurora tones, and high-contrast text colors.
NORTHERN_LIGHTS_COLORS: dict[str, dict[str, str]] = {
    "dark": {
        "bg": "#020617",  # Slate 950
        "aurora_teal": "#2DD4BF",  # Teal 400
        "aurora_cyan": "#22D3EE",  # Cyan 400
        "aurora_green": "#4ADE80",  # Green 400
        "aurora_violet": "#8B5CF6",  # Violet 500
        "aurora_magenta": "#D946EF",  # Magenta 500
        "text_primary": "#F8FAFC",  # Slate 50
        "text_secondary": "#94A3B8",  # Slate 400
        "accent": "#2DD4BF",  # Teal 400
        "card_bg": "#0f172a",
    },
    "light": {
        "bg": "#F8FAFC",  # Slate 50
        "aurora_teal": "#0D9488",  # Teal 600
        "aurora_cyan": "#0891B2",  # Cyan 600
        "aurora_green": "#16A34A",  # Green 600
        "aurora_violet": "#7C3AED",  # Violet 600
        "aurora_magenta": "#C026D3",  # Magenta 600
        "text_primary": "#0F172A",  # Slate 900
        "text_secondary": "#1E293B",  # Slate 800
        "accent": "#0D9488",  # Teal 600
        "card_bg": "#FFFFFF",
    },
}

# Global CSS definitions including fonts and animations.
GLOBAL_CSS: str = f"""
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

body {{
    font-family: 'Outfit', sans-serif;
    margin: 0;
    padding: 0;
    transition: background-color 0.3s ease, color 0.3s ease;
}}

@keyframes aurora_drift_1 {{
  0% {{ transform: translate(0, 0) scale(1) rotate(0deg); opacity: 0.5; }}
  50% {{ transform: translate(-5vw, 10vh) scale(1.2) rotate(15deg); opacity: 0.8; }}
  100% {{ transform: translate(5vw, -5vh) scale(0.9) rotate(-5deg); opacity: 0.5; }}
}}

@keyframes aurora_drift_2 {{
  0% {{ transform: translate(0, 0) scale(1.1) rotate(0deg); opacity: 0.6; }}
  50% {{ transform: translate(8vw, -8vh) scale(0.9) rotate(-10deg); opacity: 0.9; }}
  100% {{ transform: translate(6vw, 6vh) scale(1.2) rotate(5deg); opacity: 0.6; }}
}}

@keyframes aurora_drift_3 {{
  0% {{ transform: translate(0, 0) scale(0.9) rotate(0deg); opacity: 0.7; }}
  50% {{ transform: translate(-10vw, -10vh) scale(1.3) rotate(20deg); opacity: 0.4; }}
  100% {{ transform: translate(8vw, 8vh) scale(1) rotate(-10deg); opacity: 0.7; }}
}}

@keyframes aurora_drift_4 {{
  0% {{ transform: translate(0, 0) scale(1.2) rotate(0deg); opacity: 0.4; }}
  50% {{ transform: translate(12vw, 5vh) scale(0.8) rotate(-15deg); opacity: 0.8; }}
  100% {{ transform: translate(-5vw, -12vh) scale(1.1) rotate(10deg); opacity: 0.4; }}
}}

@keyframes pulse {{
  0% {{
    transform: scale(0.95);
    box-shadow: 0 0 0 0 rgba(45, 212, 191, 0.7);
  }}
  70% {{
    transform: scale(1);
    box-shadow: 0 0 0 6px rgba(45, 212, 191, 0);
  }}
  100% {{
    transform: scale(0.95);
    box-shadow: 0 0 0 0 rgba(45, 212, 191, 0);
  }}
}}

@keyframes soft_pop {{
  0% {{ transform: scale(0.9); opacity: 0; }}
  100% {{ transform: scale(1); opacity: 1; }}
}}

@keyframes tile_flash {{
  0% {{ background-color: rgba(45, 212, 191, 0.4); }}
  100% {{ background-color: transparent; }}
}}

@keyframes input_focus_glow {{
  0% {{ box-shadow: 0 0 0 0 rgba(45, 212, 191, 0.6); }}
  100% {{ box-shadow: 0 0 0 8px rgba(45, 212, 191, 0); }}
}}

@keyframes fade_in {{
  0% {{ opacity: 0; transform: translateY(10px); }}
  100% {{ opacity: 1; transform: translateY(0); }}
}}

@keyframes border_sheen {{

  0% {{ background-position: -200% 0; }}
  100% {{ background-position: 200% 0; }}
}}
@media (prefers-reduced-motion: reduce) {{

  * {{
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }}
}}

.carousel-outer-boundary {{
    overflow: hidden;
    position: relative;
    margin: 0 auto;
}}

.carousel-scroll-viewport {{
    display: flex;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    scrollbar-width: none;
    scroll-behavior: smooth;
}}

.carousel-scroll-viewport::-webkit-scrollbar {{
    display: none;
}}

.event-card {{
    flex-shrink: 0;
    scroll-snap-align: center;
    transition: transform 0.4s cubic-bezier(0.25, 0.8, 0.25, 1), opacity 0.4s, box-shadow 0.4s, border-color 0.4s !important;
    opacity: 0.5;
    transform: scale(0.9) translateY(4px);
}}

.event-card-visually-active {{
    opacity: 1.0 !important;
    transform: scale(1.05) translateY(-6px) !important;
    box-shadow: 0 10px 30px rgba(45, 212, 191, 0.4) !important;
}}
"""

