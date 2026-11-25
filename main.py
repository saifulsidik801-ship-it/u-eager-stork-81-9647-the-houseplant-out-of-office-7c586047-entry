import os

ENTRY = "Out of office. Ignored since March, down to my last leaf — water me first, then we'll talk about your email."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
