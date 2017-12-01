#!/usr/bin/env python3

"""To change the exact amount of money of one kind to another.

__author__ = "XiongJie"
__pkuid__  = "1700011827"
__email__  = "xiongjie1999@pku.edu.cn"
"""


def before_space(s):
    """Returns: Substring of s; up to, but not including, the first space
    Parameter s: the string to slice
    Precondition: s has at least one space in it"""
    if 0 <= s.find(" ") <= len(s)-1:
        t = s[:s.find(" ")]
    return t


def first_insight_quote(s):
    """Returns: The first substring of s between two (double) quote characters
    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside."""
    m = s.find('"')
    t = s[m+1:]
    n = t.find('"') + m + 1
    quote = s[m+1:n]
    return quote


def get_from(json):
    """Returns: The FROM value in the response to a currency query.
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    new_json = json[8:]
    renew_json = first_insight_quote(new_json)
    return renew_json


def get_to(json):
    """Returns: The TO value in the response to a currency query.
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    m = json.find('"')
    n = json[m+1:]
    o = n.find('"')
    p = n[o+1:]
    q = p.find('"')
    r = p[q+1:]
    s = r.find('"')
    t = r[s+1:]
    u = t.find('"')
    v = t[u+1:]
    w = v.find('"')
    x = v[w+1:]
    quote = first_insight_quote(x)
    return quote


def has_error(json):
    """Returns: True if the query has an error; False otherwise.
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    if ord(json[-11]) == ord('i'):
        return True
    else:
        return False


def iscurrency(currency):
    """Returns: True if currency is a valid (3 letter code for a) currency.
    It returns False otherwise.
    Parameter currency: the currency code to verify
    Precondition: currency is a string."""
    first_part = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='
    second_part = currency
    third_part = '&to=USD&amt=2.5'
    string = first_part+second_part+third_part
    
    from urllib.request import urlopen
    doc = urlopen(string)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    
    if has_error(jstr) == False:
        return True
    else:
        return False


def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.
    
    In this exchange, the user is changing amount_from money in
    currency currency_from to the currency currency_to. The value
    returned represents the amount in currency currency_to.
        
    The value returned has type float.
        
    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code
        
    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code
        
    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    
    if iscurrency(currency_from) == True and iscurrency(currency_to) == True:
        first_part = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?'
        second_part = 'from='
        third_part = currency_from
        fourth_part = '&to='
        fifth_part = currency_to
        sixth_part = '&amt='
        seventh_part = str(amount_from)
        string = first_part+second_part+third_part+fourth_part+fifth_part+sixth_part+seventh_part
        
        from urllib.request import urlopen
        doc = urlopen(string)
        docstr = doc.read()
        doc.close()
        jstr = docstr.decode('ascii')
        
        if has_error(jstr) == False:
            back = get_to(jstr)
            result = float(before_space(back))
            return result
        else:
            print("amount error")
    else:
        print("currency error")


def test_before_space():
    """test function:before_space(s)"""
    s = 'ee o'
    assert('ee' == before_space(s))


def test_first_insight_quote():
    """test function:first_insight_quote(s)"""
    s = 'A "B C" D "E F" G'
    assert('B C' == first_insight_quote(s))


def test_get_from():
    """test function:get_from(json)"""
    json = '{"from":"2 United States Dollars","to":"1.825936 Euros","success":true,"error":""}'
    assert('2 United States Dollars' == get_from(json))


def test_get_to():
    """test function:get_to(json)"""
    json = '{"from":"2 United States Dollars","to":"1.825936 Euros","success":true,"error":""}'
    assert('1.825936 Euros' == get_to(json))


def test_has_error():
    """test function:has_error(json)"""
    json = '{"from":"2 United States Dollars","to":"1.825936 Euros","success":true,"error":""}'
    assert(False == has_error(json))


def test_iscurrency():
    """test function:iscurrency(currency)"""
    currency = 'SSS'
    assert(False == iscurrency(currency))


def test_exchange():
    """test function:exchange(currency_from, currency_to, amount_from)"""
    currency_from = 'USD'
    currency_to = 'EUR'
    amount_from = 2.5
    assert(exchange(currency_from, currency_to, amount_from) == 2.0952375)


def testAll():
    """test all cases"""
    test_before_space()
    test_first_insight_quote()
    test_get_from()
    test_get_to()
    test_has_error()
    test_iscurrency()
    test_exchange()
    print("All tests passed")
