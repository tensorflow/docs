page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.training.HParams

## Class `HParams`





Defined in [`tensorflow/contrib/training/python/training/hparam.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/contrib/training/python/training/hparam.py).

Class to hold a set of hyperparameters as name-value pairs.

A `HParams` object holds hyperparameters used to build and train a model,
such as the number of hidden units in a neural net layer or the learning rate
to use when training.

You first create a `HParams` object by specifying the names and values of the
hyperparameters.

To make them easily accessible the parameter names are added as direct
attributes of the class.  A typical usage is as follows:

```python
# Create a HParams object specifying names and values of the model
# hyperparameters:
hparams = HParams(learning_rate=0.1, num_hidden_units=100)

# The hyperparameter are available as attributes of the HParams object:
hparams.learning_rate ==> 0.1
hparams.num_hidden_units ==> 100
```

Hyperparameters have type, which is inferred from the type of their value
passed at construction type.   The currently supported types are: integer,
float, boolean, string, and list of integer, float, boolean, or string.

You can override hyperparameter values by calling the
[`parse()`](#HParams.parse) method, passing a string of comma separated
`name=value` pairs.  This is intended to make it possible to override
any hyperparameter values from a single command-line flag to which
the user passes 'hyper-param=value' pairs.  It avoids having to define
one flag for each hyperparameter.

The syntax expected for each value depends on the type of the parameter.
See `parse()` for a description of the syntax.

Example:

```python
# Define a command line flag to pass name=value pairs.
# For example using argparse:
import argparse
parser = argparse.ArgumentParser(description='Train my model.')
parser.add_argument('--hparams', type=str,
                    help='Comma separated list of "name=value" pairs.')
args = parser.parse_args()
...
def my_program():
  # Create a HParams object specifying the names and values of the
  # model hyperparameters:
  hparams = tf.HParams(learning_rate=0.1, num_hidden_units=100,
                       activations=['relu', 'tanh'])

  # Override hyperparameters values by parsing the command line
  hparams.parse(args.hparams)

  # If the user passed `--hparams=learning_rate=0.3` on the command line
  # then 'hparams' has the following attributes:
  hparams.learning_rate ==> 0.3
  hparams.num_hidden_units ==> 100
  hparams.activations ==> ['relu', 'tanh']

  # If the hyperparameters are in json format use parse_json:
  hparams.parse_json('{"learning_rate": 0.3, "activations": "relu"}')
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    hparam_def=None,
    model_structure=None,
    **kwargs
)
```

Create an instance of `HParams` from keyword arguments.

The keyword arguments specify name-values pairs for the hyperparameters.
The parameter types are inferred from the type of the values passed.

The parameter names are added as attributes of `HParams` object, so they
can be accessed directly with the dot notation `hparams._name_`.

Example:

```python
# Define 3 hyperparameters: 'learning_rate' is a float parameter,
# 'num_hidden_units' an integer parameter, and 'activation' a string
# parameter.
hparams = tf.HParams(
    learning_rate=0.1, num_hidden_units=100, activation='relu')

hparams.activation ==> 'relu'
```

Note that a few names are reserved and cannot be used as hyperparameter
names.  If you use one of the reserved name the constructor raises a
`ValueError`.

#### Args:

* <b>`hparam_def`</b>: Serialized hyperparameters, encoded as a hparam_pb2.HParamDef
    protocol buffer. If provided, this object is initialized by
    deserializing hparam_def.  Otherwise **kwargs is used.
* <b>`model_structure`</b>: An instance of ModelStructure, defining the feature
    crosses to be used in the Trial.
* <b>`**kwargs`</b>: Key-value pairs where the key is the hyperparameter name and
    the value is the value for the parameter.


#### Raises:

* <b>`ValueError`</b>: If both `hparam_def` and initialization values are provided,
    or if one of the arguments is invalid.



## Methods

<h3 id="__contains__"><code>__contains__</code></h3>

``` python
__contains__(key)
```



<h3 id="add_hparam"><code>add_hparam</code></h3>

``` python
add_hparam(
    name,
    value
)
```

Adds {name, value} pair to hyperparameters.

#### Args:

* <b>`name`</b>: Name of the hyperparameter.
* <b>`value`</b>: Value of the hyperparameter. Can be one of the following types:
    int, float, string, int list, float list, or string list.


#### Raises:

* <b>`ValueError`</b>: if one of the arguments is invalid.

<h3 id="del_hparam"><code>del_hparam</code></h3>

``` python
del_hparam(name)
```

Removes the hyperparameter with key 'name'.

#### Args:

* <b>`name`</b>: Name of the hyperparameter.

<h3 id="from_proto"><code>from_proto</code></h3>

``` python
@staticmethod
from_proto(
    hparam_def,
    import_scope=None
)
```



<h3 id="get"><code>get</code></h3>

``` python
get(
    key,
    default=None
)
```

Returns the value of `key` if it exists, else `default`.

<h3 id="get_model_structure"><code>get_model_structure</code></h3>

``` python
get_model_structure()
```



<h3 id="override_from_dict"><code>override_from_dict</code></h3>

``` python
override_from_dict(values_dict)
```

Override hyperparameter values, parsing new values from a dictionary.

#### Args:

* <b>`values_dict`</b>: Dictionary of name:value pairs.


#### Returns:

The `HParams` instance.


#### Raises:

* <b>`ValueError`</b>: If `values_dict` cannot be parsed.

<h3 id="parse"><code>parse</code></h3>

``` python
parse(values)
```

Override hyperparameter values, parsing new values from a string.

See parse_values for more detail on the allowed format for values.

#### Args:

* <b>`values`</b>: String.  Comma separated list of `name=value` pairs where
    'value' must follow the syntax described above.


#### Returns:

The `HParams` instance.


#### Raises:

* <b>`ValueError`</b>: If `values` cannot be parsed.

<h3 id="parse_json"><code>parse_json</code></h3>

``` python
parse_json(values_json)
```

Override hyperparameter values, parsing new values from a json object.

#### Args:

* <b>`values_json`</b>: String containing a json object of name:value pairs.


#### Returns:

The `HParams` instance.


#### Raises:

* <b>`ValueError`</b>: If `values_json` cannot be parsed.

<h3 id="set_from_map"><code>set_from_map</code></h3>

``` python
set_from_map(values_map)
```

DEPRECATED. Use override_from_dict. (deprecated)

THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use `override_from_dict`.

<h3 id="set_hparam"><code>set_hparam</code></h3>

``` python
set_hparam(
    name,
    value
)
```

Set the value of an existing hyperparameter.

This function verifies that the type of the value matches the type of the
existing hyperparameter.

#### Args:

* <b>`name`</b>: Name of the hyperparameter.
* <b>`value`</b>: New value of the hyperparameter.


#### Raises:

* <b>`ValueError`</b>: If there is a type mismatch.

<h3 id="set_model_structure"><code>set_model_structure</code></h3>

``` python
set_model_structure(model_structure)
```



<h3 id="to_json"><code>to_json</code></h3>

``` python
to_json(
    indent=None,
    separators=None,
    sort_keys=False
)
```

Serializes the hyperparameters into JSON.

#### Args:

* <b>`indent`</b>: If a non-negative integer, JSON array elements and object members
    will be pretty-printed with that indent level. An indent level of 0, or
    negative, will only insert newlines. `None` (the default) selects the
    most compact representation.
* <b>`separators`</b>: Optional `(item_separator, key_separator)` tuple. Default is
    `(', ', ': ')`.
* <b>`sort_keys`</b>: If `True`, the output dictionaries will be sorted by key.


#### Returns:

A JSON string.

<h3 id="to_proto"><code>to_proto</code></h3>

``` python
to_proto(export_scope=None)
```

Converts a `HParams` object to a `HParamDef` protocol buffer.

#### Args:

* <b>`export_scope`</b>: Optional `string`. Name scope to remove.


#### Returns:

A `HParamDef` protocol buffer.

<h3 id="values"><code>values</code></h3>

``` python
values()
```

Return the hyperparameter values as a Python dictionary.

#### Returns:

A dictionary with hyperparameter names as keys.  The values are the
hyperparameter values.



