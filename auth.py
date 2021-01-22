# A single instance of an authorization object

class Auth():
    # saves the information from the given json data
    # Parameter: json
    def __init__(self, json):
        self.access_token = {'type': 'String', 'payload': json['access_token']}
        self.token_type = {'type': 'String', 'payload': json['token_type']}
        self.expires_in = {'type': 'String', 'payload': json['expires_in']}
        self.scope = {'type': 'String', 'payload': json['scope']}
        self.detail = {'type': 'String', 'payload': json['detail']}
        self.backup_code = {'type': 'String', 'payload': json['backup_code']}
        self.refresh_token = {'type': 'String', 'payload': json['refresh_token']}
    
    # To string
    # returns the access token string
    def __str__(self):
        return self.access_token['payload']