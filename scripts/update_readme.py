import os
import subprocess
from pathlib import Path
import fnmatch
import datetime
import re

README_PATH = os.getenv('README_PATH', 'README.md')
SOLUTION_GLOB = os.getenv('SOLUTION_GLOB', '**/*.py')

def list_solutions(glob_pattern):
    p = Path('.')
    files = [str(fp) for fp in p.rglob('*') if fp.is_file() and fnmatch.fnmatch(str(fp), glob_pattern) and '.git/' not in str(fp)]
    return files

def count_added_today_from_readme(path, today_str):
    content = Path(path).read_text(encoding='utf-8')
    lines = content.splitlines()
    try:
        start = next(i for i, l in enumerate(lines) if l.strip().startswith('## Stats Diárias'))
    except StopIteration:
        return 0
    header_idx = None
    for i in range(start, min(start + 20, len(lines))):
        if lines[i].strip().startswith('|') and 'Data' in lines[i]:
            header_idx = i
            break
    if header_idx is None or header_idx + 1 >= len(lines):
        return 0
    sep_idx = header_idx + 1
    row_idx = sep_idx + 1
    rows = []
    while row_idx < len(lines) and lines[row_idx].strip().startswith('|'):
        rows.append(lines[row_idx])
        row_idx += 1
    def parse_total(row):
        m = re.search(r'\*\*(\d+)\*\*', row)
        if m:
            return int(m.group(1))
        cols = [c.strip() for c in row.strip('|').split('|')]
        return int(cols[2]) if len(cols) >= 3 and cols[2].isdigit() else 0
    if not rows:
        return 0
    today_row = rows[0] if today_str in rows[0] else None
    prev_row = rows[1] if today_row and len(rows) > 1 else (rows[0] if not today_row else None)
    prev_total = parse_total(prev_row) if prev_row else 0
    return prev_total

def update_readme(path, today_str, today_count, total_count):
    content = Path(path).read_text(encoding='utf-8')
    lines = content.splitlines()
    # find "Stats Diárias" and the table header
    try:
        start = next(i for i,l in enumerate(lines) if l.strip().startswith('## Stats Diárias'))
    except StopIteration:
        return False

    header_idx = None
    for i in range(start, min(start+20, len(lines))):
        if lines[i].strip().startswith('|') and 'Data' in lines[i]:
            header_idx = i
            break
    if header_idx is None or header_idx+1 >= len(lines):
        return False
    sep_idx = header_idx + 1
    insert_idx = sep_idx + 1

    first_row = lines[insert_idx] if insert_idx < len(lines) and lines[insert_idx].strip().startswith('|') else ''
    rank_col = ''
    if first_row:
        cols = [c.strip() for c in first_row.strip('|').split('|')]
        if len(cols) >= 4:
            rank_col = cols[3]
    new_row = f"| {today_str} | {today_count} | **{total_count}**| {rank_col} |"

    if first_row and today_str in first_row:
        lines[insert_idx] = new_row
    else:
        lines.insert(insert_idx, new_row)
    Path(path).write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return True

def git_commit_push(path, message='chore: atualizar stats'):
    try:
        subprocess.run(['git', 'config', 'user.name', 'github-actions[bot]'], check=True)
        subprocess.run(['git', 'config', 'user.email', 'github-actions[bot]@users.noreply.github.com'], check=True)
        subprocess.run(['git', 'add', path], check=True)
        subprocess.run(['git', 'commit', '-m', message], check=True)
        subprocess.run(['git', 'push'], check=True)
    except subprocess.CalledProcessError:
        pass

def main():
    sols = list_solutions(SOLUTION_GLOB)
    total = len(sols)
    today_str = datetime.date.today().strftime('%d/%m/%Y')
    prev_total = count_added_today_from_readme(README_PATH, today_str)
    today_added = max(total - prev_total, 0)
    changed = update_readme(README_PATH, today_str, today_added, total)
    if changed:
        git_commit_push(README_PATH)

if __name__ == '__main__':
    main()
