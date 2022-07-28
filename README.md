---
so-al-name: Insertion Sort
cdate: 2022-07-19
pl:
  - python
---

# Insertion Sort (삽입 정렬)

이 문서에서는 **삽입 정렬(Insertion Sort)** 의 개념과 구현 과정에 관한 내용을 정리합니다.

## I. About Insertion Sort

### I.0 개요

![Insertion_Sort_Visualize.gif](./images/Insertion_Sort_Visualize.gif)

> Insertion Sort (삽입 정렬)
> **삽입 정렬(揷入整列, insertion sort)** 은 자료 배열의 모든 요소들을 앞에서부터 차례대로 *이미 정렬된 배열 부분* 과 비교하여, 자신의 위치를 찾아 삽입함으로써 정렬을 완성하는 알고리즘이다.
> 
> *\- [삽입 정렬/위키백과](https://ko.wikipedia.org/wiki/삽입_정렬)*
> 
> ---
> 
> **Insertion sort** is a simple sorting algorithm that builds the final sorted array (or list) one item at a time.
> 
> *\- [Insertion Sort/Wikipedia](https://en.wikipedia.org/wiki/Insertion_sort)*

### I.1 삽입 정렬의 특징

- [Insertion Sort/Wikipedia](https://en.wikipedia.org/wiki/Insertion_sort) 에서 참조하였습니다.
- 흔히 사람들이 카드패를 손에 쥐고 정렬 할 때 사용하는 방식과 유사합니다.
- 정말 단순한 정렬 알고리즘 입니다.
- 정렬하고자 하는 데이터가 큰 경우에는 퀵 정렬, 힙 정렬, 합병 정렬에 비해 성능이 떨어집니다.
- 구현이 매우 간단합니다.^[컴퓨터 과학자 Jon Bentley는 해당 정렬을 C++를 사용해 3줄로 구현하였고, 최적화한 버전은 5줄에 불과했습니다.]
- 복잡도 $O(n^2)$을 갖는 다른 정렬 알고리즘처럼, 작은 데이터 세트에서는 성능이 좋습니다.
- 실전에서는 같은 복잡도 $O(n^2)$를 갖는 선택 정렬, 거품 정렬보다 성능이 좋습니다.

### I.2 알고리즘

### I.3 의사 코드

### I.4 복잡도

### I.5 다른 정렬 알고리즘과의 비교

### I.6 구현 코드


## D. 구현 일지

### 2022-07-19T22:24

- 삽입 정렬 뿐만 아니라 전체 리포지터리의 뼈대를 만들었습니다. 아직은 *Python* 환경만 구축했습니다.
- 숫자가 쓰여진 카드를 사용해 직접 정렬해 보면서 삽입 정렬의 내용을 이해했습니다.
- *이미 정렬이 된 부분* 과 *이미 정렬이 된 부분* 과 비교하여 삽입할 자리를 찾는 리스트의 원소를 비교하여, 구현하는 것이 목표였습니다.
- 작동하는 코드를 완성하긴 했으나, 해당 코드가 정렬을 제대로 수행하지는 않았습니다. 실제로 삽입을 진행하는 과정(`./insertion.py` 의 `_moveRight()` 함수와 그 이후의 상황)에 뭔가 문제가 있는 것으로 추정되지만, 오늘은 조금 피곤하여 여기서 커밋을 진행합니다.

### 2022-07-20T14:22

오늘 해야 할 일은 아래와 같습니다.

- [x] 삽입 정렬이 무엇인지 관해서 정리합니다. (이 문서의 `I.` 헤더 아래에 정리합니다.)
  - 우선은 `insertion.py`의 주석에 정리하였습니다.
- [x] 어제 추정한 문제의 부분인 `insertion.py`의 `_moveRight()` 알고리즘을 다시 찬찬히 살펴보고, 어떤 오류가 있는지 잡아냅니다.

`while`문을 샤옹하던 이전 버전과는 달리, `for`문을 새로 작성하였습니다. 훨씬 직관적인 방법으로 코딩을 할 수 있었습니다.

무엇이 문제인지 파악하기 위해 디버깅을 진행했고, `input_list`, `sorted_bound_index`, `unsorted_head_index`, 를 Watch List에 추가했습니다. 안쪽 `for`문이 문제였습니다.

```python
for compare_index in range(0, sorted_bound_index):
  ...
```

`compare_index` 가, 이미 정렬된 앞쪽의 리스트의 원소들과 삽입할 새로운 원소를 비교해야 하는데, `for`문의 범위가 저렇게 설정되어 버리면 정렬된 리스트의 마지막 원소와는 아예 비교를 진행하지 않습니다. 그리고 첫번째 단계에서는 아예 비교가 진행되지도 않았구요. 때문에 아래와 같이 수정해 주었습니다.

```python
for compare_index in range(0, unsorted_head_index):
  ...
```
사실 `unsorted_head_index` 대신에 `sorted_bound_index + 1`이 와도 되지만 의미적으로 `unsorted_head_index`가 더 맞을 것 같아서 저런 식으로 작성하였습니다.
  
추가적으로 `listGen.py`의 내용도 수정했습니다. `random.sample()` 함수는 중복 추출을 허용하지 않고 단순히 부분집합만 추출하였기 때문에 `random.choice()`를 이용한 함수를 새로 작성하였습니다. 아래 링크를 참조하였습니다.

- [5.3.1 랜덤(random) 모듈/왕초보를 위한 Python: 쉽게 풀어 쓴기초 문법과 실습](https://wikidocs.net/79)

다음에 할 일은 아래와 같습니다.

- [ ] 알고리즘의 상세 내용 정리하기.
- [ ] 오름차순, 내림차순을 설정할 수 있는 기능 추가하기.
- [ ] 성능 측정을 위해 `main.py` 수정하기.

# Reference

- [\[알고리즘\] 삽입 정렬(insertion sort)이란/heejeong Kwon/Hee's Development Blog](https://gmlwjd9405.github.io/2018/05/06/algorithm-insertion-sort.html)
- [Insertion Sort/Wikipedia](https://en.wikipedia.org/wiki/Insertion_sort)
- [삽입 정렬/위키백과](https://ko.wikipedia.org/wiki/삽입_정렬)