# 텐서플로 2.0으로 코드 업그레이드

Note: 이 문서는 텐서플로 커뮤니티에서 번역했습니다. 커뮤니티 번역 활동의 특성상 정확한 번역과 최신 내용을 반영하기 위해 노력함에도
불구하고
[공식 영문 문서](https://github.com/tensorflow/docs/blob/master/site/en/guide/upgrade.md)의
내용과 일치하지 않을 수 있습니다. 이 번역에 개선할 부분이 있다면
[tensorflow/docs](https://github.com/tensorflow/docs) 깃헙 저장소로 풀 리퀘스트를 보내주시기
바랍니다. 문서 번역이나 리뷰에 참여하려면
[docs-ko@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ko)로
메일을 보내주시기 바랍니다.

텐서플로 2.0은 매개변수 재배치, 심볼(symbol) 이름 변경, 파라미터 기본값 변경과 같은 많은 API 변화가 있습니다. 이러한
수정사항들을 일일이 다 반영하는 건 지루하며 실수하기 쉽습니다. 변화들을 간략하게 그리고 TF 2.0에 매끄럽게 옮겨가기 위해 또한
기존 코드를 새로운 API로 수정하는 것을 쉽게 하기위해 텐서플로 팀은 `tf_upgrade_v2` 유틸리티를 개발하였습니다.

`tf_upgrade_v2` 유틸리티는 TF 2.0을 `pip install` 하면 자동적으로 설치됩니다. 유틸리티는 기존의 텐서플로 1.x
파이썬 스크립트를 텐서플로 2.0으로 변환하여 업그레이드를 빠르게 합니다.

변환 스크립트는 자동화되어 있지만 문법적이고 작성 스타일에 관한 변환은 스크립트에 의해 수행되지 않습니다.

## 호환성 모듈

어떤 API 심볼들은 단순히 이름을 변경하는 것만으로는 업그레이드가 안 될 수도 있습니다. 코드를 텐서플로 2.0에서 동작시키기 위해,
`compat.v1` 모듈을 포함하도록 스크립트를 업그레이드 하세요. 이 모듈은 `tf.foo`와 같은 TF 1.x 심볼을 동등한
`tf.compat.v1.foo`로 대체합니다. 호환성 모듈이 괜찮긴 하지만 직접 수정사항을 확인하고 가능한 빠르게 `tf.compat.v1.*`
네임스페이스(namespace) 대신 `tf.*` 네임스페이스에 있는 새로운 API로 마이그레이션 하기를 추천합니다.

텐서플로 2.x 모듈에서 사라지는 것들(예를 들면, `tf.flags`와 `tf.contrib`) 때문에, 어떤 변동사항은
`compat.v1`으로 바꾸는 것만으로는 동작하지 않을 수 있습니다. 이 코드를 업그레이드하려면 다른 라이브러리가 필요하거나(예를 들면,
`absl.flags`) [tensorflow/addons](http://www.github.com/tensorflow/addons)에 있는
패키지로 바꾸어야 할 수도 있습니다.

## 업그레이드 스크립트

작성한 코드를 텐서플로 1.x에서 텐서플로 2.x로 변경하려면, 다음의 지시에 따르세요:

### pip 패키지로부터 스크립트 실행

첫째로, `pip install`로 `tensorflow` 또는 `tensorflow-gpu` 패키지를 설치합니다.

Note: `tf_upgrade_v2`는 텐서플로 1.13 그리고 이후 버전에서 자동으로 설치되었습니다. (nightly TF 2.0 빌드를
포함)

업그레이드 스크립트는 하나의 파이썬 파일에 대해서 실행됩니다:

```sh
tf_upgrade_v2 --infile tensorfoo.py --outfile tensorfoo-upgraded.py
```

스크립트는 코드에서 대체할 부분을 찾지 못하면 에러 메시지를 표시합니다. 디렉토리 트리에 대해서도 실행가능 합니다:

```
# .py 파일을 업그레이드하고 다른 모든 파일들을 outtree에 복사
tf_upgrade_v2 --intree coolcode --outtree coolcode-upgraded

# .py 파일만 업그레이드
tf_upgrade_v2 --intree coolcode --outtree coolcode-upgraded --copyotherfiles False
```

## 자세한 리포트

스크립트는 자세한 변동사항들의 리스트를 보여줍니다, 예를들면:

```
'tensorflow/tools/compatibility/testdata/test_file_v1_12.py' Line 65
--------------------------------------------------------------------------------

Added keyword 'input' to reordered function 'tf.argmax'
Renamed keyword argument from 'dimension' to 'axis'

    Old:         tf.argmax([[1, 3, 2]], dimension=0))
                                        ~~~~~~~~~~
    New:         tf.argmax(input=[[1, 3, 2]], axis=0))

```

이 모든 정보는 `report.txt` 파일에 포함되어 있고 이 파일은 현재 디렉토리에 생성될 것입니다. `tf_upgrade_v2`가 실행되고
업그레이드 스크립트가 만들어지면 각자의 모델을 실행하여 출력이 TF 1.x과 비슷한지 확인할 수 있습니다.
## 주의사항

-   이 스크립트를 실행하기 전에 대상코드의 일부를 수동으로 업데이트하지 마세요. 특히, `tf.argmax` 또는
    `tf.batch_to_space`와 같이 매개변수의 순서가 변동된 함수는 스크립트가 부정확한 키워드 매개변수를 추가하여 기존코드를 잘못
    바꿀 수 있습니다.

-   스크립트는 `tensorflow`가 `import tensorflow as tf`로 임포트(import) 되어있다고 가정합니다.

-   이 스크립트는 매개변수의 순서를 바꾸지는 않습니다. 대신에 스크립트는 매개변수의 순서가 바뀐 함수들에 대해서 키워드 매개변수를
    추가합니다.

-   [tf2up.ml](http://tf2up.ml)을 방문해서 깃헙 저장소의 주피터 노트북과 파이썬 파일들을 업그레이드할 수 있는 편리한
    툴을 확인하세요.

업그레이드 스크립트의 버그를 제보하거나 기능 추가 요청을 하려면
[GitHub](https://github.com/tensorflow/tensorflow/issues). 그리고 텐서플로 2.0을 테스트하고
있다면, 의견을 듣고 싶습니다!
[TF 2.0 Testing community](https://groups.google.com/a/tensorflow.org/forum/#!forum/testing)에
가입해 주세요. 질문과 토론은 [testing@tensorflow.org](mailto:testing@tensorflow.org)로 메일 주시기
바랍니다.
