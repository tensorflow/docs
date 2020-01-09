page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.ExecutionCallback


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/eager/execution_callbacks.py#L34-L49">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `ExecutionCallback`

Valid callback actions.



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
