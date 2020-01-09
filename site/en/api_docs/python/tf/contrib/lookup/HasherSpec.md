page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.lookup.HasherSpec


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/lookup_ops.py#L782-L794">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `HasherSpec`

A structure for the spec of the hashing function to use for hash buckets.



<!-- Placeholder for "Used in" -->

`hasher` is the name of the hashing function to use (eg. "fasthash",
"stronghash").
`key` is optional and specify the key to use for the hash function if
supported, currently only used by a strong hash.

#### Fields:


* <b>`hasher`</b>: The hasher name to use.
* <b>`key`</b>: The key to be used by the hashing function, if required.

<h2 id="__new__"><code>__new__</code></h2>

``` python
__new__(
    _cls,
    hasher,
    key
)
```

Create new instance of HasherSpec(hasher, key)




## Properties

<h3 id="hasher"><code>hasher</code></h3>




<h3 id="key"><code>key</code></h3>
