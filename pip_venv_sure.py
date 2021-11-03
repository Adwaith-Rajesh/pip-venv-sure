import argparse
import os
import sys


def venv_is_active() -> bool:
    return True if os.environ.get("VIRTUAL_ENV", None) else False


def main() -> int:

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-anv", "--allow-no-venv",
                        action="store_true",
                        help="Install packages without checking whether a venv is activated.")
    parser.add_argument("--help", action="store_true", help="Show help")

    args, rest = parser.parse_known_args()

    if args.help:
        parser.print_help()

        print()
        print("pip3 --help")
        print("=" * 79)
        os.execvp("pip3", ("pip3", "--help"))

    if venv_is_active() or args.allow_no_venv:

        cmd = (
            "pip3",
            *rest
        )

    else:
        print("Activate your venv kiddo!", file=sys.stderr)
        return 1

    return os.execvp(cmd[0], cmd)


if __name__ == "__main__":
    raise SystemExit(main())
