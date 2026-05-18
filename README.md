# Magic Square 작성 예제

## 작업 요약

MagicSquare 프로젝트에 ECB(Entity-Control-Boundary) 아키텍처와 TDD 흐름을
기준으로 Cursor rules를 구성했습니다.

### Cursor Rules

- `.cursor/rules/`: Python 기준 공통 rules
- `.cursor/python/`: Python 전용 rules
- `.cursor/cpp/`: C++ 전용 rules
- `.cursor/java/`: Java 전용 rules
- `.cursorrules`: 프로젝트 전체 요약 rules

각 언어별 rule set에는 다음 내용을 포함했습니다.

- 프로젝트 목적과 파일 구조
- ECB 아키텍처와 레이어 의존성 방향
- 언어별 코드 스타일
- TDD red/green/refactor 단계 규칙
- 테스트 프레임워크와 커버리지 기준
- 금지 패턴과 대체 방법
- Cursor AI의 코드 작성 전, 작성 중, 작성 후 행동 규칙

### Python 구현

Python 기준으로 `User` 엔티티와 pytest 테스트를 추가했습니다.

- `entity/user.py`: `User` 엔티티 클래스
- `entity/__init__.py`: `User` export
- `tests/entity/test_user.py`: AAA 패턴 기반 pytest 테스트

`User` 엔티티는 사용자 이름의 앞뒤 공백을 제거하고, 빈 이름을 거부하며,
지원 가능한 홀수 차수의 마방진을 생성할 수 있는지 판단합니다.

### 확인 사항

- linter 진단 결과 오류가 없습니다.
- 현재 Windows 환경에서 `python` 명령이 PATH에 잡히지 않아 pytest 실행은 보류된 상태입니다.
