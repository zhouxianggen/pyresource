# coding: utf8 


# ecs resource
class ECS(object):
    def __init__(self, ip='', inner_ip='', groups=[]):
        self.ip = ip
        self.inner_ip = inner_ip
        self.groups = [x for x in groups]
 

# oss resource
class OSS(object):
    def __init__(self, endpoint='', bucket='', key_id='', key_value='', 
            host=''):
        self.endpoint = endpoint
        self.bucket = bucket
        self.key_id = key_id
        self.key_value = key_value
        self.host = host


# redis resource
class REDIS(object):
    def __init__(self, host='localhost', port=6379, pswd=None):
        self.host = host
        self.port = port
        self.pswd = pswd


# rds resource
class RDS(object):
    def __init__(self, host='localhost', port=3306, user='root', pswd=None):
        self.host = host
        self.port = port
        self.user = user
        self.pswd = pswd


# mongodb resource
class MDB(object):
    def __init__(self, host='localhost', port=27017, user='admin', pswd=None):
        self.host = host
        self.port = port
        self.user = user
        self.pswd = pswd


# vps resource
class VPS(object):
    def __init__(self, name, ip, port, user, pswd, vendor):
        self.name = name
        self.ip = ip
        self.port = port
        self.user = user
        self.pswd = pswd
        self.vendor = vendor
 
