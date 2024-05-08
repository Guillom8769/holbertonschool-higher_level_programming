#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    # Trier les noms et filtrer ceux qui ne commencent pas par '__'
    for name in sorted(dir(hidden_4)):
        if not name.startswith("__"):
            print(name)
