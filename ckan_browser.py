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
        return print('A %d error occured while fetching the data. \
            Please check the URL and try again.' % (r.status_code))
    try:
        data = r.json()
    except JSONDecodeError:
        return print('An error occured while decoding the data. \
            Please check the URL and try again.')
    if data['success'] != True:
        try:
            error = data['error']
        except KeyError:
            error = None
        if error:
            return print('A %d error occured while fetching the data. \
                Please check the URL and try again.' % (error))
        else:
            return print('An error occured while fetching the data. \
                Please check the URL and try again.')

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
    return url
