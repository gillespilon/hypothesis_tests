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

import matplotlib.pyplot as plt
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
    # series1 = pd.Series(
    #     data=[
    #         105, 81.4, 91.4, 84, 88.1, 91.4, 98, 90.2, 94.7, 105.5, 86.5,
    #         83.1, 86.2, 87.7, 84.7, 83.8, 86.8, 90.2, 92.4, 85.9, 84.8,
    #         89.3, 91.7, 87.7, 91.3, 90.7, 93.7, 90, 85, 87.9, 85.2, 87.4
    #     ],
    #     name="before"
    # )
    # series2 = pd.Series(
    #     data=[
    #         106.6, 83.3, 99.4, 94.7, 99.7, 94.1, 101.9, 98.6, 103.1, 106.2,
    #         92.3, 89.2, 93.6, 97.4, 88.8, 85.9, 96.5, 99.5, 99.8, 97, 95.3,
    #         100.2, 96.3, 93.9, 97.4, 98.4, 101.3, 99.1, 92.8, 95.7, 93.5,
    #         97.5
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
    # series1 = df[df.columns[0]].notna().all(axis="coluns")
    # series2 = df[df.columns[1]].notna().all(axis="coluns")
    # series1 = pd.Series(
    #     data=[
    #         34.1, 32.3, 36.5, 38.6, 39.6, 31.8, 31.0, 38.8, 29.3, 35.3,
    #         41.3, 43.3, 33.8, 28.3, 36.8, 30.6, 28.8, 40.4, 39.8, 44.8,
    #         30.8, 25.8, 32.7, 35.3, 37.9
    #     ],
    #     name="before"
    # )
    # series2 = pd.Series(
    #     data=[
    #         47.9, 44.6, 47.3, 50.6, 51.9, 43.3, 43.3, 51.9, 41.2, 47.6,
    #         54.0, 55.6, 45.6, 39.4, 48.9, 42.4, 46.3, 52.8, 48.9, 56.7,
    #         46.5, 38.7, 44.2, 47.2, 51.0
    #     ],
    #     name="after"
    # )
    # series1 = pd.Series(
    #     data=[
    #         4.61, 6.42, 5.40, 4.54, 3.98, 3.82, 5.01, 4.34, 3.80, 4.56,
    #         5.35, 3.89, 2.25, 4.24
    #     ],
    #     name="cornflakes"
    # )
    # series2 = pd.Series(
    #     data=[
    #         3.84, 5.57, 5.85, 4.80, 3.68, 2.96, 4.41, 3.72, 3.49, 3.84,
    #         5.26, 3.73, 1.84, 4.14
    #     ],
    #     name="oatbran"
    # )
    # series1 = pd.Series(
    #     data=[16.3, 4.8, 10.9, 14.2, 16.3, 9.9, 29.2, 22.4],
    #     name="control"
    # )
    # series2 = pd.Series(
    #     data=[11.5, 3.6, 12.5, 6.3, 15.2, 8.1, 16.6, 13.1],
    #     name="regenerating"
    # )
    # series1 = pd.Series(
    #     data=[1902, 1470, 382, 778, 423, 568, 1375, 682],
    #     name="males"
    # )
    # series2 = pd.Series(
    #     data=[221, 633, 200, 312, 629, 435, 2098, 283],
    #     name="females"
    # )
    # series1 = pd.Series(
    #     data=[7.3, 9.6, 10.7, 10.9, 9.7, 8.5, 8.6, 8.6, 8.0, 7.2, 6.3],
    #     name="australia"
    # )
    # series2 = pd.Series(
    #     data=[6.9, 8.8, 10.1, 10.5, 9.7, 8.7, 8.2, 7.0, 6.4, 6.0, 5.5],
    #     name="uk"
    # )
    series_differences = series1 - series2
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
    fig, (ax1, ax2) = plt.subplots(
        nrows=2,
        ncols=1,
        sharex=True,
        sharey=True
    )
    mid = (fig.subplotpars.right + fig.subplotpars.left) / 2
    fig.suptitle(t="Histograms", x=mid)
    # ax1.hist(x=series1, bins=16)
    ax1.hist(x=series1)
    ax1.set_title(label="Series one")
    ax1.set_ylabel("Count")
    # ax2.hist(x=series2, bins=16)
    ax2.hist(x=series2)
    ax2.set_title(label="Series two")
    ax2.set_xlabel("Y (units)")
    ax2.set_ylabel("Count")
    ds.despine(ax=ax1)
    ds.despine(ax=ax2)
    fig.savefig(
        fname="histograms_series_one_series_two.svg",
        format="svg"
    )
    ds.html_figure(
        file_name="histograms_series_one_series_two.svg",
        caption="histograms_series_one_series_two.svg"
    )
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
    fig, (ax1, ax2) = plt.subplots(
        nrows=1,
        ncols=2,
        sharey=True
    )
    ax1.boxplot(
        x=series1,
        notch=True,
        showmeans=True
    )
    ax2.boxplot(
        x=series2,
        notch=True,
        showmeans=True
    )
    ax1.set_xticks(
        ticks=[1],
        labels=["Series one"]
    )
    ax2.set_xticks(
        ticks=[1],
        labels=["Series two"]
    )
    ax1.set_title(label="Series one")
    ax2.set_title(label="Series two")
    ax1.set_ylabel("Y (units)")
    mid = (fig.subplotpars.right + fig.subplotpars.left) / 2
    fig.suptitle(
        t="Box-and-whisker plots",
        x=mid
    )
    ds.despine(ax=ax1)
    ds.despine(ax=ax2)
    fig.savefig(
        fname="box_and_whiskers_series_one_series_two.svg",
        format="svg"
    )
    ds.html_figure(
        file_name="box_and_whiskers_series_one_series_two.svg",
        caption="box_and_whiskers_series_one_series_two.svg"
    )
    fig, ax = ds.plot_scatter_y(y=series1)
    ax.set_title(label="Scatter plot\nSeries one")
    ax.set_xlabel("X (Sample order)")
    ax.set_ylabel("Y (units)")
    fig.savefig(
        fname="scatter_series_one.svg",
        format="svg"
    )
    ds.html_figure(
        file_name="scatter_series_one.svg",
        caption="scatter_series_one.svg"
    )
    fig, ax = ds.plot_scatter_y(y=series2)
    ax.set_title(label="Scatter plot\nSeries two")
    ax.set_xlabel("X (Sample order)")
    ax.set_ylabel("Y (units)")
    fig.savefig(
        fname="scatter_series_two.svg",
        format="svg"
    )
    ds.html_figure(
        file_name="scatter_series_two.svg",
        caption="scatter_series_two.svg"
    )
    fig, ax = ds.plot_scatter_y(y=series_differences)
    ax.set_title(label="Scatter plot\nSeries differences")
    ax.set_xlabel("X (Sample order)")
    ax.set_ylabel("Y (units)")
    fig.savefig(
        fname="scatter_series_differences.svg",
        format="svg"
    )
    ds.html_figure(
        file_name="scatter_series_differences.svg",
        caption="scatter_series_differences.svg"
    )
    fig, ax = ds.probability_plot(data=series_differences)
    ax.set_title(label="Probability plot of series differences")
    fig.savefig(
        fname="probability_plot_series_differences.svg",
        format="svg"
    )
    ds.html_figure(
        file_name="probability_plot_series_differences.svg",
        caption="probability_plot_series_differences.svg"
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
