# Livres blancs TensorFlow

Ce document identifie les livres blancs sur TensorFlow.

## Apprentissage automatique à grande échelle sur des systèmes distribués hétérogènes

[Accéder à ce livre blanc.](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45166.pdf)

**Résumé:** TensorFlow est une interface pour décrire des algorithmes d'apprentissage machine. et une implémentation pour exécuter ces algorithmes.
Un calcul exprimé en utilisant TensorFlow peut être
exécuté avec peu ou pas de changement sur une grande variété de systèmes hétérogènes, allant des appareils mobiles tels que les téléphones et des tablettes jusqu'à des systèmes distribués à grande échelle de plusieurs centaines de machines et de milliers d'appareils de calcul tels que des cartes graphiques. Le système est flexible et peut être utilisé pour décrire une grande variété d'algorithmes, y compris l'entraînement et l'inférence de modèles de réseau d'apprentissage profond, et cela a été utilisés pour mener des recherches et pour déployer l'apprentissage automatique en production dans plus d'une douzaine de secteurs de l'industrie de l'informatique et d'autres domaines, y compris la reconnaissance vocale, la vision par ordinateur, la robotique, la recherche d'information, le traitement automatique du langage naturel, l'extraction d'information géographique, et la découverte computationnelle de médicaments. Ce livre blanc décrit l'interface TensorFlow et une version de cette interface que nous avons construite chez Google. L'API TensorFlow et une version de référence ont été publiées sous forme de paquet open-source sous licence Apache 2.0 en novembre 2015 et sont disponibles sur www.tensorflow.org.


### Au format BibTeX

Si vous utilisez TensorFlow dans vos recherches et souhaitez citer le système TensorFlow, nous vous suggérons de citer ce livre blanc.

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

Ou sous forme textuelle:

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



## TensorFlow: un système pour l'apprentissage automatique à grande échelle

[Accéder à ce livre blanc.](https://www.usenix.org/system/files/conference/osdi16/osdi16-abadi.pdf)

**Résumé:** TensorFlow est un système d'apprentissage automatique qui fonctionne à grande échelle et dans des environnements hétérogènes. TensorFlow utilise des graphes de flux de données pour représenter le calcul, l'état partagé et les opérations qui font muter cet état.
Il mappe les nœuds d'un graphe de flux de données sur de nombreuses machines d'un cluster, et au sein d'une machine sur plusieurs périphériques de calcul, y compris les processeurs multicœurs, les GPU polyvalents et les ASIC personnalisés appelés Tensor Processing Units (TPU).
Cette architecture donne de la flexibilité au développeur d'applications : alors que dans les précédentes conceptions “serveur de paramètres”, la gestion des états partagés est intégrée au système, TensorFlow permet aux développeurs d'expérimenter de nouvelles optimisations et algorithmes d'apprentissage.
TensorFlow supporte un grand nombre d'applications, avec un accent mis sur l'entraînement et l'inférence des réseaux d'apprentissage profond.
Plusieurs services Google utilisent TensorFlow en production, nous l'avons publié en tant que projet open-source, et il est devenu largement utilisé pour la recherche en apprentissage automatique.
Dans ce livre blanc, nous décrivons le modèle de flux de données de TensorFlow et démontrons les performances intéressantes que TensorFlow permet d'atteindre dans plusieurs applications du monde réel.
