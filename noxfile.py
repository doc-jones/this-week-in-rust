from pathlib import Path

import nox

ROOT = Path(__file__).parent
TOOLS = ROOT / "tools"


nox.options.sessions = []


def session(default=True, **kwargs):
    def _session(fn):
        if default:
            nox.options.sessions.append(kwargs.get("name", fn.__name__))
        return nox.session(**kwargs)(fn)

    return _session


@session()
def correctness(session):
    session.install("-r", TOOLS / "requirements.txt")
    session.run("python", TOOLS / "inspect_links.py", "--num-warn", "5")
    session.run("python", TOOLS / "inspect_markdown.py", "--num-recent", "5")
