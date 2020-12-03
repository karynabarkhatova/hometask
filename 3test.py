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
    assert parse_parameters('chrome://settings/cookies/detail?site=medium.com') == {'site': 'medium.com'}
    assert parse_parameters('https://www.coursera.org/specializations/python') == {}

    # Tests for function "parse_cookies"
    assert parse_cookies('name=yandexuid;content=2738049701606514651') == {'name': 'yandexuid', 'content': '2738049701606514651'}
    assert parse_cookies('name=CONSENT;') == {'name': 'CONSENT'}
