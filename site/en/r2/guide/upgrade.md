# Upgrade to TensorFlow 2.0

TensorFlow 2.0 release includes many API changes such as argument reorders, API
symbol names, and more. The `tf_upgrade_v2` tool helps the transition by
converting existing TensorFlow 1.12 Python scripts to TensorFlow 2.0 preview.

Note: While the script produces code that runs in TensorFlow 2.0., it *does not*
transform the code to 2.0 best practices.

## Run the script from the pip package

First, install the [TensorFlow pip package](https://www.tensorflow.org/install/pip).

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

Note: `tf_upgrade_v2` is installed automatically by pip install for
TensorFlow 1.13 and later (incl. the nightly 2.0 builds).

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

## Caveats

- Do not update parts of your code manually before running this script. In
particular, functions that have had reordered arguments like `tf.argmax`
or `tf.batch_to_space` cause the script to incorrectly add keyword
arguments that mismap arguments.
- This script does not reorder arguments. Instead, the script adds keyword
arguments to functions that have their arguments reordered.
- The conversion process is not able to upgrade all functions. One notable
example is `tf.nn.conv2d` which no longer takes the `use_cudnn_on_gpu` argument.
If the script detects this, it will report to stdout (and in the report) and you
can fix it manually. For example if you have
`tf.nn.conv2d(inputs, filters, strides, padding, use_cudnn_on_gpu=True)`
you will need to change it to: `tf.nn.conv2d(input, filters, strides, padding)`.

## Bugs

To report upgrade script bugs or make feature requests, file an issue on [GitHub](https://github.com/tensorflow/tensorflow/issues).
