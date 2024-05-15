def samitleri_al(cumle):
    samitler = set()
    for herf in cumle:
        if herf.lower() not in {'a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü', ' ', '.'}:
            samitler.add(herf)
    return samitler

