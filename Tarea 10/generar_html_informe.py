from __future__ import annotations

from pathlib import Path
import re
import sys

import markdown


ROOT = Path(__file__).resolve().parent
DEFAULT_SOURCE = ROOT / "Informe_Tarea_Forense.md"

PAGE_BREAK_HEADINGS = {
  "2. Línea de tiempo",
  "7. Trabajos realizados",
  "8. Hallazgos principales",
  "10. Conclusiones",
}

FIGURE_BLOCK_RE = re.compile(
    r'<p><img alt="(?P<alt>[^"]+)" src="(?P<src>[^"]+)"></p>\s*<p class="caption"><em>(?P<caption>Figura\s+(?P<number>\d+)\..*?)</em></p>',
    flags=re.DOTALL,
)

MARKDOWNLINT_COMMENT_RE = re.compile(
    r"<!--\s*markdownlint-(?:disable|enable)\s+MD060\s*-->\s*"
)


def relocate_figures(body: str) -> str:
    figures: list[dict[str, str]] = []

    def replacement(match: re.Match[str]) -> str:
        number = match.group("number")
        figures.append(
            {
                "number": number,
                "alt": match.group("alt"),
                "src": match.group("src"),
                "caption": match.group("caption"),
            }
        )
        return (
            '<p class="figure-reference">'
            f'Referencia visual: vease la <a href="#figura-{number}">Figura {number}</a> '
          'en el Anexo de figuras.</p>'
        )

    body_without_inline_figures = FIGURE_BLOCK_RE.sub(replacement, body)
    if not figures:
        return body_without_inline_figures

    annex_parts = ['<h2 class="page-break">Anexo de figuras</h2>', '<section class="annex-list">']
    for figure in figures:
        annex_parts.append(
            f'<figure class="annex-figure" id="figura-{figure["number"]}">'
            f'<img alt="{figure["alt"]}" src="{figure["src"]}">'
            f'<figcaption><em>{figure["caption"]}</em></figcaption>'
            '</figure>'
        )
    annex_parts.append('</section>')
    return body_without_inline_figures + ''.join(annex_parts)


def build_html(markdown_text: str, title: str) -> str:
  body = markdown.markdown(
    markdown_text,
    extensions=["tables", "fenced_code", "sane_lists"],
    output_format="html5",
  )

  body = MARKDOWNLINT_COMMENT_RE.sub('', body)

  for heading in PAGE_BREAK_HEADINGS:
    body = body.replace(f"<h2>{heading}</h2>", f'<h2 class="page-break">{heading}</h2>')

  body = body.replace(
    '<h2>Análisis de Memoria, Disco y Triaje</h2>\n<ul>',
    '<h2>Análisis de Memoria, Disco y Triaje</h2>\n<ul class="document-meta">',
    1,
  )

  body = re.sub(
    r"<p><em>(Figura\s+\d+\..*?)</em></p>",
    r'<p class="caption"><em>\1</em></p>',
    body,
    flags=re.DOTALL,
  )

  body = relocate_figures(body)

  return f"""<!DOCTYPE html>
<html lang=\"es\">
<head>
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
  <title>{title}</title>
  <style>
    :root {{
      --text: #1f1f1f;
      --muted: #5f5f5f;
      --line: #d7d7d7;
      --paper: #ffffff;
      --accent: #163a5f;
    }}

    * {{ box-sizing: border-box; }}

    body {{
      margin: 0;
      color: var(--text);
      background: #f2f2f2;
      font-family: Cambria, Georgia, "Times New Roman", serif;
      line-height: 1.55;
    }}

    .page {{
      width: min(210mm, 100%);
      min-height: 297mm;
      margin: 0 auto;
      padding: 18mm 16mm 20mm;
      background: var(--paper);
      box-shadow: 0 0 18px rgba(0, 0, 0, 0.06);
    }}

    h1, h2, h3 {{
      color: var(--accent);
      line-height: 1.25;
      margin-top: 1.2em;
      margin-bottom: 0.5em;
    }}

    h1 {{
      text-align: center;
      font-size: 22pt;
      margin-top: 0;
      margin-bottom: 0.4em;
      text-transform: none;
    }}

    h2 {{
      font-size: 15.5pt;
      border-bottom: 1px solid var(--line);
      padding-bottom: 0.18em;
    }}

    h3 {{
      font-size: 12.5pt;
    }}

    p {{
      margin: 0 0 0.9em;
      text-align: justify;
      text-justify: inter-word;
      orphans: 3;
      widows: 3;
    }}

    hr {{
      border: 0;
      border-top: 1px solid var(--line);
      margin: 1.2em 0;
    }}

    ul, ol {{
      margin: 0 0 1em 1.35em;
    }}

    li {{
      margin-bottom: 0.35em;
      text-align: justify;
    }}

    strong {{
      font-weight: 700;
    }}

    code {{
      font-family: Consolas, "Courier New", monospace;
      font-size: 0.92em;
      background: #f5f7fa;
      padding: 0.08em 0.28em;
      border-radius: 3px;
    }}

    pre {{
      background: #f5f7fa;
      border: 1px solid #e4e8ee;
      padding: 0.9em;
      overflow-x: auto;
    }}

    pre code {{
      background: transparent;
      padding: 0;
    }}

    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 1em 0 1.2em;
      font-size: 0.96em;
    }}

    th, td {{
      border: 1px solid var(--line);
      padding: 0.48em 0.58em;
      vertical-align: top;
      text-align: left;
    }}

    th {{
      background: #eef3f8;
    }}

    img {{
      display: block;
      max-width: 100%;
      height: auto;
      margin: 1em auto 0.35em;
      border: 1px solid #d9dee5;
    }}

    .caption {{
      font-size: 0.95em;
      color: var(--muted);
      text-align: justify;
      margin-bottom: 1.1em;
    }}

    .figure-reference {{
      font-size: 0.95em;
      color: var(--muted);
      font-style: italic;
      margin: 0.35em 0 1.05em;
    }}

    .figure-reference a {{
      color: var(--accent);
      text-decoration: none;
      border-bottom: 1px solid rgba(22, 58, 95, 0.35);
    }}

    .annex-list {{
      margin-top: 1.2em;
    }}

    .annex-figure {{
      margin: 0 0 1.8em;
      break-inside: avoid;
      page-break-inside: avoid;
    }}

    .annex-figure img {{
      margin-top: 0;
    }}

    .annex-figure figcaption {{
      font-size: 0.95em;
      color: var(--muted);
      text-align: justify;
      margin-top: 0.35em;
    }}

    .document-meta {{
      list-style: none;
      margin: 0.9em 0 1.35em;
      padding: 0.95em 1.15em;
      border: 1px solid var(--line);
      background: #f8fafc;
    }}

    .document-meta li {{
      margin-bottom: 0.42em;
      text-align: left;
    }}

    .document-meta li:last-child {{
      margin-bottom: 0;
    }}

    .document-meta strong {{
      color: var(--accent);
    }}

    .page-break {{
      break-before: page;
      page-break-before: always;
    }}

    @page {{
      size: A4;
      margin: 16mm;
    }}

    @media print {{
      body {{ background: #ffffff; }}

      .page {{
        width: auto;
        min-height: auto;
        margin: 0;
        padding: 0;
        box-shadow: none;
      }}

      img, table, pre {{
        break-inside: avoid;
        page-break-inside: avoid;
      }}

      .annex-figure {{
        break-inside: avoid;
        page-break-inside: avoid;
      }}

      h2, h3 {{
        break-after: avoid;
        page-break-after: avoid;
      }}

      .caption {{
        break-after: avoid;
        page-break-after: avoid;
      }}
    }}
  </style>
</head>
<body>
  <main class=\"page\">
    {body}
  </main>
</body>
</html>
"""


def resolve_paths() -> tuple[Path, Path]:
  if len(sys.argv) > 1:
    source = Path(sys.argv[1]).resolve()
  else:
    source = DEFAULT_SOURCE

  if len(sys.argv) > 2:
    target = Path(sys.argv[2]).resolve()
  else:
    target = source.with_suffix(".html")

  return source, target


def build_title(source: Path) -> str:
  return source.stem.replace("_", " ")


def main() -> None:
  source, target = resolve_paths()
  markdown_text = source.read_text(encoding="utf-8").lstrip("\ufeff")
  html = build_html(markdown_text, build_title(source))
  target.write_text(html, encoding="utf-8")
  print(target)


if __name__ == "__main__":
    main()