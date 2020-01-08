page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.estimator.make_stop_at_checkpoint_step_hook

``` python
tf.contrib.estimator.make_stop_at_checkpoint_step_hook(
    estimator,
    last_step,
    wait_after_file_check_secs=30
)
```



Defined in [`tensorflow/contrib/estimator/python/estimator/hooks.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/estimator/python/estimator/hooks.py).

Creates a proper StopAtCheckpointStepHook based on chief status.