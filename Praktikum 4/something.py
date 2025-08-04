import argparse
from pathlib import Path
import opensmile

def main():
    parser = argparse.ArgumentParser(description="Extract eGeMAPS Functionals.")
    parser.add_argument(
    "audio",
    type=Path,
    nargs="?",
    default=Path(r"#############################"),
    help="#######################",
)

    parser.add_argument("--out", type=Path, default=r"##################################", help="Output CSV path.")
    args = parser.parse_args()

    smile = opensmile.Smile(
        feature_set=opensmile.FeatureSet.eGeMAPSv02,
        feature_level=opensmile.FeatureLevel.Functionals,
    )
    df = smile.process_file(str(args.audio))
    df.to_csv(args.out, index=True)
    print(f"Saved {df.shape[1]} functionals to {args.out} (shape: {df.shape})")

if __name__ == "__main__":
    main()
