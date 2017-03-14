import pytest
import requests
import ckan_browser as cb


def test_fetch():
    data = cb.fetch('http://beta.ckan.org/api/3/action/package_list')
    assert type(data) == dict
    assert data['result']
    nodata = cb.fetch('http://beta.ckan.org/api/3/action/package_list3')
    assert nodata == None


def test_validate_url():
    assert cb.validate_url('http://beta.ckan.org/') == 'http://beta.ckan.org'
    assert cb.validate_url('http://beta.ckan.org') == 'http://beta.ckan.org'
    assert cb.validate_url('beta.ckan.org') == 'http://beta.ckan.org'


def test_get_datasets():
    datasets = cb.get_datasets('http://beta.ckan.org')
    assert type(datasets) == list
    assert 'annual-survey-of-manufactures-asm' in datasets
    nodatasets = cb.get_datasets('http://example.com')
    assert nodatasets == None


def test_count_datasets():
    count = cb.count_datasets('http://beta.ckan.org')
    assert count == 15


def test_get_dataset():
    dataset = cb.get_dataset('http://beta.ckan.org', \
        'annual-survey-of-manufactures-asm')
    assert type(dataset) == dict
    assert dataset['title'] == "Annual survey of manufactures (ASM),"
    nodataset = cb.get_datasets('http://example.com')
    assert nodataset == None


def test_count_resources():
    count = cb.count_resources('http://beta.ckan.org')
    assert type(count) == dict
    assert count['internal'] == 9
    assert count['external'] == 8
    assert count['total'] == 17