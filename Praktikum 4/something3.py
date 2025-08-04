import argparse
from pathlib import Path
import opensmile

def main():
    parser = argparse.ArgumentParser(description="Extract ComParE 2016 LLDs.")
    parser.add_argument(
    "audio",
    type=Path,
    nargs="?",
    default=Path(r"######################"),
    help="#########################",
)
    parser.add_argument("--out", type=Path, default=r"###########################", help="Output CSV path.")
    args = parser.parse_args()

    smile = opensmile.Smile(
        feature_set=opensmile.FeatureSet.ComParE_2016,
        feature_level=opensmile.FeatureLevel.LowLevelDescriptors,
    )
    df = smile.process_file(str(args.audio))
    df.to_csv(args.out)
    print(f"Saved full LLD matrix {df.shape} to {args.out}")

    # Show MFCC subset
    mfcc_cols = df.filter(like="mfcc").columns
    print("MFCC preview:\n", df[mfcc_cols].head())

if __name__ == "__main__":
    main()
