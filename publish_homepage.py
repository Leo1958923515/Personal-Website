#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把本目录的 README.md 同步到主页仓库，并推到 GitHub。

背景：本项目对应两个 GitHub 仓库，README.md 只有一份「真身」，就在本目录。

    github-profile/     ->  https://github.com/Leo1958923515/Personal-Website  （项目本体）
    ../profile-homepage/->  https://github.com/Leo1958923515/Leo1958923515     （主页仓库，只放 README.md）

所以改完 README.md 之后，跑一下本脚本，主页才会更新。

用法：
    python publish_homepage.py            # 同步 + 提交 + 推送
    python publish_homepage.py --dry-run  # 只看会改什么，不动 git
    python publish_homepage.py -m "文案"  # 自定义提交信息

依赖：本机已装 git，且 GitHub 凭据已缓存（首次 push 时弹窗登录过一次即可）。
"""

import argparse
import filecmp
import os
import shutil
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "README.md")
DST_REPO = os.path.abspath(os.path.join(HERE, "..", "profile-homepage"))
DST = os.path.join(DST_REPO, "README.md")

GIT_CANDIDATES = [
    r"D:\LEO\WORK\Git\Git\cmd\git.exe",
    "git",
]

# 这个网络环境里有一个本地代理（127.0.0.1:50315），它会间歇性 502。
# 所以推送写成「探路 -> 通了才推」的重试循环。
PROBE_ATTEMPTS = 12
PROBE_TIMEOUT = 45
PUSH_TIMEOUT = 180


def find_git():
    for c in GIT_CANDIDATES:
        if os.path.isabs(c):
            if os.path.exists(c):
                return c
        else:
            found = shutil.which(c)
            if found:
                return found
    sys.exit("找不到 git，请确认 Git for Windows 已安装。")


GIT = find_git()


def run(args, timeout=120):
    try:
        r = subprocess.run([GIT] + args, cwd=DST_REPO, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=timeout)
        return r.returncode, (r.stdout or "").strip(), (r.stderr or "").strip()
    except subprocess.TimeoutExpired:
        return -1, "", f"TIMEOUT after {timeout}s"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-m", "--message", default="docs: sync README from github-profile project")
    ap.add_argument("--dry-run", action="store_true", help="只比较文件，不做任何 git 操作")
    args = ap.parse_args()

    if not os.path.exists(SRC):
        sys.exit(f"源文件不存在：{SRC}")
    if not os.path.isdir(DST_REPO):
        sys.exit(f"主页仓库目录不存在：{DST_REPO}\n（先在 GitHub 建同名空仓库，再 clone 下来）")

    same = os.path.exists(DST) and filecmp.cmp(SRC, DST, shallow=False)
    print(f"源：{SRC}")
    print(f"目标：{DST}")
    print("内容：" + ("两边一致，无需同步" if same else "有差异，需要同步"))

    if args.dry_run:
        return
    if same:
        # 文件一致也检查一下有没有未推送的提交
        rc, out, _ = run(["status", "-sb"])
        print("git status:", out or "(空)")
        return

    shutil.copy2(SRC, DST)
    print("已复制 README.md")

    for step in (["add", "README.md"],
                 ["commit", "-m", args.message]):
        rc, out, err = run(step)
        print(f"$ git {' '.join(step)} -> rc={rc}")
        if out:
            print("   " + out.replace("\n", "\n   ")[:400])
        if rc != 0:
            print("   " + err[:400])
            if step[0] == "commit":
                sys.exit("提交失败，未推送。")

    print(f"\n开始推送（最多探路 {PROBE_ATTEMPTS} 次，代理抽风时会自动重试）...")
    for i in range(1, PROBE_ATTEMPTS + 1):
        rc, out, err = run(["ls-remote", "origin"], PROBE_TIMEOUT)
        print(f"  [试 {i:>2}] 探路 rc={rc} {err[:100]}")
        if rc == 0:
            rc2, out2, err2 = run(["push", "origin", "main"], PUSH_TIMEOUT)
            print(f"       push rc={rc2}")
            if out2:
                print("       " + out2.replace("\n", " | ")[:400])
            if err2:
                print("       " + err2[:400])
            if rc2 == 0:
                print("\n✅ 主页已更新：https://github.com/Leo1958923515")
                return
        time.sleep(4)

    sys.exit("❌ 推送失败：重试次数用尽。稍后再跑一次本脚本即可（提交已在本地）。")


if __name__ == "__main__":
    main()
