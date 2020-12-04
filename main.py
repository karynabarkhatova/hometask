from urllib import parse


def parse_parameters(url):
    parsed_url = parse.urlsplit(url)
    if parsed_url.query == '':
        return dict()
    else:
        params = dict(parse.parse_qsl(parse.urlsplit(url).query))
        return params


def parse_cookies(cookies):
    if cookies == '':
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
    assert parse_parameters('http://example.com/?') == {}
    assert parse_parameters('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse_parameters('https://www.google.com.ua/maps/@50.4851493,30.4721233,14z?hl=ru') == {'hl': 'ru'}
    assert parse_parameters('https://www.google.com/search?client=ubuntu&hs=Umf&sxsrf=ALeKk02XZT5LX_M0wlhBhGo0RIDMd7gmsQ%3A1607033858054&ei=AmTJX5blAoXrrgTDwqf4DA&q=google&oq=google&gs_lcp=CgZwc3ktYWIQAzIECCMQJzIKCAAQsQMQgwEQQzIKCAAQsQMQgwEQQzIKCAAQsQMQgwEQQzIECAAQQzIECAAQQzIECAAQQzIHCAAQsQMQQzIECAAQQzIECAAQQzoICAAQsQMQgwE6BAguEENQpFxYoGFg3mFoAHAAeACAAW6IAY8EkgEDMC41mAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=psy-ab&ved=0ahUKEwiW7oDS67LtAhWFtYsKHUPhCc8Q4dUDCA0&uact=5') == {'client': 'ubuntu', 'hs': 'Umf', 'sxsrf': 'ALeKk02XZT5LX_M0wlhBhGo0RIDMd7gmsQ:1607033858054', 'ei': 'AmTJX5blAoXrrgTDwqf4DA', 'q': 'google', 'oq': 'google', 'gs_lcp': 'CgZwc3ktYWIQAzIECCMQJzIKCAAQsQMQgwEQQzIKCAAQsQMQgwEQQzIKCAAQsQMQgwEQQzIECAAQQzIECAAQQzIECAAQQzIHCAAQsQMQQzIECAAQQzIECAAQQzoICAAQsQMQgwE6BAguEENQpFxYoGFg3mFoAHAAeACAAW6IAY8EkgEDMC41mAEAoAEBqgEHZ3dzLXdpesABAQ', 'sclient': 'psy-ab', 'ved': '0ahUKEwiW7oDS67LtAhWFtYsKHUPhCc8Q4dUDCA0', 'uact': '5'}
    assert parse_parameters('chrome://settings/cookies/detail?site=medium.com') == {'site': 'medium.com'}
    assert parse_parameters('https://www.coursera.org/specializations/python') == {}
    assert parse_parameters('https://www.google.com/search?client=ubuntu&hs=970&sxsrf=ALeKk01Ji7gSmGl1jHzHJnnwmEgMKrI5Dw%3A1607036484741&ei=RG7JX7vfLMavrgTvm4LICg&q=simpsons&oq=simpsons&gs_lcp=CgZwc3ktYWIQAzIKCC4QsQMQQxCTAjIFCAAQsQMyBAgAEEMyBAgAEEMyBAguEEMyBAgAEEMyBAguEEMyAggAMgIIADICCC46CAgAELEDEIMBOgUILhCxAzoHCAAQsQMQQzoHCC4QsQMQQzoHCC4QQxCTAlDixQNY0dADYJjSA2gAcAB4AIABigGIAcUGkgEDMy41mAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=psy-ab&ved=0ahUKEwi7kcG29bLtAhXGl4sKHe-NAKkQ4dUDCA0&uact=5') == {'client': 'ubuntu', 'hs': '970', 'sxsrf': 'ALeKk01Ji7gSmGl1jHzHJnnwmEgMKrI5Dw:1607036484741', 'ei': 'RG7JX7vfLMavrgTvm4LICg', 'q': 'simpsons', 'oq': 'simpsons', 'gs_lcp': 'CgZwc3ktYWIQAzIKCC4QsQMQQxCTAjIFCAAQsQMyBAgAEEMyBAgAEEMyBAguEEMyBAgAEEMyBAguEEMyAggAMgIIADICCC46CAgAELEDEIMBOgUILhCxAzoHCAAQsQMQQzoHCC4QsQMQQzoHCC4QQxCTAlDixQNY0dADYJjSA2gAcAB4AIABigGIAcUGkgEDMy41mAEAoAEBqgEHZ3dzLXdpesABAQ', 'sclient': 'psy-ab', 'ved': '0ahUKEwi7kcG29bLtAhXGl4sKHe-NAKkQ4dUDCA0', 'uact': '5'}
    assert parse_parameters('https://www.google.com/search?q=facebook&oq=f&aqs=chrome.1.69i57j0i131i433j0i433j46i131i433j69i60l3j69i61.1777j0j4&client=ubuntu&sourceid=chrome&ie=UTF-8') == {'q': 'facebook', 'oq': 'f', 'aqs': 'chrome.1.69i57j0i131i433j0i433j46i131i433j69i60l3j69i61.1777j0j4', 'client': 'ubuntu', 'sourceid': 'chrome', 'ie': 'UTF-8'}
    assert parse_parameters('https://www.google.com/search?q=cats&client=ubuntu&hs=Llg&sxsrf=ALeKk03r_grGYLuOdfHVpmW2qVuKJiAJzA:1607037631159&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjQ9JTZ-bLtAhXVFXcKHRtqCdIQ_AUoAXoECBEQAw&biw=1920&bih=944') == {'q': 'cats', 'client': 'ubuntu', 'hs': 'Llg', 'sxsrf': 'ALeKk03r_grGYLuOdfHVpmW2qVuKJiAJzA:1607037631159', 'source': 'lnms', 'tbm': 'isch', 'sa': 'X', 'ved': '2ahUKEwjQ9JTZ-bLtAhXVFXcKHRtqCdIQ_AUoAXoECBEQAw', 'biw': '1920', 'bih': '944'}
    assert parse_parameters('https://news.google.com/topstories?hl=ru&gl=UA&ceid=UA:ru') == {'hl': 'ru', 'gl': 'UA', 'ceid': 'UA:ru'}


    # Tests for function "parse_cookies"
    assert parse_cookies('') == {}
    assert parse_cookies('name=Dima;') == {'name': 'Dima'}
    assert parse_cookies('name=__cfduid;content=d3f8da631d8ec34d5357a3f4383a816101606942741') == {'name': '__cfduid', 'content': 'd3f8da631d8ec34d5357a3f4383a816101606942741'}
    assert parse_cookies('') == {}
    assert parse_cookies('name=yandexuid;content=2738049701606514651') == {'name': 'yandexuid', 'content': '2738049701606514651'}
    assert parse_cookies('name=CONSENT;') == {'name': 'CONSENT'}
    assert parse_cookies('name=zuid;content=kgfCTjMzuoN6kdTz4Ows;domain=.zemanta.com;path=/') == {'name': 'zuid', 'content': 'kgfCTjMzuoN6kdTz4Ows', 'domain': '.zemanta.com', 'path': '/'}
    assert parse_cookies('name=WMF-Last-Access;content=03-Dec-2020;path=/') == {'name': 'WMF-Last-Access', 'content': '03-Dec-2020', 'path': '/'}
    assert parse_cookies('name=_ga;content=GA1.2.1961323879.1607037432') == {'name': '_ga', 'content': 'GA1.2.1961323879.1607037432'}
    assert parse_cookies('name=_rxuuid;content=%7B%22rx_uuid%22%3A%22RX-95776ea7-297b-4710-871d-98c89147d635-003%22%7D') == {'name': '_rxuuid', 'content': '%7B%22rx_uuid%22%3A%22RX-95776ea7-297b-4710-871d-98c89147d635-003%22%7D'}
    
    
    
