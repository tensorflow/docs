page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.compat.v1.flags.tf_decorator.tf_stack


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/util/tf_stack.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Functions used to extract and analyze stacks.  Faster than Python libs.

### Aliases:

* Module `tf.compat.v1.app.flags.tf_decorator.tf_stack`


<!-- Placeholder for "Used in" -->


## Classes

[`class CurrentModuleFilter`](../../../../../tf/compat/v1/flags/tf_decorator/tf_stack/CurrentModuleFilter): Filters stack frames from the module where this is used (best effort).

[`class FileAndLine`](../../../../../tf/compat/v1/flags/tf_decorator/tf_stack/FileAndLine): FileAndLine(file, line)

[`class StackTraceFilter`](../../../../../tf/compat/v1/flags/tf_decorator/tf_stack/StackTraceFilter): Allows filtering traceback information by removing superfluous frames.

[`class StackTraceMapper`](../../../../../tf/compat/v1/flags/tf_decorator/tf_stack/StackTraceMapper): Allows remapping traceback information to different source code.

[`class StackTraceTransform`](../../../../../tf/compat/v1/flags/tf_decorator/tf_stack/StackTraceTransform): Base class for stack trace transformation functions.

## Functions

[`convert_stack(...)`](../../../../../tf/compat/v1/flags/tf_decorator/tf_stack/convert_stack): Converts a stack extracted using extract_stack() to a traceback stack.

[`extract_stack(...)`](../../../../../tf/compat/v1/flags/tf_decorator/tf_stack/extract_stack): A lightweight, extensible re-implementation of traceback.extract_stack.

[`extract_stack_file_and_line(...)`](../../../../../tf/compat/v1/flags/tf_decorator/tf_stack/extract_stack_file_and_line): A version of extract_stack that only returns filenames and line numbers.

## Other Members

* `EMPTY_FROZEN_MAP` <a id="EMPTY_FROZEN_MAP"></a>
* `EMPTY_FROZEN_SET` <a id="EMPTY_FROZEN_SET"></a>
* `TB_CODEDICT = 3` <a id="TB_CODEDICT"></a>
* `TB_FILENAME = 0` <a id="TB_FILENAME"></a>
* `TB_FUNCNAME = 2` <a id="TB_FUNCNAME"></a>
* `TB_LINENO = 1` <a id="TB_LINENO"></a>
