#encoding:utf8

def sendMsg(MyUserName, ToUserName, msg):
    url = base_uri + '/webwxsendmsg?pass_ticket=%s' % (pass_ticket)
    params = {
        "BaseRequest": BaseRequest,
        "Msg": {"Type": 1, "Content": msg, "FromUserName": MyUserName, "ToUserName": ToUserName},
    }

    json_obj = json.dumps(params,ensure_ascii=False).encode('utf-8')
    request = urllib.request.Request(url=url, data=json_obj)
    request.add_header('ContentType', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    data = response.read()

    print(data)