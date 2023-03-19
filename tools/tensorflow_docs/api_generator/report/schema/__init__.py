# Copyright 2020 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Public API for api report proto."""

import sys

from google import protobuf

_version_parts = protobuf.__version__.split('.')
_version = (int(_version_parts[0]), int(_version_parts[1]))

if _version >= (3, 20):
  from tensorflow_docs.api_generator.report.schema import api_report_generated_pb2 as api_report_pb2  # pylint: disable=g-import-not-at-top
else:
  from tensorflow_docs.api_generator.report.schema import api_report_generated_319_pb2 as api_report_pb2  # pylint: disable=g-import-not-at-top

sys.modules['tensorflow_docs.api_generator.report.schema.api_report_pb2'] = (
    api_report_pb2
)
