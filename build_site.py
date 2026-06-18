#!/usr/bin/env python3
"""
Compila todos os autoestudos do módulo num único `index.html` self-contained.

Como rodar:
    python3 build_site.py

Saída: cria/sobrescreve `index.html` na raiz do repo.
Basta abrir o arquivo no navegador (double-click) — não precisa de servidor.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).parent

MATERIAS = [
    ("lideranca", "Liderança", "🧭"),
    ("computacao", "Computação", "💻"),
    ("matematica", "Matemática", "📐"),
    ("negocios", "Negócios", "📈"),
    ("ux", "UX", "🎨"),
]


def parse_date_ddmmyyyy(s: str):
    """Recebe '20/05/2026' e retorna tupla ordenável (ano, mes, dia)."""
    try:
        d, m, y = s.split("/")
        return (int(y), int(m), int(d))
    except Exception:
        return (9999, 99, 99)


def parse_metadata(content: str) -> dict:
    """Extrai título e data do markdown."""
    meta = {}
    if not content:
        return meta
    lines = content.split("\n")

    # Título: primeira linha "# ..."
    for line in lines[:5]:
        if line.startswith("# "):
            title = line[2:].strip()
            for suffix in (" — Explicação", " — Material original"):
                if title.endswith(suffix):
                    title = title[: -len(suffix)]
            meta["title"] = title.strip()
            break

    # Data: procurar dd/mm/aaaa nas primeiras 25 linhas
    for line in lines[:25]:
        m = re.search(r"(\d{2}/\d{2}/\d{4})", line)
        if m:
            meta["date"] = m.group(1)
            break

    return meta


def collect():
    autoestudos = []
    for slug, label, emoji in MATERIAS:
        d = ROOT / slug
        if not d.exists():
            continue
        for sub in sorted(d.iterdir()):
            if not sub.is_dir() or not sub.name.startswith("autoestudo-"):
                continue
            material_path = sub / "01-material.md"
            explicacao_path = sub / "02-explicacao.md"
            material = (
                material_path.read_text(encoding="utf-8")
                if material_path.exists()
                else ""
            )
            explicacao = (
                explicacao_path.read_text(encoding="utf-8")
                if explicacao_path.exists()
                else ""
            )

            meta = parse_metadata(explicacao) or {}
            mat_meta = parse_metadata(material) or {}
            if "title" not in meta and "title" in mat_meta:
                meta["title"] = mat_meta["title"]
            if "date" not in meta and "date" in mat_meta:
                meta["date"] = mat_meta["date"]

            parts = sub.name.split("-")
            numero = parts[1] if len(parts) > 1 else "?"

            # ID estável para hash routing
            id_ = f"{slug}-{sub.name}"

            autoestudos.append(
                {
                    "id": id_,
                    "materia_slug": slug,
                    "materia_label": label,
                    "materia_emoji": emoji,
                    "slug": sub.name,
                    "numero": numero,
                    "title": meta.get("title", sub.name),
                    "date": meta.get("date", ""),
                    "material": material,
                    "explicacao": explicacao,
                }
            )
    return autoestudos


def build_html(autoestudos):
    # Ordena por matéria (na ordem definida) e depois por número
    materia_order = {slug: i for i, (slug, _, _) in enumerate(MATERIAS)}
    autoestudos.sort(
        key=lambda a: (
            materia_order.get(a["materia_slug"], 99),
            int(a["numero"]) if a["numero"].isdigit() else 99,
        )
    )

    # Estatísticas pro header
    total = len(autoestudos)
    last_date = ""
    if autoestudos:
        with_date = [a for a in autoestudos if a["date"]]
        if with_date:
            last = max(with_date, key=lambda a: parse_date_ddmmyyyy(a["date"]))
            last_date = last["date"]

    payload = {
        "autoestudos": autoestudos,
        "materias": [
            {"slug": s, "label": l, "emoji": e} for s, l, e in MATERIAS
        ],
        "stats": {"total": total, "last_date": last_date},
    }
    # Defesa contra `</script>` no conteúdo
    data_json = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")

    html = TEMPLATE.replace("__DATA__", data_json)
    (ROOT / "index.html").write_text(html, encoding="utf-8")
    print(f"✓ index.html gerado com {total} autoestudos.")
    if last_date:
        print(f"  Última data: {last_date}")


TEMPLATE = r"""<!DOCTYPE html>
<html lang="pt-BR" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Módulo 10 — Teste A/B | Autoestudos</title>
<script src="https://cdn.jsdelivr.net/npm/marked@12/marked.min.js"></script>
<script src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/highlight.min.js"></script>
<link id="hljs-theme" rel="stylesheet" href="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/styles/github.min.css">
<style>
:root {
  --bg: #ffffff;
  --bg-elevated: #f7f8fa;
  --bg-sidebar: #fafbfc;
  --border: #e4e7eb;
  --border-strong: #cdd2d8;
  --text: #1a1f2e;
  --text-muted: #5b6573;
  --text-faint: #8b95a5;
  --accent: #4f46e5;
  --accent-hover: #4338ca;
  --accent-bg: #eef2ff;
  --code-bg: #f5f6f8;
  --table-stripe: #f9fafb;
  --shadow: 0 1px 3px rgba(0,0,0,0.04), 0 1px 2px rgba(0,0,0,0.06);
  --shadow-lg: 0 10px 25px rgba(0,0,0,0.08), 0 4px 10px rgba(0,0,0,0.04);
  --radius: 8px;
  --sidebar-width: 320px;
  --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", "Inter", Roboto, sans-serif;
  --font-mono: "JetBrains Mono", "SF Mono", Menlo, Consolas, monospace;
}
[data-theme="dark"] {
  --bg: #0f1419;
  --bg-elevated: #181d24;
  --bg-sidebar: #131820;
  --border: #252b34;
  --border-strong: #353c48;
  --text: #e6e9ef;
  --text-muted: #a0a7b3;
  --text-faint: #6a7280;
  --accent: #818cf8;
  --accent-hover: #a5b4fc;
  --accent-bg: #1e1f3a;
  --code-bg: #1c2128;
  --table-stripe: #161b22;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body {
  height: 100%;
  font-family: var(--font-sans);
  background: var(--bg);
  color: var(--text);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  font-size: 15px;
}
body {
  display: flex;
  overflow: hidden;
}

/* ── Sidebar ─────────────────────────────────────────── */
.sidebar {
  width: var(--sidebar-width);
  flex-shrink: 0;
  background: var(--bg-sidebar);
  border-right: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  height: 100vh;
  overflow: hidden;
  transition: transform 0.2s ease;
}
.sidebar-header {
  padding: 20px 20px 12px;
  border-bottom: 1px solid var(--border);
}
.sidebar-header h1 {
  font-size: 16px;
  font-weight: 700;
  letter-spacing: -0.01em;
  color: var(--text);
}
.sidebar-header p {
  font-size: 12px;
  color: var(--text-muted);
  margin-top: 2px;
}
.sidebar-stats {
  font-size: 11px;
  color: var(--text-faint);
  margin-top: 6px;
  display: flex;
  gap: 10px;
}
.sidebar-stats span { display: inline-flex; align-items: center; gap: 4px; }

.search-wrapper {
  padding: 12px 14px;
  border-bottom: 1px solid var(--border);
}
#search {
  width: 100%;
  padding: 8px 12px;
  border: 1px solid var(--border-strong);
  border-radius: var(--radius);
  background: var(--bg);
  color: var(--text);
  font-size: 13px;
  font-family: inherit;
  outline: none;
  transition: border-color 0.15s;
}
#search:focus {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px var(--accent-bg);
}

.nav {
  flex: 1;
  overflow-y: auto;
  padding: 8px 0;
}
.nav-group {
  margin-bottom: 4px;
}
.nav-group-header {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  font-size: 11px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--text-muted);
  cursor: pointer;
  user-select: none;
}
.nav-group-header:hover { color: var(--text); }
.nav-group-header .chev {
  margin-left: auto;
  transition: transform 0.15s;
  font-size: 10px;
  opacity: 0.6;
}
.nav-group.collapsed .chev { transform: rotate(-90deg); }
.nav-group.collapsed .nav-items { display: none; }
.nav-group-count {
  font-size: 10px;
  color: var(--text-faint);
  background: var(--bg-elevated);
  padding: 1px 6px;
  border-radius: 10px;
  font-weight: 500;
}

.nav-item {
  display: block;
  padding: 8px 16px 8px 36px;
  font-size: 13px;
  color: var(--text);
  text-decoration: none;
  border-left: 2px solid transparent;
  cursor: pointer;
  transition: background 0.1s;
  line-height: 1.4;
}
.nav-item:hover {
  background: var(--bg-elevated);
}
.nav-item.active {
  background: var(--accent-bg);
  color: var(--accent);
  border-left-color: var(--accent);
  font-weight: 500;
}
.nav-item-num {
  font-size: 11px;
  color: var(--text-faint);
  font-variant-numeric: tabular-nums;
}
.nav-item.active .nav-item-num { color: var(--accent); }
.nav-item-title {
  display: block;
  margin-top: 1px;
}
.nav-item-date {
  font-size: 10px;
  color: var(--text-faint);
  margin-top: 2px;
}
.nav-empty {
  padding: 12px 36px;
  font-size: 12px;
  font-style: italic;
  color: var(--text-faint);
}

.sidebar-footer {
  padding: 10px 14px;
  border-top: 1px solid var(--border);
  display: flex;
  gap: 8px;
  align-items: center;
  font-size: 12px;
}
.icon-btn {
  background: transparent;
  border: 1px solid var(--border-strong);
  color: var(--text-muted);
  padding: 6px 10px;
  border-radius: 6px;
  font-size: 12px;
  cursor: pointer;
  font-family: inherit;
  transition: all 0.15s;
  display: inline-flex;
  align-items: center;
  gap: 5px;
}
.icon-btn:hover {
  border-color: var(--accent);
  color: var(--accent);
}

/* ── Main ────────────────────────────────────────────── */
.main {
  flex: 1;
  overflow-y: auto;
  height: 100vh;
}
.main-inner {
  max-width: 860px;
  margin: 0 auto;
  padding: 56px 64px 120px;
}

.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 70vh;
  text-align: center;
  color: var(--text-muted);
}
.empty-state .emoji {
  font-size: 48px;
  margin-bottom: 16px;
}
.empty-state h2 {
  font-size: 22px;
  color: var(--text);
  margin-bottom: 8px;
  font-weight: 600;
}
.empty-state p { max-width: 460px; }

.article-header {
  margin-bottom: 32px;
  padding-bottom: 24px;
  border-bottom: 1px solid var(--border);
}
.breadcrumb {
  font-size: 12px;
  color: var(--text-muted);
  margin-bottom: 10px;
  display: flex;
  align-items: center;
  gap: 6px;
}
.breadcrumb .sep { color: var(--text-faint); }
.breadcrumb .crumb-materia {
  color: var(--accent);
  text-transform: uppercase;
  letter-spacing: 0.04em;
  font-weight: 600;
  font-size: 11px;
}
h1.article-title {
  font-size: 30px;
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.25;
  margin-bottom: 12px;
  color: var(--text);
}
.metadata {
  display: flex;
  gap: 16px;
  font-size: 13px;
  color: var(--text-muted);
  flex-wrap: wrap;
}
.metadata-item { display: inline-flex; align-items: center; gap: 5px; }

.tabs {
  display: flex;
  gap: 4px;
  margin-top: 20px;
  background: var(--bg-elevated);
  padding: 4px;
  border-radius: var(--radius);
  width: fit-content;
}
.tab {
  background: transparent;
  border: none;
  padding: 6px 14px;
  font-size: 13px;
  cursor: pointer;
  border-radius: 6px;
  color: var(--text-muted);
  font-family: inherit;
  font-weight: 500;
  transition: all 0.1s;
}
.tab:hover { color: var(--text); }
.tab.active {
  background: var(--bg);
  color: var(--text);
  box-shadow: var(--shadow);
}

/* ── Markdown rendering ──────────────────────────────── */
.markdown-body { font-size: 15px; line-height: 1.7; color: var(--text); }
.markdown-body > * + * { margin-top: 1em; }
.markdown-body h1 {
  font-size: 26px;
  font-weight: 700;
  letter-spacing: -0.015em;
  margin-top: 2em;
  margin-bottom: 0.6em;
  padding-bottom: 0.4em;
  border-bottom: 1px solid var(--border);
}
.markdown-body h1:first-child { display: none; } /* já mostramos no header */
.markdown-body h2 {
  font-size: 22px;
  font-weight: 700;
  margin-top: 2em;
  margin-bottom: 0.5em;
  letter-spacing: -0.01em;
}
.markdown-body h3 {
  font-size: 17px;
  font-weight: 600;
  margin-top: 1.5em;
  margin-bottom: 0.4em;
}
.markdown-body h4 {
  font-size: 15px;
  font-weight: 600;
  margin-top: 1.2em;
  color: var(--text-muted);
}
.markdown-body p { margin: 0.8em 0; }
.markdown-body a {
  color: var(--accent);
  text-decoration: none;
  border-bottom: 1px solid transparent;
  transition: border-color 0.1s;
}
.markdown-body a:hover { border-bottom-color: var(--accent); }
.markdown-body strong { font-weight: 600; color: var(--text); }
.markdown-body em { font-style: italic; }
.markdown-body ul, .markdown-body ol {
  padding-left: 1.6em;
  margin: 0.8em 0;
}
.markdown-body li { margin: 0.3em 0; }
.markdown-body li > p { margin: 0.4em 0; }
.markdown-body blockquote {
  border-left: 3px solid var(--accent);
  background: var(--accent-bg);
  padding: 12px 18px;
  margin: 1.2em 0;
  border-radius: 0 var(--radius) var(--radius) 0;
  color: var(--text);
}
.markdown-body blockquote > * + * { margin-top: 0.6em; }
.markdown-body code {
  font-family: var(--font-mono);
  font-size: 0.88em;
  background: var(--code-bg);
  padding: 2px 6px;
  border-radius: 4px;
  border: 1px solid var(--border);
}
.markdown-body pre {
  background: var(--code-bg);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 16px;
  overflow-x: auto;
  margin: 1em 0;
  font-size: 13px;
  line-height: 1.5;
}
.markdown-body pre code {
  background: transparent;
  border: none;
  padding: 0;
  font-size: inherit;
}
.markdown-body table {
  border-collapse: collapse;
  width: 100%;
  margin: 1.2em 0;
  font-size: 14px;
  display: block;
  overflow-x: auto;
}
.markdown-body thead {
  background: var(--bg-elevated);
}
.markdown-body th, .markdown-body td {
  border: 1px solid var(--border);
  padding: 8px 12px;
  text-align: left;
  vertical-align: top;
}
.markdown-body th { font-weight: 600; }
.markdown-body tbody tr:nth-child(even) { background: var(--table-stripe); }
.markdown-body hr {
  border: none;
  border-top: 1px solid var(--border);
  margin: 2em 0;
}
.markdown-body img {
  max-width: 100%;
  border-radius: var(--radius);
  border: 1px solid var(--border);
}

/* Reading progress bar */
.progress-bar {
  position: fixed;
  top: 0;
  left: var(--sidebar-width);
  right: 0;
  height: 3px;
  background: transparent;
  z-index: 100;
}
.progress-bar-fill {
  height: 100%;
  background: var(--accent);
  width: 0%;
  transition: width 0.05s;
}

/* Mobile */
.menu-toggle {
  display: none;
  position: fixed;
  top: 12px;
  left: 12px;
  z-index: 101;
  background: var(--bg);
  border: 1px solid var(--border-strong);
  padding: 8px 12px;
  border-radius: 6px;
  font-size: 18px;
  cursor: pointer;
  color: var(--text);
  box-shadow: var(--shadow);
}
.sidebar-backdrop {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.4);
  z-index: 99;
}

@media (max-width: 880px) {
  .menu-toggle { display: block; }
  .sidebar {
    position: fixed;
    z-index: 100;
    transform: translateX(-100%);
    box-shadow: var(--shadow-lg);
  }
  .sidebar.open { transform: translateX(0); }
  .sidebar.open ~ .sidebar-backdrop { display: block; }
  .main-inner { padding: 64px 20px 80px; }
  .progress-bar { left: 0; }
  h1.article-title { font-size: 24px; }
}

/* Scrollbar */
.nav::-webkit-scrollbar, .main::-webkit-scrollbar { width: 8px; height: 8px; }
.nav::-webkit-scrollbar-thumb, .main::-webkit-scrollbar-thumb {
  background: var(--border-strong);
  border-radius: 4px;
}
.nav::-webkit-scrollbar-thumb:hover, .main::-webkit-scrollbar-thumb:hover {
  background: var(--text-faint);
}
</style>
</head>
<body>

<button class="menu-toggle" id="menuToggle" aria-label="Abrir menu">☰</button>

<aside class="sidebar" id="sidebar">
  <div class="sidebar-header">
    <h1>📚 Módulo 10</h1>
    <p>Teste A/B — Autoestudos PBL</p>
    <div class="sidebar-stats" id="sidebarStats"></div>
  </div>
  <div class="search-wrapper">
    <input type="search" id="search" placeholder="Buscar autoestudo..." autocomplete="off">
  </div>
  <nav class="nav" id="nav"></nav>
  <div class="sidebar-footer">
    <button class="icon-btn" id="themeToggle" title="Alternar tema">
      <span id="themeIcon">🌙</span> <span id="themeLabel">Escuro</span>
    </button>
    <button class="icon-btn" id="expandAll" title="Expandir/recolher todos">↕ Todos</button>
  </div>
</aside>
<div class="sidebar-backdrop" id="sidebarBackdrop"></div>

<main class="main" id="main">
  <div class="progress-bar"><div class="progress-bar-fill" id="progressFill"></div></div>
  <div class="main-inner">
    <div class="empty-state" id="emptyState">
      <div class="emoji">📚</div>
      <h2>Bem-vinda!</h2>
      <p>Selecione um autoestudo no menu lateral pra começar a navegar pelo módulo.</p>
    </div>
    <article id="article" hidden>
      <header class="article-header">
        <div class="breadcrumb" id="breadcrumb"></div>
        <h1 class="article-title" id="articleTitle"></h1>
        <div class="metadata" id="metadata"></div>
        <div class="tabs">
          <button class="tab active" data-tab="explicacao">📖 Explicação</button>
          <button class="tab" data-tab="material">📄 Material Original</button>
        </div>
      </header>
      <div class="markdown-body" id="content"></div>
    </article>
  </div>
</main>

<script type="application/json" id="autoestudos-data">__DATA__</script>
<script>
(function() {
  'use strict';

  const DATA = JSON.parse(document.getElementById('autoestudos-data').textContent);
  const $ = (sel) => document.querySelector(sel);
  const $$ = (sel) => Array.from(document.querySelectorAll(sel));

  // Configurar marked
  marked.setOptions({
    breaks: false,
    gfm: true,
    highlight: function(code, lang) {
      if (lang && hljs.getLanguage(lang)) {
        try { return hljs.highlight(code, {language: lang}).value; } catch(e) {}
      }
      return hljs.highlightAuto(code).value;
    }
  });

  // ── Estado ─────────────────────────────────────────
  let currentId = null;
  let currentTab = 'explicacao';
  let searchTerm = '';

  // ── Sidebar ────────────────────────────────────────
  function renderStats() {
    const s = DATA.stats;
    let html = `<span title="Total de autoestudos">📑 ${s.total}</span>`;
    if (s.last_date) html += `<span title="Data do último autoestudo">📅 ${s.last_date}</span>`;
    $('#sidebarStats').innerHTML = html;
  }

  function renderNav() {
    const filtered = DATA.autoestudos.filter(matchSearch);
    const byMateria = {};
    DATA.materias.forEach(m => byMateria[m.slug] = []);
    filtered.forEach(a => {
      if (!byMateria[a.materia_slug]) byMateria[a.materia_slug] = [];
      byMateria[a.materia_slug].push(a);
    });

    let html = '';
    for (const m of DATA.materias) {
      const items = byMateria[m.slug] || [];
      const groupId = `group-${m.slug}`;
      html += `<div class="nav-group" data-group="${m.slug}" id="${groupId}">`;
      html += `<div class="nav-group-header" data-toggle="${m.slug}">`;
      html += `<span>${m.emoji}</span> <span>${m.label}</span>`;
      html += `<span class="nav-group-count">${items.length}</span>`;
      html += `<span class="chev">▾</span>`;
      html += `</div>`;
      html += `<div class="nav-items">`;
      if (items.length === 0) {
        html += `<div class="nav-empty">Nenhum autoestudo${searchTerm ? ' encontrado' : ''}</div>`;
      } else {
        for (const a of items) {
          html += `<a class="nav-item" data-id="${a.id}" href="#${a.id}">`;
          html += `<span class="nav-item-num">Autoestudo ${a.numero}</span>`;
          html += `<span class="nav-item-title">${escapeHtml(a.title)}</span>`;
          if (a.date) html += `<span class="nav-item-date">${a.date}</span>`;
          html += `</a>`;
        }
      }
      html += `</div></div>`;
    }
    $('#nav').innerHTML = html;

    // Restaurar grupos recolhidos
    const collapsed = JSON.parse(localStorage.getItem('collapsedGroups') || '[]');
    collapsed.forEach(slug => {
      const g = document.getElementById(`group-${slug}`);
      if (g) g.classList.add('collapsed');
    });

    bindNavEvents();
    highlightActive();
  }

  function matchSearch(a) {
    if (!searchTerm) return true;
    const t = searchTerm.toLowerCase();
    return (
      a.title.toLowerCase().includes(t) ||
      a.materia_label.toLowerCase().includes(t) ||
      (a.date || '').includes(t) ||
      (a.explicacao || '').toLowerCase().includes(t) ||
      (a.material || '').toLowerCase().includes(t)
    );
  }

  function bindNavEvents() {
    $$('.nav-group-header').forEach(el => {
      el.addEventListener('click', () => {
        const slug = el.dataset.toggle;
        const g = document.getElementById(`group-${slug}`);
        g.classList.toggle('collapsed');
        const collapsed = $$('.nav-group.collapsed').map(x => x.dataset.group);
        localStorage.setItem('collapsedGroups', JSON.stringify(collapsed));
      });
    });
    $$('.nav-item').forEach(el => {
      el.addEventListener('click', (e) => {
        e.preventDefault();
        const id = el.dataset.id;
        openAutoestudo(id);
        if (window.innerWidth <= 880) closeSidebar();
      });
    });
  }

  function highlightActive() {
    $$('.nav-item').forEach(el => {
      el.classList.toggle('active', el.dataset.id === currentId);
    });
  }

  // ── Conteúdo ───────────────────────────────────────
  function openAutoestudo(id) {
    const a = DATA.autoestudos.find(x => x.id === id);
    if (!a) return;
    currentId = id;
    location.hash = id;

    $('#emptyState').hidden = true;
    $('#article').hidden = false;

    const m = DATA.materias.find(x => x.slug === a.materia_slug);
    $('#breadcrumb').innerHTML =
      `<span class="crumb-materia">${m.emoji} ${m.materia_label || m.label}</span>` +
      `<span class="sep">›</span>` +
      `<span>Autoestudo ${a.numero}</span>`;
    $('#articleTitle').textContent = a.title;

    let meta = '';
    if (a.date) meta += `<span class="metadata-item">📅 ${a.date}</span>`;
    meta += `<span class="metadata-item">📖 ${countWords(a.explicacao)} palavras (explicação)</span>`;
    $('#metadata').innerHTML = meta;

    renderTab(currentTab);
    highlightActive();
    $('#main').scrollTop = 0;
  }

  function renderTab(tab) {
    currentTab = tab;
    $$('.tab').forEach(t => t.classList.toggle('active', t.dataset.tab === tab));
    const a = DATA.autoestudos.find(x => x.id === currentId);
    if (!a) return;
    const md = tab === 'material' ? a.material : a.explicacao;
    if (!md) {
      $('#content').innerHTML = '<p style="color: var(--text-muted); font-style: italic;">Conteúdo não disponível.</p>';
      return;
    }
    $('#content').innerHTML = marked.parse(md);
    // Limpa links que apontam pra arquivos .md — converte pra hash interno
    rewriteInternalLinks();
  }

  function rewriteInternalLinks() {
    const links = $$('#content a');
    links.forEach(a => {
      const href = a.getAttribute('href') || '';
      // Reescrever links como ../autoestudo-XX-foo/02-explicacao.md
      const m = href.match(/(?:\.\.\/)*([^\/]+)\/(autoestudo-[^\/]+)\/0[12]-(?:explicacao|material)\.md/);
      if (m) {
        const materia = m[1];
        const slug = m[2];
        const id = `${materia}-${slug}`;
        const target = DATA.autoestudos.find(x => x.id === id);
        if (target) {
          a.setAttribute('href', `#${id}`);
          a.addEventListener('click', (ev) => {
            ev.preventDefault();
            openAutoestudo(id);
          });
        }
      }
    });
  }

  function countWords(s) {
    if (!s) return 0;
    return s.trim().split(/\s+/).length.toLocaleString('pt-BR');
  }

  function escapeHtml(s) {
    return s.replace(/[&<>"']/g, c => ({
      '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'
    })[c]);
  }

  // ── Tabs ───────────────────────────────────────────
  $$('.tab').forEach(t => {
    t.addEventListener('click', () => renderTab(t.dataset.tab));
  });

  // ── Search ─────────────────────────────────────────
  $('#search').addEventListener('input', (e) => {
    searchTerm = e.target.value.trim();
    renderNav();
  });

  // ── Theme ──────────────────────────────────────────
  function applyTheme(t) {
    document.documentElement.setAttribute('data-theme', t);
    $('#themeIcon').textContent = t === 'dark' ? '☀️' : '🌙';
    $('#themeLabel').textContent = t === 'dark' ? 'Claro' : 'Escuro';
    // Trocar tema do hljs
    const themeUrl = t === 'dark'
      ? 'https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/styles/github-dark.min.css'
      : 'https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/styles/github.min.css';
    $('#hljs-theme').href = themeUrl;
    localStorage.setItem('theme', t);
  }
  $('#themeToggle').addEventListener('click', () => {
    const cur = document.documentElement.getAttribute('data-theme');
    applyTheme(cur === 'dark' ? 'light' : 'dark');
  });
  applyTheme(localStorage.getItem('theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'));

  // ── Expand/collapse all ────────────────────────────
  $('#expandAll').addEventListener('click', () => {
    const groups = $$('.nav-group');
    const anyExpanded = groups.some(g => !g.classList.contains('collapsed'));
    groups.forEach(g => g.classList.toggle('collapsed', anyExpanded));
    const collapsed = $$('.nav-group.collapsed').map(x => x.dataset.group);
    localStorage.setItem('collapsedGroups', JSON.stringify(collapsed));
  });

  // ── Mobile sidebar ─────────────────────────────────
  function openSidebar() { $('#sidebar').classList.add('open'); }
  function closeSidebar() { $('#sidebar').classList.remove('open'); }
  $('#menuToggle').addEventListener('click', openSidebar);
  $('#sidebarBackdrop').addEventListener('click', closeSidebar);

  // ── Reading progress ──────────────────────────────
  $('#main').addEventListener('scroll', () => {
    const m = $('#main');
    const pct = (m.scrollTop / (m.scrollHeight - m.clientHeight)) * 100;
    $('#progressFill').style.width = `${Math.min(pct, 100)}%`;
  });

  // ── Hash routing ──────────────────────────────────
  function loadFromHash() {
    const hash = location.hash.replace(/^#/, '');
    if (hash && DATA.autoestudos.find(x => x.id === hash)) {
      openAutoestudo(hash);
    }
  }
  window.addEventListener('hashchange', loadFromHash);

  // ── Keyboard shortcuts ────────────────────────────
  document.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
      e.preventDefault();
      $('#search').focus();
    } else if (e.key === 'Escape') {
      if (document.activeElement === $('#search')) $('#search').blur();
      closeSidebar();
    } else if (currentId && !e.ctrlKey && !e.metaKey && !e.altKey
               && document.activeElement.tagName !== 'INPUT') {
      const sorted = DATA.autoestudos;
      const i = sorted.findIndex(x => x.id === currentId);
      if (e.key === 'j' && i < sorted.length - 1) openAutoestudo(sorted[i+1].id);
      else if (e.key === 'k' && i > 0) openAutoestudo(sorted[i-1].id);
      else if (e.key === '1') renderTab('explicacao');
      else if (e.key === '2') renderTab('material');
    }
  });

  // ── Init ──────────────────────────────────────────
  renderStats();
  renderNav();
  loadFromHash();
})();
</script>
</body>
</html>
"""


if __name__ == "__main__":
    autoestudos = collect()
    build_html(autoestudos)
