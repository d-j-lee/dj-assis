# dj-assis

사람과 실작업 AI 사이에 **다리를 놓는 AI 비서**. 실작업 AI의 세션 품질을 최선으로 관리한다.
안드로이드 폰의 Claude 앱에서 말로 쓴다.

AI는 이미 충분히 유능하다. 이제 세션 품질을 깎는 건 사람 쪽 — 얇은 프롬프트, 노이즈, 이해가 덜 된
피드백이다. dj-assis는 그 사이에 서서:

1. 무슨 일을 원하는지 **말로** 받고
2. 사전 검토와 짧은 **인터뷰**로 **최선의 최종 프롬프트**를 짜서 작업을 이끌고
3. **주요 시점마다** 브리핑하며 다음 방향을 가이드하고
4. 사람에게는 **음성 한 줄 + 한눈에 보이는 자료**로 결정을 돕고
5. 워커에게는 **전체 방향과 지금 시점에 맞는** 지시를 보낸다

자세한 구상은 [`docs/concept.md`](docs/concept.md).

## 지금 되는 것 — 1조각: 세션 브리핑 (3·4·5)

밀린 Claude Code 세션들을 훑어 **사람이 내려야 할 결정만** 카드로 올리고, 답을 정리해 각 세션에 전달한다.

1. 폰 Claude 앱 → **Code** 탭 → 새 세션, 이 리포 선택
2. 받아쓰기로 **"브리핑"**
3. 결론 3줄과 결정 카드를 보고, 칩을 누르거나 말로 답한다
4. 해석을 한 줄씩 확인하면 각 세션으로 전달된다(권한 승인·병합 같은 건 링크만 준다)

필요한 것: Claude Code 클라우드 세션을 쓸 수 있는 플랜, GitHub 연동.
상태: 구현됨, 실사용 시험 0/3 ([`trials/`](trials/TEMPLATE.md)). 음성 출력(2조각)·정방향(3조각)은 계획 단계.

## 지도

| 파일 | 무엇 |
|---|---|
| [`docs/concept.md`](docs/concept.md) | 무엇·왜 — 계기, 구상 5요소, 설계 원칙, 위험 |
| [`docs/architecture.md`](docs/architecture.md) | 어떻게 — 역할·채널·표면 선택·조각 계획·스파이크 |
| [`docs/decisions.md`](docs/decisions.md) | 결정 기록 |
| [`.claude/skills/assis-inbox/`](.claude/skills/assis-inbox/SKILL.md) | 1조각 절차와 분류 스크립트 |
| [`trials/`](trials/TEMPLATE.md) | 실사용 시험 기록(익명) |
| [`docs/research/`](docs/research/) | 조사 근거 (날짜별, 갱신하지 않음) |
| [`docs/dev/handoff.md`](docs/dev/handoff.md) | 개발 인계 — 다음 세션의 출발점 |
| [`CLAUDE.md`](CLAUDE.md) | 이 리포에서 열린 Claude 세션의 규율 |

## 개발

```bash
python3 -m unittest discover -s tests
```
