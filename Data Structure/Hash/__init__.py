'''대표적인 데이터 구조6: 해쉬 테이블 (Hash Table)
1. 해쉬 구조
    Hash Table: 키(Key)에 데이터(Value)를 저장하는 데이터 구조
    Key를 통해 바로 데이터를 받아올 수 있으므로, 속도가 획기적으로 빨라짐
    파이썬 딕셔너리(Dictionary) 타입이 해쉬 테이블의 예: Key를 가지고 바로 데이터(Value)를 꺼냄
    보통 배열로 미리 Hash Table 사이즈만큼 생성 후에 사용 (공간과 탐색 시간을 맞바꾸는 기법)
    단, 파이썬에서는 해쉬를 별도 구현할 이유가 없음 - 딕셔너리 타입을 사용하면 됨
2. 알아둘 용어
    해쉬(Hash): 임의 값을 고정 길이로 변환하는 것
    해쉬 테이블(Hash Table): 키 값의 연산에 의해 직접 접근이 가능한 데이터 구조
    해싱 함수(Hashing Function): Key에 대해 산술 연산을 이용해 데이터 위치를 찾을 수 있는 함수
    해쉬 값(Hash Value) 또는 해쉬 주소(Hash Address): Key를 해싱 함수로 연산해서, 해쉬 값을 알아내고, 이를 기반으로 해쉬 테이블에서 해당 Key에 대한 데이터 위치를 일관성있게 찾을 수 있음
    슬롯(Slot): 한 개의 데이터를 저장할 수 있는 공간
    저장할 데이터에 대해 Key를 추출할 수 있는 별도 함수도 존재할 수 있음

4. 자료 구조 해쉬 테이블의 장단점과 주요 용도
    장점
        데이터 저장/읽기 속도가 빠르다. (검색 속도가 빠르다.)
        해쉬는 키에 대한 데이터가 있는지(중복) 확인이 쉬움
    단점
        일반적으로 저장공간이 좀더 많이 필요하다.
        여러 키에 해당하는 주소가 동일할 경우 충돌을 해결하기 위한 별도 자료구조가 필요함
    주요 용도
        검색이 많이 필요한 경우
        저장, 삭제, 읽기가 빈번한 경우
        캐쉬 구현시 (중복 확인이 쉽기 때문)'''