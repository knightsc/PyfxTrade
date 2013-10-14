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

class RateTable(object):

    INTERVAL_5_SEC = 5
    INTERVAL_10_SEC = 10
    INTERVAL_30_SEC = 30
    INTERVAL_1_MIN = 60
    INTERVAL_5_MIN = 300
    INTERVAL_15_MIN = 900
    INTERVAL_30_MIN = 1800
    INTERVAL_1_HOUR = 3600
    INTERVAL_3_HOUR = 10800
    INTERVAL_4_HOUR = 14400
    INTERVAL_8_HOUR = 28800
    INTERVAL_1_DAY = 86400

    def __init__(self, fxclient):
        self._fxclient = fxclient