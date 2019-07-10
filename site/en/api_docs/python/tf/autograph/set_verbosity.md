page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.autograph.set_verbosity

Sets the AutoGraph verbosity level.

### Aliases:

* `tf.autograph.set_verbosity`
* `tf.compat.v1.autograph.set_verbosity`
* `tf.compat.v2.autograph.set_verbosity`

``` python
tf.autograph.set_verbosity(
    level,
    alsologtostdout=False
)
```



Defined in [`python/autograph/utils/ag_logging.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/autograph/utils/ag_logging.py).

<!-- Placeholder for "Used in" -->

_Debug logging in AutoGraph_

More verbose logging is useful to enable when filing bug reports or doing
more in-depth debugging.

There are two controls that control the logging verbosity:

 * The `set_verbosity` function

 * The `AUTOGRAPH_VERBOSITY` environment variable

`set_verbosity` takes precedence over the environment variable.

#### For example:



```python
import os
import tensorflow as tf

os.environ['AUTOGRAPH_VERBOSITY'] = 5
# Verbosity is now 5

tf.autograph.set_verbosity(0)
# Verbosity is now 0

os.environ['AUTOGRAPH_VERBOSITY'] = 1
# No effect, because set_verbosity was already called.
```

Logs entries are output to [absl](https://abseil.io)'s default output,
with `INFO` level.
Logs can be mirrored to stdout by using the `alsologtostdout` argument.
Mirroring is enabled by default when Python runs in interactive mode.

#### Args:


* <b>`level`</b>: int, the verbosity level; larger values specify increased verbosity;
  0 means no logging. When reporting bugs, it is recommended to set this
  value to a larges number, like 10.
* <b>`alsologtostdout`</b>: bool, whether to also output log messages to `sys.stdout`.