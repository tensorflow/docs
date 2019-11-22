# Guida allo stile del codice TensorFlow

## Stile per Python

Seguire la [Guida di stile Python PEP 8](https://www.python.org/dev/peps/pep-0008/), 
ad eccezione, per TensorFlow, di usare 2 spazi
invece di 4. Cortesemente, conformarsi alla
[Google Python Style Guide](https://github.com/google/styleguide/blob/gh-pages/pyguide.md),
ed usare [pylint](https://www.pylint.org/) per verificare le modifiche Python.


### pylint

Per installare `pylint` e recuperare le definizioni di stile personalizzate di TensorFlow usare:

```bash

$ pip install pylint
$ wget -O /tmp/pylintrc https://raw.githubusercontent.com/tensorflow/tensorflow/master/tensorflow/tools/ci_build/pylintrc

```

Per verificare un file con `pylint`usare:

```bash
$ pylint --rcfile=/tmp/pylintrc myfile.py
```

### Versioni di Python supportate

TensorFlow supporta Python 2.7 e Python >= 3.4. Vedere la
[guida all'installazione](https://www.tensorflow.org/install) per i dettagli.

Vedere in 
[stato dei build continui](https://github.com/tensorflow/tensorflow/blob/master/README.md#continuous-build-status) 
di TensorFlow per i build ufficiali e della comunità.

#### Compatibilità con Legacy Python

TensorFlow supporterà Legacy Python (Python 2.7) fino al 
[1 Gennaio, 2020](https://groups.google.com/a/tensorflow.org/forum/#!searchin/announce/python$202.7%7Csort:date/announce/gVwS5RC8mds/dCt1ka2XAAAJ).
Fino a quella data, tutto il codice avrà bisogno di essere compatibile con le versioni di Python
elencate sopra.

Le seguenti linee dovranno essere presenti in ogni file Python:


```python
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
```

Usare `six` per scrivere codice compatibile (per esempio, `six.moves.range`).


## Stile di codifica C++

Le modifiche al codice C++ di TensorFlow dovranno essere conformi alla [Google C++ Style
Guide](https://google.github.io/styleguide/cppguide.html). Usare `clang-tidy` per 
controllare le vostre modifiche C/C++.

Per installare  `clang-tidy` su Ubuntu 16+:


```bash
$ apt-get install -y clang-tidy
```

Potete controllare un file C/C++ usando:

```bash
$ clang-format <my_cc_file> --style=google > /tmp/my_cc_file.cc
$ diff <my_cc_file> /tmp/my_cc_file.cc
```

## Altri linguaggi

*   [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html)
*   [Google JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html)
*   [Google Shell Style Guide](https://google.github.io/styleguide/shell.xml)
*   [Google Objective-C Style Guide](https://google.github.io/styleguide/objcguide.html)




## Convenzioni e usi particolari in TensorFlow

### Tensori

*   Le operazioni che trattano batch possono assumere che la **prima dimensione** di
    un Tensore sia la dimensione del batch.
*   Nella maggioranza del modelli, l' **ultima dimensione** è il numero dei  _canali_.
*   Dimensioni ad eccezione della prima e dell'ultima, di solito, rappresentano le dimensioni dello _spazio_:
    la lunghezza della sequenza, o la dimensione dell'immagine.
*   Quando è possibile, usare un operatore sovraccaricato del Tensore, invece di una funzione 
    TensorFlow. Per esempio, noi preferiamo `**`, `+`, `/`, `*`, `-`, `and/or` a
    `tf.pow`, `tf.add`, `tf.divide`, `tf.multiply`, `tf.subtract`, e `tf.logical_*` —
    a meno che si desideri un nome specifico per l'operazione.


### Operazioni Python

Un' _Operazione Python_ è una funzione che, dati in input tensori e parametri, 
crea una parte del grafo e restituisce tensori in output.

*   I primi argomenti devono essere i tensori, seguiti dal paramentri base Python.
    L'ultimo argomento è `name` con il valore di default `None`.
*   Gli argomenti Tensori devono essere o un singolo tensore o un 'iterabile' di tensori. 
    Perchè "Tensore o lista di Tensori" è troppo generico. Vedere `assert_proper_iterable`.
*   Le operazioni che prendono tensori come argomenti, se stanno usando operazioni C++
    devono chiamare `convert_to_tensor` per convertire input non-tensori in tensori.
    Notare che nella documentazione gli argoemnti sono ancora descritti come un oggetto `Tensor` di uno
    specifico dtype.
*   Ogni operazione Python deve avere un `name_scope`. Come si può vedere sotto, passare il nome
    dell'operazione come una stringa.
*   Le operazioni devono contenere un commento Python estensibile con le dichiarazioni di 
    Args e Returns, che spieghino il tipo e la semantica di ciascun valore. Eventuali
    shapes, dtypes, or ranks devono essere specificati nella descrizione. Vedere
    la documentazione per i dettagli.
*   Per migliorare l'usabilità, includere un esempio di utilizzo con intput / output
    dell'operazione in una sezione Example.
*   Evitare di fare esplicito uso di  `tf.Tensor.eval` o `tf.Session.run`. Per
    esempio, per scrivere la logica che dipende dal valore del Tensore, usare il 
    controllo di flusso di TensorFlow. In alternativa, restringere l'operazione in modo che funzioni 
    solo quando è abilitata la Eager Execution (`tf.executing_eagerly()`).

Esempio:


```python
def my_op(tensor_in, other_tensor_in, my_param, other_param=0.5,
          output_collections=(), name=None):
  """My operation that adds two tensors with given coefficients.

  Args:
    tensor_in: `Tensor`, input tensor.
    other_tensor_in: `Tensor`, same shape as `tensor_in`, other input tensor.
    my_param: `float`, coefficient for `tensor_in`.
    other_param: `float`, coefficient for `other_tensor_in`.
    output_collections: `tuple` of `string`s, name of the collection to
                        collect result of this op.
    name: `string`, name of the operation.

  Returns:
    `Tensor` of same shape as `tensor_in`, sum of input values with coefficients.

  Example:
    >>> my_op([1., 2.], [3., 4.], my_param=0.5, other_param=0.6,
              output_collections=['MY_OPS'], name='add_t1t2')
    [2.3, 3.4]
  """
  with tf.name_scope(name or "my_op"):
    tensor_in = tf.convert_to_tensor(tensor_in)
    other_tensor_in = tf.convert_to_tensor(other_tensor_in)
    result = my_param * tensor_in + other_param * other_tensor_in
    tf.add_to_collection(output_collections, result)
    return result
```

Utilizzo:

```python
output = my_op(t1, t2, my_param=0.5, other_param=0.6,
               output_collections=['MY_OPS'], name='add_t1t2')
```
