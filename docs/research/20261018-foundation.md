# 기반 조사 — 2026-10-18

> 히스토리성 근거 문서다. 정본은 `docs/concept.md`·`docs/architecture.md`이고, 이 문서는 그 근거를 보관한다.
> 갱신하지 않는다. 사실이 바뀌면 새 날짜의 조사 문서를 만들고 정본을 고친다.
>
> 출처 구분: `[실측]` 이 세션 도구 결과(실사용 계정 1개 표본, 익명) · `[문서]` 이 세션의 조사가 읽은
> 1차 자료(URL) · `[미확인]`.

## 1. 이 세션에서 잰 것

| 항목 | 값 | 비고 |
|---|---|---|
| 세션 도구 | `create_session`·`send_message`·`list_events`·`get_session`·`list_sessions`·`archive_session`·`send_later`·`PushNotification`이 클라우드 Code 세션에 존재 | 공식 문서에는 이 이름들이 없다 |
| 세션 계보 | `get_session`의 lineage depth 0 / limit 8 | 세션이 세션을 만들 수 있는 깊이 |
| 다른 세션이 만든 세션 | 표본 23개 중 7개가 `claude_code_mcp_seed` 출신 | 세션 간 생성이 실제로 쓰이고 있다 |
| 사람 대기 | 표본 22개 중 12개(신선 4 · 14일 초과 8) | `post_turn_summary.status_category` 기준 |
| 숨은 대기 | 완료 버킷인데 마지막 요약이 `need_input`: 3개 | 버킷만 보면 놓친다 |
| 요약 필드 | `post_turn_summary`가 22개 중 19개에 존재: `status_category`·`needs_action`·`status_detail`·`recent_action` | `unread`·`usage.cost_usd`·`context_usage`도 있음 |
| 목록 크기 | `list_sessions` 30건 = 52,827자(도구 한도 초과로 파일 저장) → `triage.py` 4,684자(−91%), 0.04초 | |
| 리포 스킬 로드 | 리포에 `.claude/skills/assis-inbox`를 두자 같은 세션의 스킬 목록에 바로 나타남 | 데스크 세션도 같은 방식으로 받는다 `[추정]` |
| 아티팩트 런타임 능력 | artifact·assets·comments·db·downloads·files·mcp·room·sample·user. **마이크 없음** | 런타임 0.2.85 |
| 아티팩트 `sample` 과금 | 보는 사람의 구독 사용량 | 타입 정의 |

## 2. 플랫폼 사실 (요지)

| 사실 | 상태 | 출처 |
|---|---|---|
| 양방향 음성 모드: 전 플랜, 안드로이드 포함, 한국어 지원(비영어 베타), 언어 자동감지 없음 | `[문서]` | support.claude.com/en/articles/11101966 (09-16) |
| 음성 모드 모델은 Opus/Sonnet/Haiku 빠른 판, Fable 불가, 사용량 차감 | `[문서]` | 같은 곳 |
| 통합 Claude(채팅+Cowork 통합)에서는 작업 중 대화를 포함해 어느 대화에서나 음성. Code·구 Cowork는 받아쓰기만 | `[문서]` | 같은 곳 |
| 음성에서 커넥터 사용(권한 확인 후). 프로젝트 지침·지식 적용은 명시 없음 | `[문서]`/`[미확인]` | 같은 곳 |
| 받아쓰기: 전 플랜, 한국어 베타, 음성 파일은 전사 후 삭제 | `[문서]` | articles/10065434 (07-23) |
| 안드로이드 Code 탭: 클라우드 세션 시작·감시·조종·질문 답변, Remote Control | `[문서]` | code.claude.com/docs/en/mobile |
| 클라우드 Code 세션 종료 시 알림 | `[문서]` (조사 간 상충: 다른 조사는 미확인) | articles/12618689 (10-16) |
| Remote Control 연결 시 "작업 끝/조치 필요" 푸시 토글 | `[문서]` | code.claude.com/docs/en/remote-control |
| 딥링크 `claude://code/new?q=…` | `[문서]` 긴 본문 보존 `[미확인]` | articles/14898120 (05-06) |
| Dispatch: 신규 사용자 불가 | `[문서]` | articles/13947068 (10-15) |
| 클라우드 Cowork 작업은 노트북을 닫아도 계속, 폰에서 시작·확인·답변 | `[문서]` | articles/16761823 (09-16) |
| 스킬: 웹에서 ZIP 업로드, 모바일·통합 경험에서 사용 | `[문서]` | articles/12512180, 15520349 |
| 아티팩트의 커넥터·저장: 웹/데스크톱으로 명시, 안드로이드 `[미확인]` | `[문서]` | articles/17153992 (10-08) |
| Claude Code Projects(베타): 한 대화가 클라우드 스레드를 띄움, Pro/Max, 하루 200개 | `[문서]` | code.claude.com/docs/en/claude-projects |
| `claude --cloud` / `claude -p --cloud <id>` CLI로 생성·메시지 | `[문서]` | code.claude.com/docs/en/claude-code-on-the-web |
| 클라우드 VM은 몇 분 유휴 후 정지·회수 가능. 백그라운드 작업 복원 안 됨 | `[문서]` | code.claude.com/docs/en/cloud-environments |
| Agent SDK·Managed Agents는 API 키·API 과금, 제3자 제품의 claude.ai 로그인 제공 불허 | `[문서]` | agent-sdk/overview, platform.claude.com/docs/en/managed-agents |
| 세션 간 메시지는 권한 승인을 못 한다 | `[문서]` | code.claude.com/docs/en/cross-session-messaging |

## 3. 선행 연구·근거 (F1–F12)

| # | 발견 | 출처 |
|---|---|---|
| F1 | 한 번에 주면 풀던 과제를 여러 턴에 나눠 주면 LLM 15종 평균 −39%, 초기 가정에 고착 | arxiv.org/abs/2505.06120 · Anthropic Sonnet 5 프롬프트 가이드 |
| F2 | 다듬지 않은 음성 프롬프트는 타이핑보다 첫 시도 성공률이 낮고, 다듬은 전사는 동등. 전사 오류는 코드 같은 구성형 과제에 특히 해롭다 | arxiv.org/abs/2607.05808 · 2608.03970 |
| F3 | 계획 단위 검토는 작동(계획 39% 거절), 행동 단위는 실패(권한 프롬프트 97% 승인, 심어 둔 위험 명령 거절 13.6%, 세션 후반 5%) | claude.com/blog/auto-mode-default-in-claude-code (08-07) |
| F4 | 공식 패턴: AskUserQuestion으로 인터뷰 → SPEC.md → 새 세션 실행. 두 번 고쳐도 안 되면 `/clear` 후 더 나은 프롬프트 | code.claude.com/docs/en/best-practices |
| F5 | 겨냥된 질문은 최대 +74%, 질 낮은 질문은 해롭다. 모델은 모호한 과제를 잘 구분하지 못한다 | arxiv.org/abs/2502.13069 · Zou et al. 2023 |
| F6 | 다중 에이전트 실패의 44%가 명세·설계, 32%가 에이전트 간 정렬. 프롬프트 개선은 +9~16%뿐. "행동에는 암묵적 결정이 실린다" | arxiv.org/abs/2503.13657 · cognition.ai 2025-06, 2026-04 |
| F7 | 유능한 모델에 과잉 지시는 품질 저하. "요청만이 아니라 이유를" | Anthropic Fable 5 프롬프트 가이드 · effective-context-engineering |
| F8 | 사람을 멈춰 세울 때: 파괴적·비가역, 실제 범위 변경, 그 사람만 줄 수 있는 입력. 요약은 결과 먼저 + 필요한 것 한두 개. 상태 주장을 도구 결과로 감사하게 하면 날조 보고가 거의 사라짐. SBAR은 전화 인계에 근거 | Anthropic Fable 5 가이드 · BMJ Open 2018 |
| F9 | 혼합 주도: 기대효용으로 행동/질문/대기 선택, 불확실하면 덜 하되 맞게. 굵은 작업 경계에서 끼어들면 재개 비용↓ | Horvitz CHI'99 · Iqbal & Bailey CHI'06 · Mark CHI'08 |
| F10 | 자동화가 높을수록 평상시 성능↑, 고장 대응·상황 인식↓. 설명은 정답 여부와 무관하게 수용을 높인다 | Onnasch 2014 · Parasuraman & Manzey 2010 · Bansal CHI'21 |
| F11 | 음성은 핵심, 화면은 상세(중복 금지). 한 호흡 규칙. 듣기 183 wpm vs 읽기 238 wpm, 말하기 입력은 타이핑의 약 3배 | Google 대화 설계 · Alexa · Brysbaert 2019 · Ruan 2016 |
| F12 | 명세 주도 도구의 불만은 의식(ceremony)과 검토 부담(작은 버그에 수용 기준 16개). "한 문장으로 설명되는 diff면 계획을 건너뛰라" | martinfowler.com 2025-10 · Claude Code 문서 |

## 4. 한국어 음성 유의점 (근거 얇음)

- 침묵 타이머가 아니라 의미 기반 발화 종료 감지 — 한국어는 동사·부정이 끝에 온다.
- 한영 혼용 발화의 인식 오류가 크다(HiKE, arxiv 2509.24613) → 리포·고유명사는 화면에서 확인.
- 읽어 줄 문장의 숫자는 고유어/한자어 수사 전환이 필요하다 → 음성 줄에는 숫자를 피한다.
- 존댓말은 한 가지로 일관(시스템→사용자는 합쇼체가 무난).

## 5. 확인하지 않은 것

- 조사가 읽은 URL을 하나하나 다시 열어 대조하지 않았다. 2026년 arXiv 수치는 프리프린트다.
- 클라우드 Code 세션 종료 알림은 조사 둘이 엇갈린다(하나는 문서 확인, 하나는 미확인).
- 통합 Claude 음성 대화에서 세션 도구 접근(S1), 딥링크 본문 보존(S2), 음성 모드의 프로젝트 지침 적용(S3)은 기기 실측 전이다.
- 안드로이드 Code 탭에서 `AskUserQuestion` 칩 렌더링·받아쓰기 품질(S4)은 미측정.
- 표본은 계정 1개다. 대기 비율은 일반화된 수치가 아니라 문제의 존재를 보이는 사례다.
