
# https://users.flatironinstitute.org/~mrenzo/publications.html
# https://orcid.org/0000-0002-6718-9472
import requests
import json

orcid_id = '0000-0002-6718-9472'
public_orcid_url = "http://pub.orcid.org/{}".format(orcid_id)
public_orcid_url_general = "http://pub.orcid.org"

resp = requests.get(public_orcid_url,
                    headers={'Accept':'application/orcid+json'})
results = resp.json()
# print(results.keys())

# print(results['person'])
# print(json.dumps(results, indent=4))

print(results.keys())
print(results['person'])
quit()
works = results['activities-summary']['works']['group']

for work_dict in works:
    work_object = work_dict['work-summary'][0]

    # print(work_object)
    title = work_object['title']['title']['value']

    print(work_object.keys())

    print(work_object['path'])

    work_object_path_code = work_object['path']
    work_object_full_url = public_orcid_url_general+work_object_path_code
    print(work_object_full_url)

    work_resp = requests.get(work_object_full_url,
                        headers={'Accept':'application/orcid+json'})
    work_results = work_resp.json()
    print(work_results)