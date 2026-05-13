import re
import csv
import sys
import os

LOG_FILE = 'nginx.log'
OUTPUT_FILE = 'report.csv'

LOG_REGEX = r'(\S+) - - \[(.*?)\] "(\S+) (\S+) \S+" (\d+) (\d+)'

def main():
    if not os.path.exists(LOG_FILE):
        print(f"Error: file {LOG_FILE} is not found.")
        return

    rows = []
    with open(LOG_FILE, 'r') as f:
        for line in f:
            match = re.search(LOG_REGEX, line)
            if match:
                rows.append(list(match.groups()))

    if len(sys.argv) > 1:
        status_filter = sys.argv[1]
        rows = [r for r in rows if r[4] == status_filter]
        print(f"Status filter applied: {status_filter}")

    rows.sort(key=lambda x: x[0])

    headers = ['IP', 'Timestamp', 'Method', 'URL', 'Status', 'Size']
    with open(OUTPUT_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    
    print(f"Data saved to {OUTPUT_FILE}")

    print("Pushing to Git...")
    os.system(f"git add {OUTPUT_FILE}")
    os.system(f'git commit -m "Automatic log update: {OUTPUT_FILE}"')
    os.system("git push")

if __name__ == "__main__":
    main()