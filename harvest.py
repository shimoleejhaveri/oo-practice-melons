############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""


    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

        return self.pairings

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code

        return new_code

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    musk = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    cas.add_pairing('strawberries')
    cas.add_pairing('mint')
    all_melon_types.append(cas)

    cren = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        print(f'{melon.name} pairs with')

        for pair in melon.pairings:
            print(f"- {pair}")

    # Fill in the rest

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dic = {}
    for melon in melon_types:
        melon_dic[melon.code] = melon


    return melon_dic

    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    shape = 5
    color = 5
    
    def __init__(self, melon_type, shape_rating, color_rating, harvested_from, harvested_by):
        """Initialize a harvest."""

        self.type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by


    def is_sellable(shape_rating, color_rating, harvested_from):
        if self.shape_rating > shape and self.color_rating > color and harvested_from != "Field 3":

            return True

        return False

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melon_dic = make_melon_type_lookup(make_melon_types())

    melon1 = Melon('yw', 8, 7, 'Field 2', "Sheila")
    melon2 = Melon('yw', 3, 4, 'Field 2', "Sheila")
    melon3 = Melon('yw', 9, 8, 'Field 3', "Sheila")
    melon9 = Melon('yw', 7, 10, 'Field 3', "Sheila")
    list_yw = [melon1, melon2, melon3, melon9]
    melon4 = Melon('cas', 10, 6, 'Field 35', "Sheila")
    list_cas = [melon4]
    melon5 = Melon('cren', 8, 9, 'Field 35', "Michael")
    melon6 = Melon('cren', 8, 2, 'Field 35', "Michael")
    melon7 = Melon('cren', 2, 3, 'Field 4', "Michael")
    list_cren = [melon5, melon6, melon7]
    melon8 = Melon('musk', 6, 7, 'Field 4', "Michael")
    list_musk = [melon8]


    

    return make_melon_type_lookup(make_melon_types())




    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



