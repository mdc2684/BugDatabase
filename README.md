# BugDatabase

A lightweight, self-hosted bug tracker built with Flask. BugDatabase gives small
teams a simple board to report, store and share bugs found during development —
no heavyweight JIRA setup, just a single `app.py` and Jinja templates.

Originally built as a 4-day toy project (team 23, 2023-03-27 ~ 2023-03-30), it is
now maintained as a minimal open-source tracker for hobby projects and classroom
use.

## Features

- User registration & login (session-based auth)
- Create / read / update / delete bug reports on a shared board
- Minimal dependencies: Flask + SQLite-friendly design
- Clean template structure under `templates/`

## Quick Start

```bash
pip install flask
python app.py
# open http://localhost:5000
```

## Project Layout

```
app.py            # Flask application (routes + models)
templates/        # Jinja2 templates (login, register, board, post views)
.gitignore        # standard Python/IDE ignores
```

## Roadmap

- [ ] Search & filter bugs by tag/status
- [ ] Comment threads on each bug report
- [ ] Pagination on the board list
- [ ] REST API endpoints for automation

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Bug reports and PRs welcome — please use
the issue templates.

## License

[MIT](LICENSE)

---

# BugDatabase (한국어)

개발 중 발견한 버그를 작성해 저장하고 공유하는 게시판 커뮤니티 서비스입니다.
Flask + Jinja 템플릿으로 구성된 가벼운 자체 호스팅 버그 트래커입니다.

## 주요 기능

- 회원가입 / 로그인 (세션 기반 인증)
- 버그 리포트 작성·열람·수정·삭제
- 최소 의존성, 단일 `app.py` 구조

## 실행 방법

```bash
pip install flask
python app.py
```

MIT 라이선스로 배포됩니다.
