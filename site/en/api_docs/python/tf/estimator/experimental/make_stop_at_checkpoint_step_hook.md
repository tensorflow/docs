page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.experimental.make_stop_at_checkpoint_step_hook


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/hooks/hooks.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates a proper StopAtCheckpointStepHook based on chief status.

### Aliases:

* `tf.compat.v1.estimator.experimental.make_stop_at_checkpoint_step_hook`
* `tf.compat.v2.estimator.experimental.make_stop_at_checkpoint_step_hook`


``` python
tf.estimator.experimental.make_stop_at_checkpoint_step_hook(
    estimator,
    last_step,
    wait_after_file_check_secs=30
)
```



<!-- Placeholder for "Used in" -->
