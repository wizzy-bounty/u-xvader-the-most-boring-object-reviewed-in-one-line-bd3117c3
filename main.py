import os

TEXT = "The doormat gets stepped on by everyone, thanked by no one, and still says 'welcome'."

def resolve_out_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

def main():
    out_dir = resolve_out_dir()
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
