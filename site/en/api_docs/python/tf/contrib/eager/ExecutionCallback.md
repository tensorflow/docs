page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.ExecutionCallback

## Class `ExecutionCallback`

Valid callback actions.





Defined in [`python/eager/execution_callbacks.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/eager/execution_callbacks.py).

<!-- Placeholder for "Used in" -->

These can be passed to `seterr` or `errstate` to create callbacks when
specific events occur (e.g. an operation produces `NaN`s).

IGNORE: take no action.
PRINT:  print a warning to `stdout`.
RAISE:  raise an error (e.g. `InfOrNanError`).
WARN:   print a warning using <a href="../../../tf/logging/warn"><code>tf.compat.v1.logging.warn</code></a>.

## Class Members

* `IGNORE` <a id="IGNORE"></a>
* `PRINT` <a id="PRINT"></a>
* `RAISE` <a id="RAISE"></a>
* `WARN` <a id="WARN"></a>
