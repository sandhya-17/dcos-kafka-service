#
#    Copyright (C) 2015 Mesosphere, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from common import exec_command


def test_help():
    returncode, stdout, stderr = exec_command(
        ['dcos-kafka', 'kafka', 'help'])

    assert returncode == 0
    assert stdout.startswith(b"Usage:")
    assert stderr == b''