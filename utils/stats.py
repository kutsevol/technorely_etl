import pandas as pd


def get_count_rows(df):
    """
    :param df: pandas DataFrame
    :return: integer of rows
    """
    return df.shape[0]


def get_stats_by_gender(df):
    """
    :param df: pandas DataFrame
    :return: dict with key - gender, value - count
    """
    group_gender = df.groupby(["gender"]).groups.keys()

    return {
        group: len(df.groupby(["gender"]).groups.get(group))
        for group in group_gender
    }


def get_stats_of_popular_days_of_week(df, col):
    """
    :param df: pandas DataFrame
    :param col: column to convert in datetime
    :return: tuple of the most and least popular days
    """
    day_of_week = pd.to_datetime(df[col],
                                 utc=True).dt.day_name().value_counts()

    return day_of_week.index[0], day_of_week.index[-1]


def get_top_n_in_column(df, col, n=10):
    """
    :param df: pandas DataFrame
    :param col: name of column
    :param n: how many position should be returned
    :return: list of top n popular record in column
    """
    return df[col].value_counts()[:n]
