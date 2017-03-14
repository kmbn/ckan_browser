A module for retrieving basic data from the CKAN API (version 3), including the number of datasets available, the individual datasets themselves, and the number of internal and external resources.

# Requirements
The module is written in Python 3 and requires `Requests`. The tests require `pytest`. To install the requirements, do `pip install -r /path/to/requirements.txt`. If you're already in the directory containing the module, just do `pip install -r requirements.txt`. You may want to set up a virtual environment first.

# Usage
Import the module:
`import ckan_browser as cb`

Retrieve a dataset:
`dataset = cb.get_dataset(site_url, name_of_dataset)`, where site_url is the URL of the website in quotes (e.g., 'beta.ckan.org') and name_of_dataset is the name of the dataset in quotes (e.g., 'annual-survey-of-manufactures-asm'). For a quick test, try: `cb.get_dataset('http://beta.ckan.org', 'annual-survey-of-manufactures-asm')`.
`dataset` will be a dictionary. View all of it with `print(dataset)` or try `print(dataset['title'])` to view only its title.

Get the number of datasets on a site:
`cb.count_datasets(site_url)`, where `site_url` is the URL of the website in quotes (e.g., 'beta.ckan.org'). Try: `cb.count_datasets('beta.ckan.org')`

Get the number of internal and external resources on a site:
`cb.count_resources(site_url)`, where `site_url` is the URL of the website in quotes (e.g., 'beta.ckan.org'). The result will be dictionary containing the number of internal resources, the number of external resources, and the total number of resources. Try: `cb.count_resources('beta.ckan.org')`

# Tests
All of the functions are tested. To run the tests, `cd` to the directory containing the `ckan_browser.py` and `test.py` and then do `pytest`.