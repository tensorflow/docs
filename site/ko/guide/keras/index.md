# 케라스(Keras)

Note: 이 문서들은 텐서플로 커뮤니티에서 번역했습니다. 커뮤니티 번역 활동의 특성상 정확한 번역과 최신 내용을 반영하기 위해 노력함에도 불구하고
[공식 영문 문서](https://www.tensorflow.org/?hl=en)의 내용과 일치하지 않을 수 있습니다. 이 번역에 개선할 부분이
있다면 [tensorflow/docs](https://github.com/tensorflow/docs) 깃헙 저장소로 풀 리퀘스트를 보내주시기
바랍니다. 문서 번역이나 리뷰에 참여하려면
[docs-ko@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ko)로
메일을 보내주시기 바랍니다.

`tf.keras`는 텐서플로의 딥러닝 모델 설계와 훈련을 위한 고수준(high-level) API입니다. 이는 빠른 프로토타이핑, 최첨단 기술의 연구 및 생산에 사용되며, 세 가지 주요 이점이 있습니다:

-   *사용자 친화적*<br> 케라스는 일반 사용 사례에 최적화된 간단하고 일관적인 인터페이스를 제공합니다. 이는 사용자 오류에 대해 명확하고 실용적인 피드백을 제공합니다.
-   *모듈화 및 구성 가능성*<br> 케라스 모델은 구성 요소의 설정에 의해 연결되는 식으로 거의 제한없이 만들 수 있습니다.
-   *쉬운 확장*<br> 연구를 위한 새로운 아이디어를 표현하기 위해 사용자 정의 설계 블록을 작성하세요. 새로운 층(layers), 지표(metrics), 손실 함수를 생성하고 최첨단 모델을 개발하세요.

[케라스: 빠른 개요](./overview.ipynb) 가이드는 시작하는 데 도움이 될 것입니다.

`tf.keras'를 통한 머신 러닝에 입문하는 분들을 위한 안내는 [입문 튜토리얼 세트](https://www.tensorflow.org/tutorials/keras)를 보세요.

API에 대해 더 자세히 알아보고 싶다면, 텐서플로 케라스의 고급 사용자가 알아야 할 사항을 다루는 다음 가이드 세트를 참조하세요:

-   [케라스의 함수형 API 가이드](./functional.ipynb)
-   [훈련 및 평가 가이드](./train_and_evaluate.ipynb)
-   [서브 클래싱(subclassing)을 사용한 기초적인 층(layer)과 모델 작성 가이드](./custom_layers_and_models.ipynb)
-   [모델 저장 및 직렬화 가이드](./save_and_serialize.ipynb)
-   [사용자 정의 콜백 작성 가이드](./custom_callback.ipynb)
