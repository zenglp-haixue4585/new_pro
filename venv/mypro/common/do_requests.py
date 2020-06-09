import requests


class DoRequests:

    def http_requests(self, url, method='get', data=None, json=None, **kwargs):
        """

        :param url: 请求的url
        :param method: 请求的方法
        :param data:
        :return:
        """
        session = requests.sessions.session()
        if method.lower() == 'get':
            if data:
                resp = session.get(url=url, params=data)
            else:
                resp = session.get(url=url)
            return resp
        elif method.lower() == 'post':
            if data:
                resp = session.post(url=url, data=data)
            elif json:
                resp = session.post(url=url, json=json)
            else:
                resp = session.post(url=url)
            return resp


if __name__ == '__main__':
    do_req = DoRequests()
    res = do_req.http_request("https://www.baidu.com")
    print(res.url)
    print(res.cookies)
