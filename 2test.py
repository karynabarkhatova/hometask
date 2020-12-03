from urllib import parse


def parse_parameters(url):
    parsedurl = parse.urlsplit(url)
    if parsedurl.query == '':
        return dict()
    else:
        params = dict(parse.parse_qsl(parse.urlsplit(url).query))
        return params


def parse_cookies(cookies):
    if len(cookies) < 1:
        return dict()
    else:
        try:
            d = dict(x.split('=') for x in cookies.split(';'))
            return d
        except:
            d = dict()
            pairs = cookies.strip(';')
            pair = pairs.split('=')
            key = pair[0]
            value = pair[1]
            d[key] = value
            return d


if __name__ == '__main__':
    # Tests for function "parse_parameters"
    assert parse_parameters('https://www.google.com.ua/maps/@50.4851493,30.4721233,14z?hl=ru') == {'hl': 'ru'}
    assert parse_parameters('https://www.google.com/search?client=ubuntu&hs=Umf&sxsrf=ALeKk02XZT5LX_M0wlhBhGo0RIDMd7gmsQ%3A1607033858054&ei=AmTJX5blAoXrrgTDwqf4DA&q=google&oq=google&gs_lcp=CgZwc3ktYWIQAzIECCMQJzIKCAAQsQMQgwEQQzIKCAAQsQMQgwEQQzIKCAAQsQMQgwEQQzIECAAQQzIECAAQQzIECAAQQzIHCAAQsQMQQzIECAAQQzIECAAQQzoICAAQsQMQgwE6BAguEENQpFxYoGFg3mFoAHAAeACAAW6IAY8EkgEDMC41mAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=psy-ab&ved=0ahUKEwiW7oDS67LtAhWFtYsKHUPhCc8Q4dUDCA0&uact=5') == {'client': 'ubuntu', 'hs': 'Umf', 'sxsrf': 'ALeKk02XZT5LX_M0wlhBhGo0RIDMd7gmsQ:1607033858054', 'ei': 'AmTJX5blAoXrrgTDwqf4DA', 'q': 'google', 'oq': 'google', 'gs_lcp': 'CgZwc3ktYWIQAzIECCMQJzIKCAAQsQMQgwEQQzIKCAAQsQMQgwEQQzIKCAAQsQMQgwEQQzIECAAQQzIECAAQQzIECAAQQzIHCAAQsQMQQzIECAAQQzIECAAQQzoICAAQsQMQgwE6BAguEENQpFxYoGFg3mFoAHAAeACAAW6IAY8EkgEDMC41mAEAoAEBqgEHZ3dzLXdpesABAQ', 'sclient': 'psy-ab', 'ved': '0ahUKEwiW7oDS67LtAhWFtYsKHUPhCc8Q4dUDCA0', 'uact': '5'}

    # Tests for function "parse_cookies"
    assert parse_cookies('name=__cfduid;content=d3f8da631d8ec34d5357a3f4383a816101606942741') == {'name': '__cfduid', 'content': 'd3f8da631d8ec34d5357a3f4383a816101606942741'}
    assert parse_cookies('') == {}
    
