import warnings

import datasense as ds
import pandas as pd


warnings.filterwarnings("ignore")
series1_paired = pd.Series(
    data=[
        68, 76, 74, 71, 71, 72, 75, 83, 75, 74, 76, 77, 78, 75, 75, 84, 77,
        69, 75, 65
    ],
    name="before"
)
series2_paired = pd.Series(
    data=[
        67, 77, 74, 74, 69, 70, 71, 77, 71, 74, 73, 68, 71, 72, 77, 80, 74,
        73, 72, 62
    ],
    name="after"
)


def test_paired_t():
    result = ds.paired_t(
        series1=series1_paired,
        series2=series2_paired,
        significance_level=0.05,
        alternative_hypothesis="two-sided",
    )
    # expected = (
    # t statistic, t p value, t power,
    # Shapiro-Wilk statistic, Shapiro-Wilk p value,
    # Anderson-Darling test statistic, Anderson-Darling p value
    # )
    expected = (
        3.0234339882840073, 0.006989193823492975,
        0.9718567132949829, 0.7935113906860352,
        0.33171651643374744, 0.692,
        0.14709700945048904, 0.3071349516596349
    )
    assert result == expected
    result = ds.paired_t(
        series1=series1_paired,
        series2=series2_paired,
        significance_level=0.05,
        alternative_hypothesis="less"
    )
    expected = (
        3.0234339882840073, 0.9965054030882535,
        0.9718567132949829, 0.7935113906860352,
        0.33171651643374744, 0.692,
        0.14709700945048904, 0.3071349516596349
    )
    assert result == expected
    result = ds.paired_t(
        series1=series1_paired,
        series2=series2_paired,
        significance_level=0.05,
        alternative_hypothesis="greater"
    )
    expected = (
        3.0234339882840073, 0.0034945969117464873,
        0.9718567132949829, 0.7935113906860352,
        0.33171651643374744, 0.692,
        0.14709700945048904, 0.3071349516596349
    )
    result = ds.paired_t(
        series1=series1_paired,
        series2=series2_paired,
        significance_level=0.05,
        alternative_hypothesis="two-sided",
        hypothesized_value=4
    )
    expected = (
        -2.4737187176869146, 0.022976718604245508,
        0.9718567132949829, 0.7935113906860352,
        0.33171651643374744, 0.692,
        0.14709700945048904, 0.3071349516596349
    )
    assert result == expected
    result = ds.paired_t(
        series1=series1_paired,
        series2=series2_paired,
        significance_level=0.05,
        alternative_hypothesis="less",
        hypothesized_value=4
    )
    expected = (
        -2.4737187176869146, 0.011488359302122775,
        0.9718567132949829, 0.7935113906860352,
        0.33171651643374744, 0.692,
        0.14709700945048904, 0.3071349516596349
    )
    assert result == expected
    result = ds.paired_t(
        series1=series1_paired,
        series2=series2_paired,
        significance_level=0.05,
        alternative_hypothesis="greater",
        hypothesized_value=4
    )
    expected = (
        -2.4737187176869146, 0.9885116406978772,
        0.9718567132949829, 0.7935113906860352,
        0.33171651643374744, 0.692,
        0.14709700945048904, 0.3071349516596349
    )
    assert result == expected
