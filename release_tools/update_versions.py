"""Update tensorflow version in docs."""
import argparse

try:
  import pathlib2 as pathlib
except ImportError:
  import pathlib


EXTS = [".ipynb",".md",".yaml",".html"]
SKIP = [
    "site/en/install/source_windows.md",
    "site/en/install/source.md",]

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
    for file_path in pathlib.Path("site/en").glob("**/*"+ext):
      if str(file_path) in SKIP:
        continue

      content = file_path.read_text()

      content = content.replace(args.old_version.full(), args.new_version.full())
      content = content.replace("github.com/tensorflow/tensorflow/blob/r"+args.old_version.short(),
                                "github.com/tensorflow/tensorflow/blob/r"+args.old_version.short())
      file_path.write_text(content)
