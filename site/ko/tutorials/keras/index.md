# 머신러닝을 배우고 사용하기

Note: 아래는 저희 텐서플로우 커뮤니티에서 번역한 문서들입니다. 커뮤니티 번역활동의 특성상 정확한 번역과 항상 최신의 내용을 반영하기 위한 노력에도
불구하고 [공식 영문 문서](https://www.tensorflow.org/?hl=en)의 내용과 일치하지 않는 부분이 있을 수 있습니다.
만약 번역에 대한 개선점에 대한 제안이 있으신 분은
[tensorflow/docs](https://github.com/tensorflow/docs) 깃헙 저장소로 풀 리퀘스트를 보내주시기 바랍니다.
문서를 작성하거나 커뮤니티 번역에 대한 리뷰를 남기시길 원하시는 분은 [본 양식](https://bit.ly/tf-translate)을
작성하시거나
[docs@tensorflow.org list](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs)로
메일을 보내주시기 바랍니다.


이 노트북 파일들은 *[Deep Learning with Python](https://books.google.com/books?id=Yo3CAQAACAAJ)* 책을 바탕으로 작성되었습니다. 이 튜토리얼은 딥러닝 모델을 만들고 훈련하기 위해 텐서플로의 고수준 파이썬 API인 `tf.keras`를 사용합니다. 텐서플로와 케라스(Keras)에 대해 더 알고 싶다면 [텐서플로 케라스 가이드](../../guide/keras)를 참고하세요.

출판사 노트: *Deep Learning with Python*은 딥러닝을 설명하기 위해 파이썬과 케라스 라이브러리를 사용합니다. 이 책은 케라스 창시자이고 구글 AI 연구원인 프랑소와 숄레(François Chollet)가 썼습니다. 이 책에서 직관적인 설명과 실용적인 예제를 통해 딥러닝을 배울 수 있습니다. (이 책의 한글 번역서는 *[케라스 창시자에게 배우는 딥러닝](https://books.google.co.kr/books?id=EJV5DwAAQBAJ)* 입니다)

머신러닝의 기본 원리와 개념을 배우려면 [머신러닝 단기집중과정](https://developers.google.com/machine-learning/crash-course/)을 수강해 보세요. [추가 자료](../next_steps) 페이지에 텐서플로와 머신러닝에 대한 더 많은 정보가 정리되어 있습니다.

1. [기초적인 분류 문제](./basic_classification.ipynb)
2. [텍스트 분류](./basic_text_classification.ipynb)
3. [회귀](./basic_regression.ipynb)
4. [과대적합과 과소적합](./overfit_and_underfit.ipynb)
5. [모델의 저장과 복원](./save_and_restore_models.ipynb)
