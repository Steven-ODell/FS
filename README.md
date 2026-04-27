# Terminal File Explorer

A minimal TUI file explorer built with Python and blessed. Navigate your filesystem and open files directly in nvim from the terminal.

## Features

- Vim-style navigation (j/k/l/h)
- Navigate into folders and back up with h
- Opens files in nvim with cwd set correctly for plugins like Snacks explorer

## Requirements

- Python 3
- neovim

## Install

```bash
pip install blessed
```

## Run

```bash
python3 app.py
```

## Controls

| Key | Action |
|-----|--------|
| j / ↓ | Move down |
| k / ↑ | Move up |
| l / Enter | Open folder or file |
| h / b | Go back |
| q | Quit |

## Notes

- `baseDir` is hardcoded to a path in `app.py` — change this before running
