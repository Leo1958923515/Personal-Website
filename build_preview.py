#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub Profile README 预览生成器

用法：
    python build_preview.py

作用：读取同目录的 README.md，生成自包含的 preview.html，
      用 GitHub 原生 Markdown 样式渲染，方便在本地直接预览效果，
      并提供一个开关高亮所有 "✏️" 占位内容。

修改 README.md 后重新运行本脚本即可刷新预览。
"""

import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / "README.md"
OUT = HERE / "preview.html"

TEMPLATE = r"""<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Leo · GitHub Profile README 预览</title>
<style>
  :root[data-theme="light"] {
    --bg: #ffffff; --fg: #1f2328; --muted: #59636e; --border: #d1d9e0;
    --link: #0969da; --code-bg: rgba(129,139,152,.12);
    --hdr-bg: #f6f8fa; --hdr-border: #d1d9e0;
  }
  :root[data-theme="dark"] {
    --bg: #0d1117; --fg: #e6edf3; --muted: #9198a1; --border: #3d444d;
    --link: #4493f8; --code-bg: rgba(110,118,129,.4);
    --hdr-bg: #151b23; --hdr-border: #3d444d;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0; background: var(--bg); color: var(--fg);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial,
                 "PingFang SC", "Microsoft YaHei", sans-serif;
    font-size: 16px; line-height: 1.5;
    -webkit-font-smoothing: antialiased;
    transition: background .2s, color .2s;
  }
  .toolbar {
    position: sticky; top: 0; z-index: 20;
    display: flex; align-items: center; gap: 10px; flex-wrap: wrap;
    padding: 10px 16px; background: var(--hdr-bg);
    border-bottom: 1px solid var(--hdr-border);
  }
  .toolbar .brand { font-weight: 600; font-size: 13px; color: var(--muted); margin-right: auto; }
  .toolbar .brand b { color: var(--fg); }
  .btn {
    font: inherit; font-size: 12px; line-height: 20px; cursor: pointer;
    padding: 4px 12px; border-radius: 6px; border: 1px solid var(--border);
    background: var(--bg); color: var(--fg); transition: border-color .15s, color .15s;
  }
  .btn:hover { border-color: var(--link); color: var(--link); }
  .btn[aria-pressed="true"] { border-color: var(--link); color: var(--link); font-weight: 600; }
  .wrap { max-width: 1012px; margin: 0 auto; padding: 32px 24px 96px; }
  #md > :first-child { margin-top: 0; }
  #md h3 {
    font-size: 1.25em; font-weight: 600; margin: 32px 0 16px;
    padding-bottom: .3em; border-bottom: 1px solid var(--border);
  }
  #md h4 { font-size: 1em; font-weight: 600; margin: 24px 0 16px; }
  #md p { margin: 0 0 16px; }
  #md a { color: var(--link); text-decoration: none; }
  #md a:hover { text-decoration: underline; }
  #md img { max-width: 100%; vertical-align: middle; }
  #md ul, #md ol { margin: 0 0 16px; padding-left: 2em; }
  #md li { margin: .25em 0; }
  #md li + li { margin-top: .25em; }
  #md blockquote {
    margin: 0 0 16px; padding: 0 1em; color: var(--muted);
    border-left: .25em solid var(--border);
  }
  #md code {
    font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
    font-size: 85%; padding: .2em .4em; border-radius: 6px; background: var(--code-bg);
  }
  #md pre { background: var(--code-bg); padding: 16px; border-radius: 6px; overflow: auto; }
  #md pre code { background: none; padding: 0; font-size: 100%; }
  #md hr { height: 1px; border: 0; background: var(--border); margin: 24px 0; }
  #md details { margin-bottom: 16px; }
  #md summary { cursor: pointer; font-weight: 600; }
  #md summary:hover { color: var(--link); }
  #md sub { font-size: 75%; color: var(--muted); }
  #md .ph {
    background: #fff8c5; color: #9a6700; border: 1px dashed #d4a72c;
    border-radius: 4px; padding: 0 4px; font-size: 85%; font-family: ui-monospace, Menlo, Consolas, monospace;
    word-break: break-all;
  }
  :root[data-theme="dark"] #md .ph { background: #3a2d12; color: #e3b341; border-color: #9e6a03; }
  #toast {
    position: fixed; left: 50%; bottom: 28px; transform: translate(-50%, 12px);
    background: #1f2328; color: #fff; font-size: 13px;
    padding: 8px 16px; border-radius: 8px; opacity: 0; pointer-events: none;
    transition: opacity .2s, transform .2s; z-index: 50;
  }
  #toast.on { opacity: 1; transform: translate(-50%, 0); }
</style>
</head>
<body>
<div class="toolbar">
  <span class="brand">预览 · <b>README.md</b>（GitHub Profile）</span>
  <button class="btn" id="togglePH" aria-pressed="true">高亮占位符：开</button>
  <button class="btn" id="toggleTheme">深色模式</button>
  <button class="btn" id="copyMd">复制 Markdown</button>
</div>
<div class="wrap"><div id="md">正在渲染…</div></div>
<div id="toast">已复制到剪贴板</div>

<script type="application/json" id="src">__MARKDOWN_JSON__</script>
<script src="https://cdn.jsdelivr.net/npm/marked@12.0.2/marked.min.js"></script>
<script>
(function () {
  var raw = JSON.parse(document.getElementById('src').textContent);
  var root = document.getElementById('md');
  var showPH = true;

  function escapeHtml(s) {
    return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }
  function withPlaceholders(md) {
    return md.replace(/<!--\s*✏️([\s\S]*?)-->/g, function (_, body) {
      return '<mark class="ph">✏️' + escapeHtml(body).replace(/\s*\n\s*/g, ' ') + '</mark>';
    });
  }
  function render() {
    var md = showPH ? withPlaceholders(raw) : raw;
    if (window.marked) {
      marked.setOptions({ gfm: true, breaks: false, headerIds: false, mangle: false });
      root.innerHTML = marked.parse(md);
    } else {
      root.innerHTML = '<p style="color:#9a6700">未能加载 Markdown 渲染库（需要联网）。' +
        '这不影响 README.md 本身，可直接把它上传到 GitHub 查看效果。</p>';
    }
  }

  document.getElementById('togglePH').addEventListener('click', function () {
    showPH = !showPH;
    this.setAttribute('aria-pressed', String(showPH));
    this.textContent = '高亮占位符：' + (showPH ? '开' : '关');
    render();
  });

  document.getElementById('toggleTheme').addEventListener('click', function () {
    var dark = document.documentElement.getAttribute('data-theme') === 'dark';
    document.documentElement.setAttribute('data-theme', dark ? 'light' : 'dark');
    this.textContent = dark ? '深色模式' : '浅色模式';
  });

  document.getElementById('copyMd').addEventListener('click', function () {
    var done = function () {
      var t = document.getElementById('toast');
      t.classList.add('on');
      setTimeout(function () { t.classList.remove('on'); }, 1400);
    };
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(raw).then(done, fallback);
    } else { fallback(); }
    function fallback() {
      var ta = document.createElement('textarea');
      ta.value = raw; ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta); ta.select();
      try { document.execCommand('copy'); done(); } catch (e) {}
      document.body.removeChild(ta);
    }
  });

  render();
})();
</script>
</body>
</html>
"""


def build() -> None:
    if not SRC.exists():
        raise SystemExit(f"找不到 {SRC}")
    md = SRC.read_text(encoding="utf-8")
    payload = json.dumps(md, ensure_ascii=False).replace("</", "<\\/")
    OUT.write_text(TEMPLATE.replace("__MARKDOWN_JSON__", payload), encoding="utf-8")
    print(f"已生成 {OUT}  （{len(md)} 字符 Markdown）")


if __name__ == "__main__":
    build()
