class Colors:
    grey = (32, 32, 32)
    beige = (255, 229, 204)
    dark_pink = (255, 102, 178)
    medium_pink = (255, 153, 204)
    light_pink = (255, 204, 229)
    dark_purple = (255, 102, 255)
    light_purple = (255, 204, 255)
    coral = (255, 204, 204)

    @classmethod
    def get_cell_colors(cls):
        return [cls.grey, cls.beige, cls.dark_pink, cls.medium_pink, cls.light_pink, cls.dark_purple, cls.light_purple, cls.coral]
    