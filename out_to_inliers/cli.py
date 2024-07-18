"""Console script for out_to_inliers."""

import fire


def help() -> None:
    print("out_to_inliers")
    print("=" * len("out_to_inliers"))
    print(
        "Manipulation of outliers under robust methods to transform them closer to inliers"
    )


def main() -> None:
    fire.Fire({"help": help})


if __name__ == "__main__":
    main()  # pragma: no cover
