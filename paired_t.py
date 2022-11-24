#! /usr/bin/env python3
"""
“Paired” means that there is a one-to-one correspondence between the values in
two samples. If  𝑥1,𝑥2,...,𝑥𝑛  and  𝑦1,𝑦2,...,𝑌𝑛  are two samples, then 𝑥𝑖
corresponds to  𝑦𝑖 .

Example. A sample of a product is taken from a process. Measurements are made
of the “before” condition. The products are potentially changed in some way,
such as a cleaning step. The “before” and “after” measurements of a
characteristic are made with the same device, on the same  𝑛  units. Each
“before” measurement is paired with the corresponding “after” measurement and
the differences are calculated.

A paired t test can be used for:

Is the average of the differences not equal to zero?
Is the average of the differences greater than zero?
Is the average of the differences less than zero?
Is the average of the differences not equal to some hypothesized average?
Is the average of the differences greater than some hypothesized average?
Is the average of the differences less than some hypothesized average?

For t tests in general:

The data in a sample follow a normal distribution mean  𝜇  and variance  𝜎2 .
The sample variance  𝑠2  follows a  𝜒2  distribution with  𝜌  degrees of
freedom under the null hypothesis, where  𝜌  is a positive constant.
(𝑌⎯⎯⎯⎯−𝜇)  and the sample standard deviations  𝑠  are independent.
"""

from pathlib import Path
import time

import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy.stats as stats
import datasense as ds
import pandas as pd
import numpy as np



def main():
    filetypes = [("csv and feather files", ".csv .CSV .feather .FEATHER")]
    path_in_title = "Select csv or feather file to read"
    initialdir = Path(__file__).parent.resolve()
    header_title = "Paired-sample t test"
    # path_in = Path("paired_t_data.csv")
    output_url = "paired_sample_t.html"
    header_id = "paired-sample-t-test"
    hypothesized_value = 4
    significance_level = 0.05
    colour = "#0077bb"
    decimals = 3
    width = 7
    # path_in = ds.ask_open_file_name_path(
    #     title=path_in_title,
    #     initialdir=initialdir,
    #     filetypes=filetypes
    # )
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
        significance_level=significance_level,
        alternative_hypothesis="two-sided",
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
        significance_level=significance_level,
        alternative_hypothesis="less",
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
        significance_level=significance_level,
        alternative_hypothesis="greater",
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
        significance_level=significance_level,
        alternative_hypothesis="two-sided",
        hypothesized_value=hypothesized_value,
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
        significance_level=significance_level,
        alternative_hypothesis="less",
        hypothesized_value=hypothesized_value,
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
        significance_level=significance_level,
        alternative_hypothesis="greater",
        hypothesized_value=hypothesized_value,
        width=width,
        decimals=decimals
    )
    print(result)
    print()
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
