# Upgrading your code to TensorFlow 2.0

TensorFlow 2.0 will include many API changes, such as reordering arguments, renaming symbols, and changing default values for parameters. Manually performing all of these modifications would be tedious, and prone to error. To streamline the changes, and to make your transition to TF 2.0 as seamless as possible, the TensorFlow engineering team has created a `tf_upgrade_v2` utility that will help transition legacy code to the new API.

The `tf_upgrade_v2` utility is included automatically with a pip install of TF 2.0, and will help accelerate your upgrade processes by converting existing TensorFlow 1.13 Python scripts to TensorFlow 2.0.

We have attempted to automate as many of the upgrade tasks as possible: however, there are still syntactical and stylistic changes that cannot be performed by the script.

Certain API symbols cannot be upgraded simply by using a string replacement. To ensure your code is still supported in TensorFlow 2.0, the upgrade script includes a `compat.v1` module. This module will replace calls of the form `tf.foo` with equivalent `tf.compat.v1.foo` references. It is recommended, however, to manually proofread such replacements and migrate them to new APIs in `tf.*` namespace instead of `tf.compat.v1.*` namespace as quickly as feasible.

Furthermore, due to module deprecations (for example, `tf.flags` and `tf.contrib`), TensorFlow 2.0 will include changes that cannot be worked around by switching to `compat.v1`. Upgrading code that uses these modules might require using an additional library (for e.g. `absl.flags`) or switching to a package in [`tensorflow/addons`](http://www.github.com/tensorflow/addons).

If you want to try upgrading your models from TensorFlow 1.12 to TensorFlow 2.0, follow the instructions below.

## Run the script from the pip package

First, `pip` install `tf-nightly-2.0-preview` or `tf-nightly-gpu-2.0-preview`.

**Note**: `tf_upgrade_v2` is installed automatically for TensorFlow 1.13 and later (including the nightly TF 2.0 builds).

The upgrade script can be run on a single Python file:

```sh
tf_upgrade_v2 --infile foo.py --outfile foo-upgraded.py
```

This prints a list of errors that the script *can not* fix. You can also run
it on a directory tree:

```
# upgrade the .py files and copy all the other files to the outtree
tf_upgrade_v2 --intree coolcode --outtree coolcode-upgraded

# just upgrade the .py files
tf_upgrade_v2 --intree coolcode --outtree coolcode-upgraded --copyotherfiles False
```

## Detailed report

The script also reports a list of detailed changes, for example:

```
'tensorflow/tools/compatibility/testdata/test_file_v1_12.py' Line 65
--------------------------------------------------------------------------------

Added keyword 'input' to reordered function 'tf.argmax'
Renamed keyword argument from 'dimension' to 'axis'

    Old:         tf.argmax([[1, 3, 2]], dimension=0))
                                        ~~~~~~~~~~
    New:         tf.argmax(input=[[1, 3, 2]], axis=0))

```
All of this information is included in the `report.txt` file that will be exported to your current directory. Once `tf_upgrade_v2` has run and exported your upgraded script, you can run your model and check to ensure your outputs are similar to TF 1.x.

## Caveats

- **Do not update parts of your code manually before running this script.** In particular, functions that have had reordered arguments like tf.argmax or tf.batch_to_space cause the script to incorrectly add keyword arguments that mismap your existing code.

- **This script does not reorder arguments.**  Instead, the script adds keyword arguments to functions that have their arguments reordered.

To report upgrade script bugs or make feature requests, file an issue on [GitHub ](https://github.com/tensorflow/tensorflow/issues)— and if you’re testing TensorFlow 2.0, we want to hear about it! Please feel free to join the [TF 2.0 Testing community](https://groups.google.com/a/tensorflow.org/forum/?utm_medium=email&utm_source=footer#!forum/testing) and send questions and discussion to [testing@tensorflow.org](mailto:testing@tensorflow.org).
