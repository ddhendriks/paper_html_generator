import orcid
import requests

client_id = 'APP-BIBWOT29ECF0QZ2W'
client_secret = '90dd3f0e-3a89-405e-aef4-57f5af9bfe75'

# api = orcid.PublicAPI(institution_key, institution_secret, sandbox=True)
# token = api.get_token_from_authorization_code(authorization_code,
#                                               redirect_uri)
# search_token = api.get_search_token_from_orcid()

# search_results = api.search('text:English', access_token=Token)


# token_url = 'https://sandbox.orcid.org/oauth/token'
token_url = 'https://sandbox.orcid.org/oauth/token'
header = {"Accept": "application/json"}

data = {
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'client_credentials',
    'scope': '/read-public'
}

resp = requests.post(token_url, data=data, headers=header)
print(dir(resp))
print(resp.text)

print(resp[''])