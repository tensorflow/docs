# White Paper su TensorFlow

Questo documento identifica i white paper su TensorFlow.

## Machine Learning su Larga Scala su Sistemi Distribuiti Eterogenei

[Accedi a questo white paper.](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45166.pdf)

**Sommario:** TensorFlow è un'interfaccia per esprimere algoritmi 
e programmi di machine learning ed un'implementazione per
eseguire questi algoritmi.
Una computazione descritta con TensorFlow può essere eseguita
senza o con minimi cambiamenti su una grande varietà di sistemi
eterogenei, dai dispositivi mobili come telefoni e tablet
fino a grandi sistemi distribuiti di centinaia di macchine
e migliaia di dispositivi di calcolo come le schede GPU.
Il sistema è flessibile e può essere usato per esprimere una 
grande varietà di algoritmi, inclusi algoritmi di addestramento
e inferenza per modelli di reti neurali, ed è stato usato per 
condurre ricerche e per realizzare systemi di machine learning
in produzione in più di una dozzina di aree dell'informatica
ed in altri campi, inclusi: riconoscimento del parlato,
visione artificiale, robotica, ricerca di informazioni, elaborazione
del linguaggio naturale, estrazione di informazioni geografiche, e
ricerca farmaceutica computazionale. Questo documento descrive
l'interfaccia di TensorFlow e l'implementazione dell'interfaccia
che abbiamo realizzato in Google. Le API di TensorFlow e l'
implementazione di riferimento sono state rilasciate come pacchetto 
open-source con licenza Apache 2.0 nel Novembre 2015, e sono 
disponibili su www.tensorflow.org.


### In formato BibTeX

Se usate TensorFlow nella vostra ricerca e volete citare il sistema TensorFlow, 
vi suggeriamo di citare questo White Paper.

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

O in forma testuale:

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



## TensorFlow: Un sistema per Machine Learning su Larga Scala

[Accedi a questo white paper.](https://www.usenix.org/system/files/conference/osdi16/osdi16-abadi.pdf)

**Sommario:** TensorFlow è un sistema di machine learning che
opera su larga scala ed in ambienti eterogenei. TensorFlow
usa grafi dataflow per rappresentare la computazione,
stati condivisi, e le operazioni che cambiano questi stati, 
mappando i nodi di un grafo dataflow tra molte macchine in cluster, 
e tra macchine appartenenti a diversi dispositivi di computazione
inclusi CPU multicore, GPUs generiche, e ASICs progettati in proprio
detti Tensor Processing Units (TPUs). Quest'architettura fornisce
flessibilità allo sviluppatore di applicazioni: mentre nei precedenti 
progetti basati su “server parametrici” la gestione degli stati condivisi
è realizzata all'interno del sistema, TensorFlow permette agli 
sviluppatori di sperimentare con nuove ottimizzazioni e algoritmi di addestramento.
TensorFlow supporta varie applicazioni, focalizzandosi in particolare 
sull'addestramento e sull'inferenza su reti neurali.
Diversi servizi Google usano TensorFlow in produzione,
lo abbiamo realizzato come un progetto open-source, ed è 
largamente usato per la ricerca nel machine learning.
In questo documento, descriviamo il modello di dataflow di
TensorFlow e dimostriamo le prestazioni raggiunte da TensorFlow, 
nel mondo reale, in diverse applicazioni.

