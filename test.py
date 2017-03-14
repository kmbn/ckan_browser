import pytest
import requests
import ckan_browser as cb


def test_fetch():
    data = cb.fetch('http://beta.ckan.org/api/3/action/package_list')
    assert type(data) == dict
    assert data['result']