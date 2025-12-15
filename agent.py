import json
from pathlib import Path


def load_malis():
    path = Path("data/mails.json")
    with path.open("r", encoding="utf-8") as f:
        mails = json.load(f)
    return mails


def main():
    malis = load_malis()
    print("Loaded malis:")
    print(malis)


if __name__ == '__main__':
    main()
