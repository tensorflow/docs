page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.keras.initializers.lecun_normal


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/init_ops_v2.py#L631-L654">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



LeCun normal initializer.

### Aliases:

* <a href="/api_docs/python/tf/compat/v2/keras/initializers/lecun_normal"><code>tf.compat.v2.initializers.lecun_normal</code></a>


``` python
tf.compat.v2.keras.initializers.lecun_normal(seed=None)
```



<!-- Placeholder for "Used in" -->

It draws samples from a truncated normal distribution centered on 0
with `stddev = sqrt(1 / fan_in)`
where `fan_in` is the number of input units in the weight tensor.

#### Arguments:


* <b>`seed`</b>: A Python integer. Used to seed the random generator.


#### Returns:

An initializer.



#### References:

- Self-Normalizing Neural Networks,
[Klambauer et al., 2017]
(https://papers.nips.cc/paper/6698-self-normalizing-neural-networks)
([pdf]
(https://papers.nips.cc/paper/6698-self-normalizing-neural-networks.pdf))
- Efficient Backprop,
[Lecun et al., 1998](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)
