#!/usr/bin/env python3
import yaml
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

ROOT = Path(__file__).parent
DATA = ROOT / "data"
TEMPLATES = ROOT / "templates"
OUTPUT = ROOT / "docs"

DATA_FILES = [
    "site",
    "nav",
    "hero",
    "offerings",
    "about",
    "services",
    "current_work",
    "contact",
]

def load_yaml(name):
    with open(DATA / f"{name}.yml") as f:
        return yaml.safe_load(f)

def main():
    context = {name: load_yaml(name) for name in DATA_FILES}

    env = Environment(loader=FileSystemLoader(TEMPLATES))
    template = env.get_template("index.html")

    html = template.render(**context)

    OUTPUT.mkdir(parents=True, exist_ok=True)
    (OUTPUT / "index.html").write_text(html)
    print(f"Generated {OUTPUT / 'index.html'}")

if __name__ == "__main__":
    main()