page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.test.StubOutForTesting

## Class `StubOutForTesting`

Support class for stubbing methods out for unit testing.



### Aliases:

* Class `tf.compat.v1.test.StubOutForTesting`
* Class `tf.test.StubOutForTesting`



Defined in [`python/platform/googletest.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/platform/googletest.py).

<!-- Placeholder for "Used in" -->


#### Sample Usage:



You want os.path.exists() to always return true during testing.

   stubs = StubOutForTesting()
   stubs.Set(os.path, 'exists', lambda x: 1)
     ...
   stubs.CleanUp()

The above changes os.path.exists into a lambda that returns 1.  Once
the ... part of the code finishes, the CleanUp() looks up the old
value of os.path.exists and restores it.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__()
```






## Methods

<h3 id="CleanUp"><code>CleanUp</code></h3>

``` python
CleanUp()
```

Undoes all SmartSet() & Set() calls, restoring original definitions.


<h3 id="Set"><code>Set</code></h3>

``` python
Set(
    parent,
    child_name,
    new_child
)
```

In parent, replace child_name's old definition with new_child.

The parent could be a module when the child is a function at
module scope.  Or the parent could be a class when a class' method
is being replaced.  The named child is set to new_child, while the
prior definition is saved away for later, when UnsetAll() is
called.

This method supports the case where child_name is a staticmethod or a
classmethod of parent.

#### Args:


* <b>`parent`</b>: The context in which the attribute child_name is to be changed.
* <b>`child_name`</b>: The name of the attribute to change.
* <b>`new_child`</b>: The new value of the attribute.

<h3 id="SmartSet"><code>SmartSet</code></h3>

``` python
SmartSet(
    obj,
    attr_name,
    new_attr
)
```

Replace obj.attr_name with new_attr.

This method is smart and works at the module, class, and instance level
while preserving proper inheritance. It will not stub out C types however
unless that has been explicitly allowed by the type.

This method supports the case where attr_name is a staticmethod or a
classmethod of obj.

#### Notes:

- If obj is an instance, then it is its class that will actually be
  stubbed. Note that the method Set() does not do that: if obj is
  an instance, it (and not its class) will be stubbed.
- The stubbing is using the builtin getattr and setattr. So, the __get__
  and __set__ will be called when stubbing (TODO: A better idea would
  probably be to manipulate obj.__dict__ instead of getattr() and
  setattr()).



#### Args:


* <b>`obj`</b>: The object whose attributes we want to modify.
* <b>`attr_name`</b>: The name of the attribute to modify.
* <b>`new_attr`</b>: The new value for the attribute.


#### Raises:


* <b>`AttributeError`</b>: If the attribute cannot be found.

<h3 id="SmartUnsetAll"><code>SmartUnsetAll</code></h3>

``` python
SmartUnsetAll()
```

Reverses SmartSet() calls, restoring things to original definitions.

This method is automatically called when the StubOutForTesting()
object is deleted; there is no need to call it explicitly.

It is okay to call SmartUnsetAll() repeatedly, as later calls have
no effect if no SmartSet() calls have been made.

<h3 id="UnsetAll"><code>UnsetAll</code></h3>

``` python
UnsetAll()
```

Reverses Set() calls, restoring things to their original definitions.

This method is automatically called when the StubOutForTesting()
object is deleted; there is no need to call it explicitly.

It is okay to call UnsetAll() repeatedly, as later calls have no
effect if no Set() calls have been made.

<h3 id="__enter__"><code>__enter__</code></h3>

``` python
__enter__()
```




<h3 id="__exit__"><code>__exit__</code></h3>

``` python
__exit__(
    unused_exc_type,
    unused_exc_value,
    unused_tb
)
```






