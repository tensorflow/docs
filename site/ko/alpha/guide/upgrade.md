# Upgrade code to TensorFlow 2.0

TensorFlow 2.0 includes many API changes, such as reordering arguments, renaming symbols, and changing default values for parameters. Manually performing all of these modifications would be tedious and prone to error. To streamline the changes, and to make your transition to TF 2.0 as seamless as possible, the TensorFlow team has created the `tf_upgrade_v2` utility to help transition legacy code to the new API.

The `tf_upgrade_v2` utility is included automatically with a `pip install` of TF 2.0. It will accelerate your upgrade process by converting existing TensorFlow 1.x Python scripts to TensorFlow 2.0.

The conversion script automates as much as possible, but there are still syntactical and stylistic changes that cannot be performed by the script.

## Compatibility module

Certain API symbols can not be upgraded simply by using a string replacement. To ensure your code is still supported in TensorFlow 2.0, the upgrade script includes a `compat.v1` module. This module replaces TF 1.x symbols like `tf.foo` with the equivalent `tf.compat.v1.foo` reference. While the compatibility module is nice, we recommend that you manually proofread replacements and migrate them to new APIs in the `tf.*` namespace instead of `tf.compat.v1.*` namespace as quickly as possible.

Because of TensorFlow 2.x module deprecations (for example, `tf.flags` and `tf.contrib`), some changes can not be worked around by switching to `compat.v1`. Upgrading this code may require using an additional library (for example, `absl.flags`) or switching to a package in [tensorflow/addons](http://www.github.com/tensorflow/addons).

## Upgrade script

To convert your code from TensorFlow 1.x to TensorFlow 2.x, follow these instructions:

### Run the script from the pip package

First, `pip install` the `tensorflow==2.0.0-alpha0` or `tensorflow-gpu==2.0.0-alpha0` package.

Note: `tf_upgrade_v2` is installed automatically for TensorFlow 1.13 and later (including the nightly TF 2.0 builds).

The upgrade script can be run on a single Python file:

```sh
tf_upgrade_v2 --infile tensorfoo.py --outfile tensorfoo-upgraded.py
```

The script will print errors if it can not find a fix for the code. You can also run it on a directory tree:

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

- Do not update parts of your code manually before running this script. In particular, functions that have had reordered arguments like `tf.argmax` or `tf.batch_to_space` cause the script to incorrectly add keyword arguments that mismap your existing code.

- The script assumes that `tensorflow` is imported using `import tensorflow as tf`.

- This script does not reorder arguments. Instead, the script adds keyword arguments to functions that have their arguments reordered.

- Check out [tf2up.ml](http://tf2up.ml) for a convenient tool to upgrade Jupyter
  notebooks and Python files in a GitHub repository.

To report upgrade script bugs or make feature requests, please file an issue on [GitHub](https://github.com/tensorflow/tensorflow/issues). And if you’re testing TensorFlow 2.0, we want to hear about it! Join the [TF 2.0 Testing community](https://groups.google.com/a/tensorflow.org/forum/#!forum/testing) and send questions and discussion to [testing@tensorflow.org](mailto:testing@tensorflow.org).
