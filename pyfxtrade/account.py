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

from resource import Resource

class Account(object):

    def __init__(self, fxclient):
        self._fxclient = fxclient
        self.id = None
        self.name = None
        self.property_names = []
        self.home_currency = None
        self.margin_rate = None
        self.balance = None
        self.unrealized_pl = None
        self.realized_pl = None
        self.nav = None
        self.margin_used = None
        self.margin_available = None
        self.open_trades = None
        self.open_orders = None

    def _load_account_status(self):
        data = object.__getattribute__(self, '_fxclient')._default_params()
        data['account_id'] = object.__getattribute__(self, 'id')
        info = object.__getattribute__(self, '_fxclient')._call_method(Resource.ACCOUNT_STATUS, data)
        object.__setattr__(self, 'balance', info['balance'])
        object.__setattr__(self, 'unrealized_pl', info['unrealized_pl'])
        object.__setattr__(self, 'realized_pl', info['realized_pl'])
        object.__setattr__(self, 'nav', info['nav'])
        object.__setattr__(self, 'margin_used', info['margin_used'])
        object.__setattr__(self, 'margin_available', info['margin_avail'])
        object.__setattr__(self, 'open_trades', info['open_trades'])
        object.__setattr__(self, 'open_orders', info['open_orders'])

    def __getattribute__(self, name):
        if not object.__getattribute__(self, 'balance'):
            object.__getattribute__(self, '_load_account_status')()

        return object.__getattribute__(self, name)
