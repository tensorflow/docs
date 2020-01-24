# Checkpoints (Pontos de Verificação)

Este documento apresenta como salvar e restaurar modelos TensorFlow construídos com
estimadores. TensorFlow disponibiliza dois formatos de modelos:

*   checkpoints, que é um formato dependente do código que criou o modelo.
*   SavedModel, que é um formato independente do código que criou o modelo.

O foco desse documento são os checkpoints. Para detalhes sobre o `SavedModel`, consulte o guia
[Salvando e Restaurando](../guide/saved_model.md).


## Código Exemplo

Este documento se baseia no
[exemplo de classificação de flores Iris](https://github.com/tensorflow/models/blob/master/samples/core/get_started/premade_estimator.py) detalhado em [Iniciando com TensorFlow](../guide/premade_estimators.md).
Para baixar e acessar esse exemplo, execute os dois comandos abaixo:

```shell
git clone https://github.com/tensorflow/models/
cd models/samples/core/get_started
```

A maioria dos trechos de código neste documento são pequenas variações de `premade_estimator.py`.

## Salvando modelos parcialmente treinados

Estimadores automaticamente gravam o seguinte no disco:

*   **checkpoints**, que são versões do modelo criado durante o treinamento.
*   **event files**, que contém informações usadas para criar visualizações no 
    [TensorBoard](https://developers.google.com/machine-learning/glossary/#TensorBoard)

Para especificar o diretório de nível superior no qual o Estimator armazena seus
informações, atribua um valor ao argumento opcional `model_dir` de *qualquer*
`Estimador`.
Tomando o `DNNClassifier` como exemplo, o código a seguir define o argumento `model_dir`
no diretório `models/iris`:

```python
classifier = tf.estimator.DNNClassifier(
    feature_columns=my_feature_columns,
    hidden_units=[10, 10],
    n_classes=3,
    model_dir='models/iris')
```
Suponha que você chame o método `train` do estimador. Por exemplo:

```python
classifier.train(
        input_fn=lambda:train_input_fn(train_x, train_y, batch_size=100),
                steps=200)
```

Conforme sugerido pelos diagramas a seguir, a primeira chamada para `treinamento`
adiciona checkpoints e outros arquivos ao diretório `model_dir`

<div style="width:80%; margin:auto; margin-bottom:10px; margin-top:20px;">
<img style="width:100%" src="https://www.tensorflow.org/images/first_train_calls.png">
</div>
<div style="text-align: center">
A primeira chamada de train().
</div>

Para ver os objetos criados no diretório `model_dir` em um sitema baseado em 
UNIX, basta executar o comando `ls` como demonstrado abaixo:

<pre>
$ ls -1 models/iris
checkpoint
events.out.tfevents.timestamp.hostname
graph.pbtxt
model.ckpt-1.data-00000-of-00001
model.ckpt-1.index
model.ckpt-1.meta
model.ckpt-200.data-00000-of-00001
model.ckpt-200.index
model.ckpt-200.meta
</pre>

O comando `ls`  acima mostra que o estimador criou checkpoints (pontos de verificação)
nos passos 1 (o início do treinamento) e 200 (o fim do treinamento).


### Diretório padrão de checkpoint

Se você não especificar `model_dir` na construção de um estimador, o Estimador
escreverá arquivos checkpoint em um diretório temporário escolhido pela função
[tempfile.mkdtemp] (https://docs.python.org/3/library/tempfile.html#tempfile.mkdtemp) do Python.
Por exemplo, a construção do Estimador a seguir  *não* especifica o argumento `model_dir`:

```python
classifier = tf.estimator.DNNClassifier(
    feature_columns=my_feature_columns,
    hidden_units=[10, 10],
    n_classes=3)

print(classifier.model_dir)
```

A função `tempfile.mkdtemp` escolhe um diretório temporário seguro
apropriado para o seu sistema operacional. Por exemplo, um diretório temporário típico
no macOS pode ser algo como o seguinte:

<pre>
/var/folders/0s/5q9kfzfj3gx2knj0vj8p68yc00dhcr/T/tmpYm1Rwa
</pre>

### Frequência dos checkpoints

Por padrão, o Estimador salva os
[checkpoints](https://developers.google.com/machine-learning/glossary/#checkpoint)
no `model_dir` de acordo com a programação a seguir:

*   Escreve checkpoint a cada 10 minutos (600 seconds).
*   Escreve um checkpoint quando o método `train` é iniciado (primeira iteração)
    e concluído (iteração final).
*   Mantém somente os 5 mais recentes checkpoints no diretório.

Você pode alterar essa programação padrão seguindo os seguintes passos:

1.  Crie um objeto `tf.estimator.RunConfig` que define a programação desejada.
2.  Ao instanciar o Estimador, passe esse objeto `RunConfig` para o argumento `config` do estimador.

Por exemplo, o código seguinte muda a programação de checkpoints para cada 20 minutos e mantém os 10 mais recentes:

```python
my_checkpointing_config = tf.estimator.RunConfig(
    save_checkpoints_secs = 20*60,  # Salva checkpoints a cada 20 minutos.
    keep_checkpoint_max = 10,       # Mantém os 10 checkpoints mais recentes.
)

classifier = tf.estimator.DNNClassifier(
    feature_columns=my_feature_columns,
    hidden_units=[10, 10],
    n_classes=3,
    model_dir='models/iris',
    config=my_checkpointing_config)
```

## Restaurando seu modelo

Na primeira vez em que você chama o método `train` do Estimador, o TensorFlow salva um
checkpoint para o `model_dir`. Cada chamada subseqüente para os métodos `train`,` assessment` ou `predict` causa o seguinte:


1.  O Estimador constrói os modelos
    [graph](https://developers.google.com/machine-learning/glossary/#graph)
    executando o `model_fn()`.  (Para maiores detalhes sobre o `model_fn()`, acesse
    [Criando Estimadores Customizados.](../guide/custom_estimators.md))
2.  O estimador inicializa os pesos do novo modelo a partir dos dados
     armazenado no checkpoint mais recente.

Em outras palavras, como a ilustração a seguir sugere, uma vez que os checkpoints
existam, o TensorFlow reconstrói o modelo toda vez que você chama `train()`,
`evaluate()`, ou `predict()`.

<div style="width:80%; margin:auto; margin-bottom:10px; margin-top:20px;">
<img style="width:100%" src="https://www.tensorflow.org/images/subsequent_calls.png">
</div>
<div style="text-align: center">
Chamadas posteriores de train(), evaluate(), ou predict()
</div>


### Evitando uma restauração ruim

Restaurar o estado de um modelo a partir de um checkpoint só funciona se o modelo
e checkpoint são compatíveis. Por exemplo, suponha que você treinou um
Estimador `DNNClassifier` que contém duas camadas ocultas,
cada um com 10 nós:

```python
classifier = tf.estimator.DNNClassifier(
    feature_columns=feature_columns,
    hidden_units=[10, 10],
    n_classes=3,
    model_dir='models/iris')

classifier.train(
    input_fn=lambda:train_input_fn(train_x, train_y, batch_size=100),
        steps=200)
```

Após o treinamento (e, portanto, após a criação de checkpoints em `models / iris`),
imagine que você alterou o número de neurônios em cada camada oculta de 10 para
20 e, em seguida, tentou treinar novamente o modelo:

``` python
classifier2 = tf.estimator.DNNClassifier(
    feature_columns=my_feature_columns,
    hidden_units=[20, 20],  # Muda o número de neurônios no modelo.
    n_classes=3,
    model_dir='models/iris')

classifier.train(
    input_fn=lambda:train_input_fn(train_x, train_y, batch_size=100),
        steps=200)
```

Como o estado no checkpoint é incompatível com o modelo descrito
no `classifier2`, o retreinamento falha com o seguinte erro:

<pre>
...
InvalidArgumentError (see above for traceback): tensor_name =
dnn/hiddenlayer_1/bias/t_0/Adagrad; shape in shape_and_slice spec [10]
does not match the shape stored in checkpoint: [20]
</pre>

Para executar experimentos nos quais você treina e compara ligeiramente diferentes
versões de um modelo, salve uma cópia do código que criou cada
`model_dir`, possivelmente criando um ramo git separado para cada versão.
Essa separação manterá seus checkpoints recuperáveis.

## Resumo

Os checkpoints fornecem um mecanismo automático fácil para salvar e restaurar
modelos criados por Estimadores.

Veja o guia [Savando and Restaurando](../guide/saved_model.md) para detalhes sobre:

*   Salvando e restaurando modelos usando APIs TensorFlow.
*   Exportando e importando modelos no formato SavedModel, que é um
     formato de serialização, neutro em linguagem, recuperável.