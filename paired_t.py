#! /usr/bin/env python3
"""
'Paired' means that there is a one-to-one correspondence between the values in
two samples. If  𝑥1,𝑥2,...,𝑥𝑛  and  𝑦1,𝑦2,...,𝑌𝑛  are two samples, then 𝑥𝑖
corresponds to  𝑦𝑖 .

Example. A sample of a product is taken from a process. Measurements are made
of the 'before' condition. The products are potentially changed in some way,
such as a cleaning step. The 'before' and 'after' measurements of a
characteristic are made with the same device, on the same  𝑛  units. Each
'before' measurement is paired with the corresponding 'after' measurement and
the differences are calculated.

A paired t test can be used for:

Is the average of the differences not equal to zero?
Is the average of the differences greater than zero?
Is the average of the differences less than zero?
Is the average of the differences not equal to some hypothesized average?
Is the average of the differences greater than some hypothesized average?
Is the average of the differences less than some hypothesized average?

For t tests in general:

- The data in a sample follow a normal distribution with mean mu and variance
sigma squared.
- The sample variance  s squared follows a chi-squared
distribution with rho degrees of freedom under the null hypothesis, where rho
is a positive constant.
- Ybar - mu and the sample standard deviation s are independent.
"""

from pathlib import Path
import time

import datasense as ds
import pandas as pd


def main():
    # filetypes = [("csv and feather files", ".csv .CSV .feather .FEATHER")]
    # path_in_title = "Select csv or feather file to read"
    # initialdir = Path(__file__).parent.resolve()
    header_title = "Paired-sample t test"
    # path_in = Path("paired_t_data.csv")
    output_url = "paired_sample_t.html"
    header_id = "paired-sample-t-test"
    significance_level = 0.05
    hypothesized_value = 4
    decimals = 3
    width = 7
    # path_in = ds.ask_open_file_name_path(
    #     title=path_in_title,
    #     initialdir=initialdir,
    #     filetypes=filetypes
    # )
    # hypothesized_value = float(input("Enter the hypothesized value:"))
    start_time = time.perf_counter()
    original_stdout = ds.html_begin(
        output_url=output_url,
        header_title=header_title,
        header_id=header_id
    )
    ds.script_summary(
        script_path=Path(__file__),
        action="started at"
    )
    ds.style_graph()
    series1 = pd.Series(
        data=[
            68, 76, 74, 71, 71, 72, 75, 83, 75, 74, 76, 77, 78, 75, 75, 84, 77,
            69, 75, 65
        ],
        name="before"
    )
    series2 = pd.Series(
        data=[
            67, 77, 74, 74, 69, 70, 71, 77, 71, 74, 73, 68, 71, 72, 77, 80, 74,
            73, 72, 62
        ],
        name="after"
    )
    series_differences = series1 - series2
    # series1 = pd.Series(
    #     data=[
    #         105, 81.4, 91.4, 84, 88.1, 91.4, 98, 90.2, 94.7, 105.5, 86.5, 83.1,
    #         86.2, 87.7, 84.7, 83.8, 86.8, 90.2, 92.4, 85.9, 84.8, 89.3, 91.7,
    #         87.7, 91.3, 90.7, 93.7, 90, 85, 87.9, 85.2, 87.4
    #     ],
    #     name="before"
    # )
    # series2 = pd.Series(
    #     data=[
    #         106.6, 83.3, 99.4, 94.7, 99.7, 94.1, 101.9, 98.6, 103.1, 106.2,
    #         92.3, 89.2, 93.6, 97.4, 88.8, 85.9, 96.5, 99.5, 99.8, 97, 95.3,
    #         100.2, 96.3, 93.9, 97.4, 98.4, 101.3, 99.1, 92.8, 95.7, 93.5, 97.5
    #     ],
    #     name="after"
    # )
    # series1 = pd.Series(
    #     data=[9.4, 10.6, 12.0, 8.7, 9.1, 7.0, 10.2, 11.3],
    #     name="pre"
    # )
    # series2 = pd.Series(
    #     data=[8.2, 7.2, 10.5, 10.3, 10.2, 8.5, 9.4, 8.7],
    #     name="post"
    # )
    # print("Data file", path_in)
    # print()
    # df = ds.read_file(file_name=path_in)
    # series1 = df[df.columns[0]].dropna()
    # series2 = df[df.columns[1]].dropna()
    # levels = ["before", "after"]
    # for level in levels:
    #     if level == "before":
    #         series = series1
    #     else:
    #         series = series2
    #     parametric_statistics = ds.parametric_summary(
    #         series=series,
    #         decimals=decimals
    #     ).to_string()
    #     print(f"Parametric statistics for y level {level}")
    #     print(parametric_statistics)
    #     print()
    # for level in levels:
    #     if level == "before":
    #         series = series1
    #     else:
    #         series = series2
    #     nonparametric_statistics = ds.nonparametric_summary(
    #         series=series,
    #         alphap=1/3,
    #         betap=1/3,
    #         decimals=decimals
    #     ).to_string()
    #     print(f"Non-parametric statistics for y level {level}")
    #     print(nonparametric_statistics)
    #     print()
    print("Scenario 1")
    print("Ho: The population average of the differences equals zero.")
    print("Ha: The population average of the differences does not equal zero.")
    print()
    result = ds.paired_t(
        series1=series1,
        series2=series2,
        hypothesized_value=0,
        alternative_hypothesis="two-sided",
        significance_level=significance_level,
        width=width,
        decimals=decimals
    )
    print(result)
    print()
    print("Scenario 2")
    print("Ho: The population average of the differences equals zero.")
    print("Ha: The population average of the differences is less than zero.")
    print()
    result = ds.paired_t(
        series1=series1,
        series2=series2,
        hypothesized_value=0,
        alternative_hypothesis="less",
        significance_level=significance_level,
        width=width,
        decimals=decimals
    )
    print(result)
    print()
    print("Scenario 3")
    print("Ho: The population average of the differences equals zero.")
    print(
        "Ha: The population average of the differences is greater than zero."
    )
    print()
    result = ds.paired_t(
        series1=series1,
        series2=series2,
        hypothesized_value=0,
        alternative_hypothesis="greater",
        significance_level=significance_level,
        width=width,
        decimals=decimals
    )
    print(result)
    print()
    print("Scenario 4")
    print("Ho: The population average of the differences equals d.")
    print("Ha: The population average of the differences does not equal d.")
    print()
    result = ds.paired_t(
        series1=series1,
        series2=series2,
        hypothesized_value=hypothesized_value,
        alternative_hypothesis="two-sided",
        significance_level=significance_level,
        width=width,
        decimals=decimals
    )
    print(result)
    print()
    print("Scenario 5")
    print("Ho: The population average of the differences equals d.")
    print("Ha: The population average of the differences is less than d.")
    print()
    result = ds.paired_t(
        series1=series1,
        series2=series2,
        hypothesized_value=hypothesized_value,
        alternative_hypothesis="less",
        significance_level=significance_level,
        width=width,
        decimals=decimals
    )
    print(result)
    print()
    print("Scenario 6")
    print("Ho: The population average of the differences equals d.")
    print("Ha: The population average of the differences is greater than d.")
    print()
    result = ds.paired_t(
        series1=series1,
        series2=series2,
        hypothesized_value=hypothesized_value,
        alternative_hypothesis="greater",
        significance_level=significance_level,
        width=width,
        decimals=decimals
    )
    print(result)
    print()
    fig, ax = ds.plot_histogram(series=series_differences)
    ax.set_xlabel("Y (units)")
    ax.set_ylabel("Count")
    ax.set_title(label="Histogram of series differences")
    fig.savefig(
        fname="histogram_series_differences.svg",
        format="svg"
    )
    ds.html_figure(
        file_name="histogram_series_differences.svg",
        caption="histogram_series_differences.svg"
    )
    # if t_test_pvalue < significance_level:
    #     print('Statistically significant. The test statistic =',
    #           t_test_statisic.round(3),
    #           '. The p value = ', t_test_pvalue.round(3)), '.'
    # else:
    #     print('Not statistically significant. The test statistic =',
    #           t_test_statisic.round(3),
    #           '. The p value = ', t_test_pvalue.round(3)), '.'
    # print(result)
    stop_time = time.perf_counter()
    ds.script_summary(
        script_path=Path(__file__),
        action="finished at"
    )
    ds.report_summary(
        start_time=start_time,
        stop_time=stop_time
    )
    ds.html_end(
        original_stdout=original_stdout,
        output_url=output_url
    )


if __name__ == "__main__":
    main()
