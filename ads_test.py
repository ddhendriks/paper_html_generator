ads_token = 'TwlQ1tQFwitk9K6YbZSNg5XsGcf8FYZMJ8PcQM8y'

from astroquery import nasa_ads as na


class paper():
    def __init__(self, title, authors, is_first_author, doi, bibcode, pub, pubdate):
        self.title = title
        self.authors = authors
        self.is_first_author = is_first_author
        self.doi = doi
        self.bibcode = bibcode
        self.pub = pub
        self.pubdate = pubdate

    def to_html():
        pass

    def __str__(self):
        return "{}: {}".format(self.title, " ".join(self.authors))

def check_if_first_author(authors, first_name, last_name):
    """
    Function to check if the current person is the main author
    """
    is_first_author = False

    first_author = authors[0]
    if ',' in first_author:
        split_first_author = first_author.split(',')

        # Check if they match
        is_first_author = split_first_author[0]==last_name

    return is_first_author




na.ADS.TOKEN = ads_token
na.ADS.NROWS = 100

orcid_id = '0000-0002-6718-9472'
first_name = 'Mathieu'
last_name = 'Renzo'

res = na.ADS.query_simple('orcid:0000-0002-6718-9472')

papers_list = []

#
for el in res:
    #
    title = el['title'][0]
    bibcode = el['bibcode']
    doi = el['doi']
    authors = el['author']
    eid = el['eid']
    pubdate = el['pubdate']
    pub = el['pub']


    is_first_author = check_if_first_author(authors, first_name, last_name)
    print(authors)
    print(is_first_author)

    #
    cur_paper = paper(title, authors, is_first_author, doi, bibcode, pub, pubdate)

    papers_list.append(cur_paper)

print(papers_list[0])

