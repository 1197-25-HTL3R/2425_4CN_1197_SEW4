import subprocess, sys

if __name__ == "__main__":
    print(f"{sys.argv} startet einen Subprozess:")
    result = subprocess.run(["python", "write_stdout_strerr.py"],
    capture_output=True, text=True, check=False)
    print(result.stdout)
    print(result.stderr)
    print(f"Der returncode war: {result.returncode}")