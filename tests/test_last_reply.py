"""last_reply.py 회귀 시험 — 합성 데이터만 쓴다.

    python3 -m unittest discover -s tests
"""
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".claude/skills/assis-inbox/scripts"))
import last_reply  # noqa: E402


def assistant(at, text=None, tool=False, subagent=False):
    content = [{"type": "tool_use", "name": "Bash", "input": {}}] if tool else [{"type": "text", "text": text}]
    inner = {"message": {"role": "assistant", "content": content}}
    if subagent:
        inner.update({"agent_id": "a1", "parent_tool_use_id": "t1"})
    return {"created_at": at, "assistant": {"uuid": at, "internal_anthropic_catchall": inner}}


def wrap(events):
    body = json.dumps({"ccr": {"data": events, "has_more": True}})
    return f'<other-session nonce="x" untrusted="true">\nDATA {{see}}:\n    {body}\n</other-session nonce="x">'


class LastReplyTest(unittest.TestCase):
    def test_skips_subagents_and_tool_only_turns(self):
        events = [
            assistant("2026-10-18T10:00", "첫 응답"),
            assistant("2026-10-18T10:01", tool=True),
            assistant("2026-10-18T10:02", "하위 에이전트 보고", subagent=True),
            assistant("2026-10-18T10:03", "본 스레드 마지막"),
        ]
        replies = last_reply.last_replies(last_reply.load_events(wrap(events)), 2)
        self.assertEqual([r["text"] for r in replies], ["첫 응답", "본 스레드 마지막"])

    def test_plain_assistant_message_shape(self):
        events = [{"created_at": "t", "assistant": {"message": {"content": [{"type": "text", "text": "plain"}]}}}]
        self.assertEqual(last_reply.last_replies(events, 1)[0]["text"], "plain")

    def test_result_event(self):
        events = [{"created_at": "t", "result": {"result": "끝났다"}}]
        self.assertEqual(last_reply.last_replies(events, 1)[0]["kind"], "result")

    def test_no_data(self):
        with self.assertRaises(ValueError):
            last_reply.load_events("no json")


if __name__ == "__main__":
    unittest.main()
