import os
import random
import subprocess
from datetime import datetime, timedelta

def main():
    start_date = datetime(2026, 8, 11)
    end_date = datetime(2026, 10, 1)
    current_date = start_date

    file_path = "contribution_activity.txt"
    total_commits = 0

    print(f"Starting commit generation from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}...")

    while current_date <= end_date:
        num_commits = random.randint(5, 20)
        for i in range(num_commits):
            hour = random.randint(9, 21)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            
            commit_time = current_date.replace(hour=hour, minute=minute, second=second)
            date_str = commit_time.strftime("%Y-%m-%dT%H:%M:%S")

            with open(file_path, "a") as f:
                f.write(f"Activity log entry: {date_str}\n")

            subprocess.run(["git", "add", file_path], check=True)

            env = os.environ.copy()
            env["GIT_AUTHOR_DATE"] = date_str
            env["GIT_COMMITTER_DATE"] = date_str

            msg = f"Update learning activity log ({date_str})"
            subprocess.run(["git", "commit", "-m", msg], env=env, check=True)
            total_commits += 1

        current_date += timedelta(days=1)

    print(f"Successfully created {total_commits} backdated commits!")

if __name__ == "__main__":
    main()
