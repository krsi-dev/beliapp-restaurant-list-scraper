import argparse
import beliapp

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="python ."
    )

    parser.add_argument(
        "username",
        type=str,
        help="target beliapp user"
    )

    kwargs = parser.parse_args()
    beliapp.scrape(username=kwargs.username)