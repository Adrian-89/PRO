def sort(asc=True):
    def decorator(func):
        return sort


@sort
def extract_evens(*values):
    return (v for v in values if  v % 2 == 0):