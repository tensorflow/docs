# Guida allo stile del codice TensorFlow

## Stile Python

Segue la guida [PEP 8 Python style
](https://www.python.org/dev/peps/pep-0008/) ad eccezione, per TensorFlow, di usare 2
spazi invece di 4. Cortesemente, allineatevi alla
[Guida Google di Stile per Python](https://github.com/google/styleguide/blob/gh-pages/pyguide.md),
ed usate [pylint](https://www.pylint.org/) per controllare le vostre modifiche Python.


### pylint

Per installare `pylint` e recuperare le definizioni personalizzate di stile di TensorFlow:

```bash

$ pip install pylint
$ wget -O /tmp/pylintrc https://raw.githubusercontent.com/tensorflow/tensorflow/master/tensorflow/tools/ci_build/pylintrc

```

Per controllare un file con `pylint`:

```bash
$ pylint --rcfile=/tmp/pylintrc myfile.py
```

### Versioni di Python supportate

TensorFlow supporta Python 2.7 e Python >= 3.4. Vedere la
[guida di installazione](https://www.tensorflow.org/install) per i dettagli.

Vedere lo 
[stato del build continuo](https://github.com/tensorflow/tensorflow/blob/master/README.md#continuous-build-status)
di TensorFlow per i build ufficiali e quelli supportati dalla comunità.

#### Compatibilità con Legacy Python

TensorFlow supporterà Legacy Python (Python 2.7) fino al 
[1 Gennaio, 2020](https://groups.google.com/a/tensorflow.org/forum/#!searchin/announce/python$202.7%7Csort:date/announce/gVwS5RC8mds/dCt1ka2XAAAJ).
Fino ad allora, sarà necessario che tutto il cosdice sia compatibile con le versioni di Python elencate sopra.

Queste linee dovranno essere presenti in ogni file Python:


```python
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
```

Usate `six` per scrivere codice compatibile (per esempio, `six.moves.range`).


## Style di codifica C++

Le modifiche al codice C++ di TensorFlow dovrebbero essere conformi alla 
[Guida Google di Stile C++](https://google.github.io/styleguide/cppguide.html). 
Usare `clang-tidy` per controllare le vostre modifiche al codice C/C++.

Per installare  `clang-tidy` su Ubuntu 16+:


```bash
$ apt-get install -y clang-tidy
```

Potete controllare un file C/C++ con il seguente:

```bash
$ clang-format <my_cc_file> --style=google > /tmp/my_cc_file.cc
$ diff <my_cc_file> /tmp/my_cc_file.cc
```

## Altri linguaggi

*   [Guida di Stile Google per Java](https://google.github.io/styleguide/javaguide.html)
*   [Guida di Stile Google per JavaScript](https://google.github.io/styleguide/jsguide.html)
*   [Guida di Stile Google per Shell](https://google.github.io/styleguide/shell.xml)
*   [Guida di Stile Google per Objective-C](https://google.github.io/styleguide/objcguide.html)




## Convenzioni ed usi speciali in TensorFlow

### Tensori

*   Le operazioni che trattano batch possono ipotizzare che la **prima dimensione** di
    un Tensore sia la dimensione del batch.
*   In molti modelli, l'**ultima dimensione** è il numero di _canali_.
*   Le dsimensioni escluse la prima e l'ultima, di solito, rappresentano le dimensioni dell _spazio_
    : la lunghezza della sequenza, o la dimensione dell'immagine.
    *   Quando possibile, usate un operatore sovraccarivcato tra Tensori, invece di una funzione di TensorFlow. 
    Per esempio, noi preferiamo `**`, `+`, `/`, `*`, `-`, `and/or` a
    `tf.pow`, `tf.add`, `tf.divide`, `tf.multiply`, `tf.subtract`, e `tf.logical_*` —
    a meno che sia richiesto un nome specifico per l'operazione.


### Operazioni Python

Un' _operazione Python_ è una funzione che, dati in input tensori e parametri,
crea una parte del grafo, e ritorna come risultato dei tensori.
*   Il primo argomento dovrebbe essere costituito di tensori, seguito dai parametri Python di base.
    L'ultimo argomento è `name` con valore di default `None`.
*   Gli argomenti Tensori dovrebbero essere un tensore singolo o un elenco "iterabile" di 
    tensori. Perché, "un Tensore o una lista di Tensori" è troppo generico. Vedere `assert_proper_iterable`.
*   Le operazioni che prendono tensori come argomenti ed usano operazioni C++, 
    dovranno chiamare `convert_to_tensor` per convertire input non-tensori in tensori.
    Notare che gli argomenti sono acora descritti nella documentazione come oggetti 
    di uno specifico tipo dtype: `Tensor`.
*   Ogni operazione Python dovrebbe avere un `name_scope`. 
    Come si può vedere sotto, per passare il nome dell'operaizone come una stringa.
*   Le operazioni dovrebbero contenere un commento estensibile Python con dichiarazioni
    Args e Returns che spieghino sia il tipo sia il significato di ogni valore. Eventuali
    shape, dtype, o rank dovrebbero essere specificati nella descrizione. Vedere i
    dettagli della documentazione.
*   Per una migliore usabilità, includere un esempio di utilizzo dell'operazione con input / output
    in una sezione Example.
*   Evitate di fare uso esplicito di `tf.Tensor.eval` o `tf.Session.run`. Per esempio,
    per scrivere della logica che dipnede dal valore del Tensore, usate il controllo di flusso di TensorFlow.
    In alternativa, restringete l'operazione a funzionare solo quando è abilitata l'esecuzione eager
    (`tf.executing_eagerly()`).

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
