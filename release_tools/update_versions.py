"""Update tensorflow version in docs."""
import argparse

try:
  import pathlib2 as pathlib
except ImportError:
  import pathlib


EXTS = [".ipynb",".md",".yaml",".html"]

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
    for file in pathlib.Path("site/en").glob("**/*"+ext):
      content = file.read_text()

      content = content.replace(args.old_version.full(), args.new_version.full())
      content = content.replace("github.com/tensorflow/tensorflow/blob/r"+args.old_version.short(),
                                "github.com/tensorflow/tensorflow/blob/r"+args.old_version.short())
      file.write_text(content)
