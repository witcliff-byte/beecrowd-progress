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

def count_added_today(glob_pattern):
    today = datetime.date.today().isoformat()
    try:
        cmd = ['git', 'log', f'--since={today}T00:00:00', '--pretty=format:', '--name-only', '--diff-filter=A']
        out = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
        added= set(line.strip() for line in out.splitlines() if line.strip())
        return sum(1 for f in added if fnmatch.fnmatch(f, glob_pattern))
    except Exception:
        return 0

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
    today_added = count_added_today(SOLUTION_GLOB)
    today_str = datetime.date.today().strftime('%d/%m/%Y')
    changed = update_readme(README_PATH, today_str, today_added, total)
    if changed:
        git_commit_push(README_PATH)

if __name__ == '__main__':
    main()
