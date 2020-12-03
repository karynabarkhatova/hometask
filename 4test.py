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
    assert parse_parameters('https://www.google.com/search?client=ubuntu&hs=970&sxsrf=ALeKk01Ji7gSmGl1jHzHJnnwmEgMKrI5Dw%3A1607036484741&ei=RG7JX7vfLMavrgTvm4LICg&q=simpsons&oq=simpsons&gs_lcp=CgZwc3ktYWIQAzIKCC4QsQMQQxCTAjIFCAAQsQMyBAgAEEMyBAgAEEMyBAguEEMyBAgAEEMyBAguEEMyAggAMgIIADICCC46CAgAELEDEIMBOgUILhCxAzoHCAAQsQMQQzoHCC4QsQMQQzoHCC4QQxCTAlDixQNY0dADYJjSA2gAcAB4AIABigGIAcUGkgEDMy41mAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=psy-ab&ved=0ahUKEwi7kcG29bLtAhXGl4sKHe-NAKkQ4dUDCA0&uact=5') == {'client': 'ubuntu', 'hs': '970', 'sxsrf': 'ALeKk01Ji7gSmGl1jHzHJnnwmEgMKrI5Dw:1607036484741', 'ei': 'RG7JX7vfLMavrgTvm4LICg', 'q': 'simpsons', 'oq': 'simpsons', 'gs_lcp': 'CgZwc3ktYWIQAzIKCC4QsQMQQxCTAjIFCAAQsQMyBAgAEEMyBAgAEEMyBAguEEMyBAgAEEMyBAguEEMyAggAMgIIADICCC46CAgAELEDEIMBOgUILhCxAzoHCAAQsQMQQzoHCC4QsQMQQzoHCC4QQxCTAlDixQNY0dADYJjSA2gAcAB4AIABigGIAcUGkgEDMy41mAEAoAEBqgEHZ3dzLXdpesABAQ', 'sclient': 'psy-ab', 'ved': '0ahUKEwi7kcG29bLtAhXGl4sKHe-NAKkQ4dUDCA0', 'uact': '5'}
    assert parse_parameters('https://www.google.com/search?q=facebook&oq=f&aqs=chrome.1.69i57j0i131i433j0i433j46i131i433j69i60l3j69i61.1777j0j4&client=ubuntu&sourceid=chrome&ie=UTF-8') == {'q': 'facebook', 'oq': 'f', 'aqs': 'chrome.1.69i57j0i131i433j0i433j46i131i433j69i60l3j69i61.1777j0j4', 'client': 'ubuntu', 'sourceid': 'chrome', 'ie': 'UTF-8'}

    # Tests for function "parse_cookies"
    assert parse_cookies('name=zuid;content=kgfCTjMzuoN6kdTz4Ows;domain=.zemanta.com;path=/') == {'name': 'zuid', 'content': 'kgfCTjMzuoN6kdTz4Ows', 'domain': '.zemanta.com', 'path': '/'}
    assert parse_cookies('name=WMF-Last-Access;content=03-Dec-2020;path=/;') == {'name': 'WMF-Last-Access', 'content': '03-Dec-2020', 'path': '/'}
