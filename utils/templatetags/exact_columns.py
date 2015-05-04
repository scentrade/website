from django.template import Library
from itertools import cycle
from math import ceil

register = Library()

@register.filter
def exact_columns(items, number_of_columns):
    """Divides a list in an exact number of columns.
    The number of columns is guaranteed.

    Examples:

        8x3:
        [[1, 2, 3], [4, 5, 6], [7, 8]]

        2x3:
        [[1], [2], []]
    """
    try:
        number_of_columns = int(number_of_columns)
        items = list(items)
    except (ValueError, TypeError):
        return [items]

    number_of_items = len(items)
    items_per_column = float(number_of_items) / float(number_of_columns)
    items_per_column = int(ceil(items_per_column))

    columns = [[] for x in range(number_of_columns)]
    actual_column = 0

    for index, item in enumerate(items):
        columns[actual_column].append(item)
        if (index + 1) % items_per_column == 0:
            actual_column += 1

    return columns