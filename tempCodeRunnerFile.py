import matplotlib.font_manager as fm

def generate_random_font():
    available_fonts = fm.findSystemFonts()
    random_font = random.choice(available_fonts)
    return random_font