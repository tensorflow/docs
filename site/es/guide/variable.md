# Variables

Una **variable** de TensorFlow es la mejor manera de representar un estado compartido y persistente
manipulado por su programa.

Variables son manipuladas via la clase `tf.Variable`. Una `tf.Variable`
representa un el valor de un tensor que puede ser cambiado corriendo operaciones
en el. Operaciones especificas te permiten leer y modificar los valores del
tensor. Librerias de alto nivel como `tf.keras` usan `tf.Variable` para guardar
parametros de modelo. Esta guia cubre como crear, actualizar y administrar
`tf.Variable`s en TensorFlow.

## Creando una Variable

Para crear una variable, simplemente provee el valor inicial

``` python
my_variable = tf.Variable(tf.zeros([1., 2., 3.]))
```

Esto crea una variable la cual es un tensor 3D con forma `[1, 2,
3]` llenado con ceros. Esta variable, por default, tendra el `dtype`
`tf.float32`. El dtype es, si no se especifica, inferido del valor
inicial.

Si existe un `tf.device` scope activo, la variable sera colocada en ese
dispositivo; de otra manera la variable sera colocada en el dispositivo "mas rapido"
con su dtype (esto significa que la mayoria de las variables son colocadas automaticamente
en una GPU si esta disponible). Por ejemplo, el siguiente codigo crea una variable
llamada `v` y la coloca en el segundo GPU:

``` python
with tf.device("/device:GPU:1"):
  v = tf.Variable(tf.zeros([10, 10]))
```

Idealmente se deberia usar la API `tf.distribute`, ya que eso permite que
se escriba el codigo una sola vez y funcione en diferentes configuraciones.

## Usar variables

Para usar el valor de una `tf.Variable` en una grafica TensorFlow, simplemente se
trata como un `tf.Tensor` normal:

``` python
v = tf.Variable(0.0)
w = v + 1  # w es un tf.Tensor que se computa basado en el valor de v.
           # Cualuier momento en que una variable es usada en una expresion
           # Es convertida automaticamente en un tf.Tensor representando su
           # valor
```

Para asignar un valor a una variable, se usan los metodos `assign`, `assign_add`, y
friends en la clase `tf.Variable`. Por ejemplo, asi es como se pueden llamar estos
metodos:

``` python
v = tf.Variable(0.0)
v.assign_add(1)
```

La mayoria de los optimizadores de TensorFlow tienen operaciones especializadas que
eficientemente actualizan los valores de las variables de acuerdo con algunos
algoritmos de descenso de gradiente. Revisa `tf.keras.optimizers.Optimizer` para
una explicación de como usar optimizadores.

Tambien se puede leer explicitamente el valor actual de una variable, usando
`read_value`:

```python
v = tf.Variable(0.0)
v.assign_add(1)
v.read_value()  # 1.0
```

Cuando la ultima referencia a una `tf.Variable` se sale del scope la memoria utilizada
es liberada.

### Seguimiento de variables

Una variable en TensorFlow es un objeto de Python. Conforme creas capas, modelos,
optimizadores, y otras herramientas relacionadas, probablemente sea necesario
obtener una lista de todas las variables en un (digamos) modelo.

Un caso de uso comun es [implementando `Layer` subclases](
https://www.tensorflow.org/guide/keras/custom_layers_and_models#the_layer_class).
La clase `Layer` rastrea recursivamente las variables establecidas como atributos de instancia:

```python
class MyLayer(tf.keras.layers.Layer):

  def __init__(self):
    super(MyLayer, self).__init__()
    self.my_var = tf.Variable(1.0)
    self.my_var_list = [tf.Variable(x) for x in range(10)]

class MyOtherLayer(tf.keras.layers.Layer):

  def __init__(self):
    super(MyOtherLayer, self).__init__()
    self.sublayer = MyLayer()
    self.my_other_var = tf.Variable(10.0)

m = MyOtherLayer()
print(len(m.variables))  # 12 (11 de MyLayer, mas my_other_var)
```

Si no se esta desarrollando una nueva `Layer`, TensorFlow tambien posee una
case generica base `tf.Module` que _solo_ implementa rastreo de variables.
Instancias de `tf.Module` tienen las propiedades `variables` y
`trainable_variables` que regresan todas las (trainable) variables de ese modelo
potencialmente navegando a traves de otros modelos (similar al rastreo hecho por
la clase`Layer`).
