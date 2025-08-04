import argparse
from pathlib import Path
import numpy as np
import opensmile

def main():
    parser = argparse.ArgumentParser(description="Extract eGeMAPS LLDs.")
    parser.add_argument(
    "audio",
    type=Path,
    nargs="?",
    default=Path(r"###########################"),
    help="########################",
)
    parser.add_argument("--out", type=Path, default=r"##########################", help="Output CSV path.")
    args = parser.parse_args()

    smile = opensmile.Smile(
        feature_set=opensmile.FeatureSet.eGeMAPSv02,
        feature_level=opensmile.FeatureLevel.LowLevelDescriptors,
    )
    df = smile.process_file(str(args.audio))
    df.replace(-201.0, np.nan, inplace=True)

    df.to_csv(args.out)
    print(f"Saved LLD matrix {df.shape} to {args.out}")

if __name__ == "__main__":
    main()
