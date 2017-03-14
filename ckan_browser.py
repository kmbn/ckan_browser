"""
A module for retrieving basic data from the CKAN API (version 3).

"""

import requests


def fetch(url):
    """
    Takes a complete API URL, fetches content from the API,
    and returns a dictionary containing the contents of the repsonse
    (i.e., 'result' as well as 'help', 'success', etc.).

    """
    r = requests.get(url=url)

    # Make sure the request succeeded and the data loads.
    if r.status_code != 200:
        print('A %d error occured while fetching the data. \
            Please check the URL and try again.' % (r.status_code))
        return None
    try:
        data = r.json()
    except JSONDecodeError:
        print('An error occured while decoding the data. \
            Please check the URL and try again.')
        return None
    if data['success'] != True:
        try:
            error = data['error']
        except KeyError:
            error = None
        if error:
            print('A %d error occured while fetching the data. \
                Please check the URL and try again.' % (error))
            return None
        else:
            print('An error occured while fetching the data. \
                Please check the URL and try again.')
            return None

    return data


def validate_url(url):
    """
    Check and if possible clean up the URL entered by the user.
    Currently just removes a trailing / if present when the user enters
    the URL of the website so that the concatenated address is OK,
    but could be expanded.

    """
    if url[-1] == '/':
        url = url[:-1]
    if url[:7] != 'http://':
        url = 'http://' + url
    return url


def get_datasets(site_url):
    """
    Takes the URL of the site (i.e., 'http://beta.ckan.org')
    and returns a list containg the names of the available datasets.

    """
    site_url = validate_url(site_url)
    data = fetch(site_url + '/api/3/action/package_list')
    if not data:
        print('Could not get datasets.')
        return None
    datasets = data['result']
    return datasets


def count_datasets(site_url):
    """
    Takes the URL of the site (i.e., 'http://beta.ckan.org') and returns
    an integer representing the number of available datasets.

    """
    datasets = get_datasets(site_url)
    count = len(datasets)
    return count


def get_dataset(site_url, name):
    """
    Takes the URL of the site (i.e., 'http://beta.ckan.org') and the name of
    the dataset and returns a dict containing a given dataset.

    """
    site_url = validate_url(site_url)
    data = fetch(site_url + '/api/3/action/package_show?id=' + name)
    if not data:
        print('Could not get dataset.')
        return None
    dataset = data['result']
    return dataset


def count_resources(site_url):
    """
    Takes the URL of the site (i.e., 'http://beta.ckan.org') and returns
    a dict with the number of internal/uploaded resources,
    the number of external/linked resources,
    and the total number of resources.

    """
    site_url = validate_url(site_url)

    # NOTE:
    # Using the 'package_list_with_resources' action would seem to be
    # simpler and faster, but it does not return all of the datasets
    # (currently, it returns 10 rather than 15 datasets), so we're going to
    # take a two-step approach here.

    # Get a list of all the datasets.
    datasets = get_datasets(site_url)
    internal = 0
    external = 0
    # Fetch each dataset and count the number int/ext resources in each.
    for i in datasets:
        dataset = get_dataset(site_url, i)
        for resource in dataset['resources']:
            if resource['url_type'] == 'upload':
                internal += 1
            else:
                external += 1
    count = {'internal': internal, 'external': external, \
        'total': internal + external}
    return count