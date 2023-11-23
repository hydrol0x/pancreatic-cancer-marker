def to_binary(df):
    new_df = df.copy()

    new_df['diagnosis'] = df['diagnosis'].apply(
        lambda x: 0 if x in [1, 2] else 1)
    return new_df
