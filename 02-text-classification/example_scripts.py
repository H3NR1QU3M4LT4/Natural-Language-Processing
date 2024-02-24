from datasets import load_dataset


def main():
    emotions = load_dataset("emotion")
    emotions.set_format(type="pandas")
    df = emotions["train"].to_pandas()
    print(df.head())


if __name__ == "__main__":
    main()