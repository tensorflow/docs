page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.ExecutionCallback

## Class `ExecutionCallback`





Defined in [`tensorflow/python/eager/execution_callbacks.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/eager/execution_callbacks.py).

Valid callback actions.

These can be passed to `seterr` or `errstate` to create callbacks when
specific events occur (e.g. an operation produces `NaN`s).

IGNORE: take no action.
PRINT:  print a warning to `stdout`.
RAISE:  raise an error (e.g. `InfOrNanError`).
WARN:   print a warning using <a href="../../../tf/logging/warn"><code>tf.logging.warn</code></a>.

## Class Members

<h3 id="IGNORE"><code>IGNORE</code></h3>

<h3 id="PRINT"><code>PRINT</code></h3>

<h3 id="RAISE"><code>RAISE</code></h3>

<h3 id="WARN"><code>WARN</code></h3>

<h3 id="__members__"><code>__members__</code></h3>

