

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# Module: tf.contrib.lookup



Defined in [`tensorflow/contrib/lookup/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/lookup/__init__.py).

Ops for lookup operations.



## Classes

[`class HashTable`](../../tf/contrib/lookup/HashTable): A generic hash table implementation.

[`class HasherSpec`](../../tf/contrib/lookup/HasherSpec): A structure for the spec of the hashing function to use for hash buckets.

[`class IdTableWithHashBuckets`](../../tf/contrib/lookup/IdTableWithHashBuckets): String to Id table wrapper that assigns out-of-vocabulary keys to buckets.

[`class InitializableLookupTableBase`](../../tf/contrib/lookup/InitializableLookupTableBase): Initializable lookup table interface.

[`class KeyValueTensorInitializer`](../../tf/contrib/lookup/KeyValueTensorInitializer): Table initializers given `keys` and `values` tensors.

[`class LookupInterface`](../../tf/contrib/lookup/LookupInterface): Represent a lookup table that persists across different steps.

[`class MutableDenseHashTable`](../../tf/contrib/lookup/MutableDenseHashTable): A generic mutable hash table implementation using tensors as backing store.

[`class MutableHashTable`](../../tf/contrib/lookup/MutableHashTable): A generic mutable hash table implementation.

[`class StrongHashSpec`](../../tf/contrib/lookup/StrongHashSpec): A structure to specify a key of the strong keyed hash spec.

[`class TableInitializerBase`](../../tf/contrib/lookup/TableInitializerBase): Base class for lookup table initializers.

[`class TextFileIdTableInitializer`](../../tf/contrib/lookup/TextFileIdTableInitializer): Table initializer for string to `int64` IDs tables from a text file.

[`class TextFileIndex`](../../tf/contrib/lookup/TextFileIndex)

[`class TextFileInitializer`](../../tf/contrib/lookup/TextFileInitializer): Table initializers from a text file.

[`class TextFileStringTableInitializer`](../../tf/contrib/lookup/TextFileStringTableInitializer): Table initializer for `int64` IDs to string tables from a text file.

## Functions

[`index_table_from_file(...)`](../../tf/contrib/lookup/index_table_from_file): Returns a lookup table that converts a string tensor into int64 IDs.

[`index_table_from_tensor(...)`](../../tf/contrib/lookup/index_table_from_tensor): Returns a lookup table that converts a string tensor into int64 IDs.

[`index_to_string(...)`](../../tf/contrib/lookup/index_to_string): Maps `tensor` of indices into string values based on `mapping`. (deprecated)

[`index_to_string_table_from_file(...)`](../../tf/contrib/lookup/index_to_string_table_from_file): Returns a lookup table that maps a `Tensor` of indices into strings.

[`index_to_string_table_from_tensor(...)`](../../tf/contrib/lookup/index_to_string_table_from_tensor): Returns a lookup table that maps a `Tensor` of indices into strings.

[`string_to_index(...)`](../../tf/contrib/lookup/string_to_index): Maps `tensor` of strings into `int64` indices based on `mapping`. (deprecated)

[`string_to_index_table_from_file(...)`](../../tf/contrib/lookup/string_to_index_table_from_file): DEPRECATED FUNCTION

[`string_to_index_table_from_tensor(...)`](../../tf/contrib/lookup/string_to_index_table_from_tensor): DEPRECATED FUNCTION

## Other Members

`FastHashSpec`

