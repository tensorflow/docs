description: Functions used to extract and analyze stacks.  Faster than Python libs.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.tf_decorator.tf_stack" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.compat.v1.flags.tf_decorator.tf_stack

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/util/tf_stack.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Functions used to extract and analyze stacks.  Faster than Python libs.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.app.flags.tf_decorator.tf_stack`</p>
</p>
</section>



## Classes

[`class CurrentModuleFilter`](../../../../../tf/compat/v1/flags/tf_decorator/tf_stack/CurrentModuleFilter.md): Filters stack frames from the module where this is used (best effort).

[`class FrameSummary`](../../../../../tf/compat/v1/flags/tf_decorator/tf_stack/FrameSummary.md)

[`class StackSummary`](../../../../../tf/compat/v1/flags/tf_decorator/tf_stack/StackSummary.md)

[`class StackTraceFilter`](../../../../../tf/compat/v1/flags/tf_decorator/tf_stack/StackTraceFilter.md): Allows filtering traceback information by removing superfluous frames.

[`class StackTraceMapper`](../../../../../tf/compat/v1/flags/tf_decorator/tf_stack/StackTraceMapper.md): Allows remapping traceback information to different source code.

[`class StackTraceTransform`](../../../../../tf/compat/v1/flags/tf_decorator/tf_stack/StackTraceTransform.md): Base class for stack trace transformation functions.

## Functions

[`extract_stack(...)`](../../../../../tf/compat/v1/flags/tf_decorator/tf_stack/extract_stack.md): A lightweight, extensible re-implementation of traceback.extract_stack.

