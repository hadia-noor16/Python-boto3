#!/usr/bin/env python3
# fake_logs.py — generate Apache-style fake logs (CLF or ELF)
# No external dependencies. Works on Windows/Linux/Mac.

import argparse
import datetime as dt
import gzip
import os
import random
import sys
import time

RESP_CODES = ["200", "301", "404", "500"]
RESP_WEIGHTS = [0.90, 0.04, 0.04, 0.02]

VERBS = ["GET", "POST", "DELETE", "PUT"]
VERB_WEIGHTS = [0.65, 0.20, 0.10, 0.05]

RESOURCES = [
    "/",
    "/index.html",
    "/about.html",
    "/search?q=cloud",
    "/docs/api",
    "/wp-content",
    "/wp-admin",
    "/explore",
    "/app/main/posts",
    "/posts/posts/explore",
    "/apps/cart.jsp?appID=",
    "/img/logo.png",
    "/css/site.css",
    "/js/app.js",
]

REFERERS = [
    "-",
    "https://www.google.com/",
    "https://www.bing.com/",
    "https://twitter.com/",
    "https://news.ycombinator.com/",
    "https://example.com/",
]

USER_AGENTS = [
    # a few realistic UA strings
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6_1) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
]

def rand_ip() -> str:
    return ".".join(str(random.randint(1, 254)) for _ in range(4))

def now_parts() -> tuple[str, str]:
    """
    Return (timestamp_str, tz_offset_str) like ('20/Oct/2025:23:59:59', '-0600')
    Uses local timezone offset; no external libs required.
    """
    local = dt.datetime.now().astimezone()
    ts = local.strftime("%d/%b/%Y:%H:%M:%S")
    tz = local.strftime("%z")
    return ts, tz

def pick_verb() -> str:
    return random.choices(VERBS, weights=VERB_WEIGHTS, k=1)[0]

def pick_resource() -> str:
    res = random.choice(RESOURCES)
    if "apps" in res:
        res += str(random.randint(1000, 10000))
    return res

def pick_referer() -> str:
    return random.choice(REFERERS)

def pick_user_agent() -> str:
    return random.choice(USER_AGENTS)

def pick_resp() -> str:
    return random.choices(RESP_CODES, weights=RESP_WEIGHTS, k=1)[0]

def pick_bytes() -> int:
    # Around 5KB average
    return max(0, int(random.gauss(5000, 500)))

def make_line(log_format: str) -> str:
    ip = rand_ip()
    ts, tz = now_parts()
    verb = pick_verb()
    uri = pick_resource()
    resp = pick_resp()
    byt = pick_bytes()
    ref = pick_referer()
    ua = pick_user_agent()

    if log_format == "CLF":
        # Common Log Format
        # 127.0.0.1 - - [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326
        return f'{ip} - - [{ts} {tz}] "{verb} {uri} HTTP/1.0" {resp} {byt}\n'
    else:
        # Extended/Combined Log Format (adds referer and user-agent)
        # 127.0.0.1 - - [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326 "http://www.example.com/start.html" "Mozilla/4.08 [en] (Win98; I ;Nav)"
        return f'{ip} - - [{ts} {tz}] "{verb} {uri} HTTP/1.0" {resp} {byt} "{ref}" "{ua}"\n'

def open_output(output: str | None, prefix: str | None) -> tuple[object, str | None]:
    timestr = time.strftime("%Y%m%d-%H%M%S")
    base = (f"{prefix}_" if prefix else "") + f"access_log_{timestr}.log"

    if output == "LOG":
        f = open(base, "w", encoding="utf-8")
        return f, base
    elif output == "GZ":
        f = gzip.open(base + ".gz", "wt", encoding="utf-8")
        return f, base + ".gz"
    else:
        return sys.stdout, None

def main():
    p = argparse.ArgumentParser("fake_logs.py", description="Generate fake Apache logs")
    p.add_argument("-o", "--output", choices=["LOG", "GZ", "CONSOLE"], default="CONSOLE",
                   help="Write to a file (LOG), gzip (GZ), or STDOUT (CONSOLE)")
    p.add_argument("-l", "--log-format", choices=["CLF", "ELF"], default="ELF",
                   help="CLF = Common Log Format, ELF = Combined/Extended")
    p.add_argument("-n", "--num", type=int, default=10,
                   help="Number of lines to generate (0 = infinite)")
    p.add_argument("-p", "--prefix", type=str, default=None,
                   help="Prefix for output filename (when using LOG/GZ)")
    p.add_argument("-s", "--sleep", type=float, default=0.0,
                   help="Sleep seconds between lines (can be fractional)")
    args = p.parse_args()

    f, path = open_output(args.output, args.prefix)
    count = 0

    try:
        while True:
            line = make_line(args.log_format)
            f.write(line)
            # Flush frequently so you can tail the file live
            if args.output != "CONSOLE":
                f.flush()

            count += 1
            if args.num > 0 and count >= args.num:
                break

            # Either fixed sleep, or a random 30–300s if 0 (feel free to change)
            if args.sleep > 0:
                time.sleep(args.sleep)
            else:
                # comment the next two lines if you don't want random spacing
                dt_rand = random.randint(0, 0)  # 0 = no wait by default
                if dt_rand:
                    time.sleep(dt_rand)
    except KeyboardInterrupt:
        pass
    finally:
        if f is not sys.stdout:
            f.close()
        if path:
            print(f"Wrote {count} lines → {path}")

if __name__ == "__main__":
    main()
