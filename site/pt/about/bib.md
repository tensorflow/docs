# Documentação Técnica do TensorFlow

Este documento identifica documentos técnicos sobre o TensorFlow.

## Aprendizado de Máquina em Larga Escala em Sistemas Distribuídos Heterogêneos

[Acessar essa documentação.](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45166.pdf)

**Resumo:** TensorFlow é uma interface para expressar algoritmos de aprendizado de máquina
e uma implementação para executar tais algoritmos. Um cálculo expresso usando o TensorFlow pode ser
executado com pouca ou nenhuma alteração em uma ampla variedade de
sistemas, variando dispositivos móveis, como telefones
e tablets e até sistemas distribuídos em larga escala de centenas
de máquinas e milhares de dispositivos computacionais, como
Placas de GPU. O sistema é flexível e pode ser usado para expressar
uma ampla variedade de algoritmos, incluindo treinamento e inferência de algoritmos 
para modelos de redes neurais profundas, e tem sido
usado para conduzir pesquisas e implantar sistemas de aprendizado de máquina
em produção em mais de uma dúzia de áreas de ciência da computação e outros campos, incluindo reconhecimento de fala, visão computacional, robótica, recuperação de informação, linguagem natural,
processamento de idiomas, extração de informações geográficas e
descoberta computacional de drogas. Este artigo descreve a interface TensorFlow e uma implementação dessa interface que nós construímos na Google. A API do TensorFlow e uma implantação de referência foi lançada como um pacote de código aberto sob a licença Apache 2.0 em novembro de 2015 e estão disponíveis em www.tensorflow.org.

### In BibTeX format

Se você usa o TensorFlow em sua pesquisa e gostaria de citar o sistema TensorFlow, nós sugerimos
que você cite esse artigo técnico.

<pre>
@misc{tensorflow2015-whitepaper,
title={ {TensorFlow}: Large-Scale Machine Learning on Heterogeneous Systems},
url={https://www.tensorflow.org/},
note={Software available from tensorflow.org},
author={
    Mart\'{\i}n~Abadi and
    Ashish~Agarwal and
    Paul~Barham and
    Eugene~Brevdo and
    Zhifeng~Chen and
    Craig~Citro and
    Greg~S.~Corrado and
    Andy~Davis and
    Jeffrey~Dean and
    Matthieu~Devin and
    Sanjay~Ghemawat and
    Ian~Goodfellow and
    Andrew~Harp and
    Geoffrey~Irving and
    Michael~Isard and
    Yangqing Jia and
    Rafal~Jozefowicz and
    Lukasz~Kaiser and
    Manjunath~Kudlur and
    Josh~Levenberg and
    Dandelion~Man\'{e} and
    Rajat~Monga and
    Sherry~Moore and
    Derek~Murray and
    Chris~Olah and
    Mike~Schuster and
    Jonathon~Shlens and
    Benoit~Steiner and
    Ilya~Sutskever and
    Kunal~Talwar and
    Paul~Tucker and
    Vincent~Vanhoucke and
    Vijay~Vasudevan and
    Fernanda~Vi\'{e}gas and
    Oriol~Vinyals and
    Pete~Warden and
    Martin~Wattenberg and
    Martin~Wicke and
    Yuan~Yu and
    Xiaoqiang~Zheng},
  year={2015},
}
</pre>

Ou, de forma textual:

<pre>
Martín Abadi, Ashish Agarwal, Paul Barham, Eugene Brevdo,
Zhifeng Chen, Craig Citro, Greg S. Corrado, Andy Davis,
Jeffrey Dean, Matthieu Devin, Sanjay Ghemawat, Ian Goodfellow,
Andrew Harp, Geoffrey Irving, Michael Isard, Rafal Jozefowicz, Yangqing Jia,
Lukasz Kaiser, Manjunath Kudlur, Josh Levenberg, Dan Mané, Mike Schuster,
Rajat Monga, Sherry Moore, Derek Murray, Chris Olah, Jonathon Shlens,
Benoit Steiner, Ilya Sutskever, Kunal Talwar, Paul Tucker,
Vincent Vanhoucke, Vijay Vasudevan, Fernanda Viégas,
Oriol Vinyals, Pete Warden, Martin Wattenberg, Martin Wicke,
Yuan Yu, and Xiaoqiang Zheng.
TensorFlow: Large-scale machine learning on heterogeneous systems,
2015. Software available from tensorflow.org.
</pre>



## TensorFlow: A System for Large-Scale Machine Learning

[Acesse essa publicação.](https://www.usenix.org/system/files/conference/osdi16/osdi16-abadi.pdf)

**Resumo:** O TensorFlow é um sistema de aprendizado de máquina que opera em
em larga escala e em ambientes heterogêneos. TensorFlow
usa gráficos de fluxo de dados para representar a computação,
estado compartilhado e as operações que modificam esse estado. Isto
mapeia os nós de um gráfico de fluxo de dados em várias máquinas
em um cluster e dentro de uma máquina em vários computadores
dispositivos, incluindo CPUs multicore, de uso geral
GPUs e ASICs personalizados, conhecidos como
Unidades de processamento de tensores (TPUs). Essa arquitetura dá
flexibilidade para o desenvolvedor do aplicativo: enquanto no
“Servidor de parâmetros” projeta o gerenciamento de
estado está embutido no sistema, o TensorFlow permite que os desenvolvedores
experimentar novas otimizações e algoritmos de treinamento.
O TensorFlow suporta uma variedade de aplicações,
com foco no treinamento e inferência em redes neurais profundas.
Vários serviços do Google usam o TensorFlow na produção,
nós o lançamos como um projeto de código aberto e
tornou-se amplamente utilizado para pesquisa de aprendizado de máquina.
Neste artigo, descrevemos o modelo de fluxo de dados TensorFlow
e demonstramos o desempenho atraente que o TensorFlow
alcança para várias aplicações no mundo real.