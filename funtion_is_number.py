def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        pass
    try:
        import unicodedata

        unicodedata.numeric(num)
        return True
    except (TypeError, ValueError):
        pass
    return False
