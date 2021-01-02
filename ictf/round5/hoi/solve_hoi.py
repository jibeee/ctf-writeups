import base64
import itertools


def main():
    flag_parts = ("N0X2l", "ZV90a", "ntqdX", "nbm9y", "aWN0Z", "GlzX2", "d1eX0")
    for perm in itertools.permutations(flag_parts, len(flag_parts)):
        candidate = base64.b64decode("".join(perm) + "=")
        try:
            flag = candidate.decode("ascii")
            if flag.startswith("ictf{") and flag.endswith("}"):
                print(flag)
        except UnicodeDecodeError:
            pass


if __name__ == "__main__":
    main()
