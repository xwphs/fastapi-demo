
def base_response(code, msg, data=None):
    result = {
        'code': code,
        'message': msg,
        'data': data
    }
    return result

def success(msg, data=None):
    return base_response(200, msg, data)

def fail(code = -1, msg='', data=None):
    return base_response(code, msg, data)