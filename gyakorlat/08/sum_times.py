# Implementald az alabbi fuggvenyt!
# A parametere egy lista, ami 'hh:mm' formatumu stringeket tartalmaz.
# Ezek idotartamokat jelolnek: a 'hh' az orakat, az 'mm' a perceket.
# Ezek mindig 2-jegyu szamok, amik kezdodhetnek 0-val.
# A fuggveny ugyanilyen formatumban adja vissza az idotartamok osszeget.
# Az eredmenyben is legalabb 2 szamjegy hosszu legyen az orak szama, de lehet
# tobb szamjegyu is.
# A parameterben kapott listat ne valtoztassa meg!

def sum_times(times: list) -> str:
    """Sum up a list of times given as 'hh:mm' strings.

    'hh' is the number of hours as a 2-digit integer between 00 and 99.
    'mm' is the number of minutes as a 2-digit integer between 00 and 59.
    If a number is below 10, a 0 digit precedes it.

    Return the sum as an 'hh:mm' string.
    Or 'hhh:mm', if the result has 100 or more hours.
    Or 'hhhh:mm', if the result has 1000 or more hours.
    ...

    >>> sum_times(['11:30', '02:35'])
    '14:05'
    >>> sum_times(['42:00', '44:44', '40:15'])
    '126:59'
    >>> sum_times([])
    '00:00'
    """
    # Ide ird a fuggveny implementaciojat:
    sum = 0
    for t in times:
        h = int(t[0:2])
        m = int(t[3] + t[4])
        strings = t.split(':')
        h = int(strings[0])
        m = int(strings[1])
        sum += 60*h + m
    hh = sum // 60
    mm = sum - 60*hh # mm = sum % 60
    result = ''
    if hh < 10:
        result += '0'
    result += str(hh) + ':'
    if mm < 10:
        result += '0'
    result += str(mm)
    #result = f'{hh:02}:{mm:02}'
    return result


if __name__ == '__main__':
    # Docstringben levo peldak ellenorzese
    import doctest
    doctest.testmod()
    # Itt tudod sajat peldakon tesztelni, pl.:
    example = ['03:20', '05:15', '00:30']
    print(sum_times(example))
