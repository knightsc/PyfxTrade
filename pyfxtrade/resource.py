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

class Resource(object):
    USER_LOGIN = 0
    USER_LOGOUT = 1
    ACCOUNT_LIST = 2
    ACCOUNT_STATUS = 3
    SYSTEM_INFO = 4

    _RESOURCES = {
        USER_LOGIN: {'url': 'v1/user/login.json', 'method': 'POST'},
        USER_LOGOUT: {'url': 'v1/user/logout.json', 'method': 'POST'},
        ACCOUNT_LIST: {'url': 'v1/account/list.json', 'method': 'GET'},
        ACCOUNT_STATUS: {'url': 'v1/account/status.json', 'method': 'GET'},
        SYSTEM_INFO: {'url': 'v1/system/info.json', 'method': 'GET'}
    }