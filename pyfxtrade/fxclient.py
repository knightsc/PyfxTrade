# Copyright 2013 Scott Knight
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import abc
import hashlib
import json
from httplib2 import Http
from urllib import urlencode
from rate_table import RateTable
from resource import Resource
from account import Account

class FXClient(object):

    __metaclass__ = abc.ABCMeta

    _API_KEY = '68e9c4cec7792f22'

    def __init__(self):
        self.session_token = None
        self.username = None
        self.password = None
        self._accounts = []
        self.rate_table = RateTable(self)

    @abc.abstractmethod
    def _base_url(self):
        """Get the base URL for whichever client type this is"""

    def is_authenticated(self):
        return self.session_token != None and self.session_token != ''

    def _default_params(self):
        return {
            'session_token': self.session_token,
        }

    def _login_params(self):
        # We only really need api_key, username and password
        # This way though we look more like a real client
        return {
            'api_key': FXClient._API_KEY,
            'client_type': 'MOBILE',
            'device_type': 'Android',
            'device_version': 'HTC One',
            'client_version': '2131100208',
            'operating_system': '4.1',
            'device_id': hashlib.md5(self.username).hexdigest()[:16],
            'screen_size': '1024x768',
            'locale': 'English (United States)',
            'connection_type': 'WIFI',
            'network_operator': 't-mobile',
        }

    def _call_method(self, request_method, params=None):
        resource = Resource._RESOURCES[request_method]
        url = '%s%s' % (self._base_url(), resource['url'])
        body = None

        if params:
            if resource['method'] == 'GET':
                url += '?%s' % (urlencode(params))
            else:
                body = urlencode(params)

        http = Http()
        resp, content = http.request(url, resource['method'], body)
        if resp['status'] != '200':
            raise Exception(content)
        else:
            return json.loads(content)

    def login(self, username, password, session_token=None):
        self.username = username
        self.password = password
        self.session_token = session_token

        data = self._login_params()
        data['username'] = self.username
        if session_token:
            data.update(self._default_params())
        else:
            data['password'] = self.password

        resp = self._call_method(Resource.USER_LOGIN, data)

        if not session_token:
            self.session_token = resp['session_token']

    def logout(self):
        self._call_method(Resource.USER_LOGOUT, self._default_params())
        self.session_token = None
        self.username = None
        self.password = None

    def system_info(self):
        resp = self._call_method(Resource.SYSTEM_INFO)
        print resp

    @property
    def accounts(self):
        if not self._accounts:
            data = self._default_params()
            data['username'] = self.username
            resp = self._call_method(Resource.ACCOUNT_LIST, data)

            for a in resp['account_list']:
                account = Account(self)
                account.id = a['id']
                account.name = a['name']
                account.home_currency = a['homecurr']
                account.margin_rate = a['margin_rate']
                for p in a['account_property_name']:
                    account.property_names.append(p)

                self._accounts.append(account)

        return self._accounts

class FXTrade(FXClient):

    def _base_url(self):
        return 'https://fxtrade-webapi.oanda.com/'

class FXGame(FXClient):

    def _base_url(self):
        return 'https://fxgame-webapi.oanda.com/'