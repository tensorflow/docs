# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
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
"""Update tensorflow version in docs. Run this from the repo-root."""
import argparse
import re

try:
  import pathlib2 as pathlib
except ImportError:
  import pathlib


EXTS = [".ipynb",".md",".yaml",".html"]
EXPAND_TABLES = [
    "source_windows.md",
    "source.md",]

class Version(object):
  def __init__(self, in_string):
    self.major, self.minor, self.patch = in_string.split(".")
    assert self.major.isdigit()
    assert self.minor.isdigit()
    assert self.patch.isdigit()

  def full(self):
    return ".".join([self.major, self.minor, self.patch])

  def short(self):
    return ".".join([self.major, self.minor])


parser = argparse.ArgumentParser()
parser.add_argument("--old_version", type=Version, required=True,
                    help="The old version to replace")
parser.add_argument("--new_version", type=Version, required=True,
                    help="The new version to replace it with")

if __name__=="__main__":
  args = parser.parse_args()

  for ext in EXTS:
    for file_path in pathlib.Path(".").rglob("*"+ext):
      content = file_path.read_text()
      if file_path.name in EXPAND_TABLES:
        content = re.sub("(<tr>.*?){}(.*?</tr>)".format(re.escape(args.old_version.short())),
                         r"\g<1>{}\g<2>\n\g<0>".format(args.new_version.short()), content)
        file_path.write_text(content)
        continue

      content = file_path.read_text()

      content = content.replace(args.old_version.full(), args.new_version.full())
      content = content.replace("github.com/tensorflow/tensorflow/blob/r"+args.old_version.short(),
                                "github.com/tensorflow/tensorflow/blob/r"+args.old_version.short())
      file_path.write_text(content)
