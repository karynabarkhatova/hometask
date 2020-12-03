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
    assert parse_parameters('https://www.google.com/search?q=cats&client=ubuntu&hs=Llg&sxsrf=ALeKk03r_grGYLuOdfHVpmW2qVuKJiAJzA:1607037631159&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjQ9JTZ-bLtAhXVFXcKHRtqCdIQ_AUoAXoECBEQAw&biw=1920&bih=944') == {'q': 'cats', 'client': 'ubuntu', 'hs': 'Llg', 'sxsrf': 'ALeKk03r_grGYLuOdfHVpmW2qVuKJiAJzA:1607037631159', 'source': 'lnms', 'tbm': 'isch', 'sa': 'X', 'ved': '2ahUKEwjQ9JTZ-bLtAhXVFXcKHRtqCdIQ_AUoAXoECBEQAw', 'biw': '1920', 'bih': '944'}
    assert parse_parameters('https://news.google.com/topstories?hl=ru&gl=UA&ceid=UA:ru') == {'hl': 'ru', 'gl': 'UA', 'ceid': 'UA:ru'}

    # Tests for function "parse_cookies"
    assert parse_cookies('name=_ga;content=GA1.2.1961323879.1607037432') == {'name': '_ga', 'content': 'GA1.2.1961323879.1607037432'}
    assert parse_cookies('name=_rxuuid;content=%7B%22rx_uuid%22%3A%22RX-95776ea7-297b-4710-871d-98c89147d635-003%22%7D') == {'name': '_rxuuid', 'content': '%7B%22rx_uuid%22%3A%22RX-95776ea7-297b-4710-871d-98c89147d635-003%22%7D'}
