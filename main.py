import os

LINE = "I submitted at 11:58, two minutes before the deadline, exactly as planned. My internal clock has read 11:58 since March 2019, and I have never once doubted it. It is a clock. Clocks do not lie."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w") as f:
    f.write(LINE + "\n")

# Read back what the grader will see and refuse to continue silently if
# the output ever differs from the intended line.
with open("/output/entry.txt") as f:
    assert f.read() == LINE + "\n", "output mismatch"

# Copy to repo root for local inspection; the grader mounts the repo
# read-only, so a failure here must never crash the run.
try:
    repo_root = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(repo_root, "entry.txt"), "w") as f:
        f.write(LINE + "\n")
except Exception:
    pass
