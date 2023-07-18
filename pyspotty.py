from tools.spotify_requests import RequestUserAuth


class Pyspotty:

    def __init__(self):
        credentials = self.get_credentials()
        self.client_id = credentials['id']
        self.client_secret = credentials['secret']
        if self.client_id is None or self.client_secret is None:
            print('Credentials.txt file must have two lines with mappings:\nid:<your client_id here>\nsecret:<your client_secret here>')
            quit()

        token_request = RequestUserAuth(self.client_id, self.client_secret)
        token_request.call()
        token_request.print_response()
        self.access_token = token_request.response

    def get_credentials(self):
        mappings = {}
        with open('credentials.txt','r') as f:
            content = f.readlines()

            for line in content:
                key, value = line.split(':')
                mappings[key] = value
        return mappings

