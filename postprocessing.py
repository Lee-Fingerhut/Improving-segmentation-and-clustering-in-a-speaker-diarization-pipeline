import argparse
import math
import numpy as np
import pandas as pd
# import seaborn as sns


def rint(x):
    return int(x // 1)


def sec_to_min(x: float):
    mils = rint(100 * (x % 1))
    secs = rint((x // 1) % 60)
    mins = rint(x // 60)
    return f"{str(mins).zfill(2)}:{str(secs).zfill(2)}:{str(mils).zfill(2)}"


def dec4(x: float):
    return "{:.4f}".format(x)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--in-rttm-dir', required=True, type=str, help='input directory with rttm files')
    parser.add_argument('--out-csv-dir', required=True, type=str, help='Directory to store output csv files')
    parser.add_argument('--out-xlsx-dir', required=True, type=str, help='Directory to store output xlsx files')
    args = parser.parse_args()

    df = pd.read_csv(args.in_rttm_dir,
                     delimiter=" ",
                     names=["sp", "file name", "1", "start time (sec)", "duration", "na1", "na2", "speaker", "na3",
                            "na4"]
                     )


    # df = pd.read_csv('/Users/lee/Documents/VBx-Version1/VBx/exp/odkzj.rttm',
    #                  delimiter=" ",
    #                  names=["sp", "file name", "1", "start time (sec)", "duration", "na1", "na2", "speaker", "na3",
    #                         "na4"]
    #                  )
    df = df.drop(['sp', 'file name', '1', 'na1', 'na2', 'na3', 'na4'], axis=1)
    df["end time (sec)"] = df["start time (sec)"] + df["duration"]

    df["start time (min)"] = df["start time (sec)"].map(sec_to_min)
    df["end time (min)"] = df["end time (sec)"].map(sec_to_min)

    df["end time (sec)"] = df["end time (sec)"].map(dec4)

    df = df[['start time (sec)', 'end time (sec)', 'start time (min)', 'end time (min)', 'speaker']]
    # df.to_csv('/Users/lee/Documents/VBx-Version1/VBx/exp/odkzj.csv')
    df.to_csv(args.out_csv_dir)

    df = df.drop(['start time (sec)', 'end time (sec)'], axis=1)

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    # writer = pd.ExcelWriter('/Users/lee/Documents/VBx-Version1/VBx/exp/odkzj.xlsx', engine='xlsxwriter')
    writer = pd.ExcelWriter(args.out_xlsx_dir, engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Sheet1')

    # Get the xlsxwriter workbook and worksheet objects.
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    # Add a format. Light red fill with dark red text.
    format1 = workbook.add_format({'bg_color': '#FFC7CE',
                                   'font_color': '#9C0006'})

    # Set the conditional format range.
    start_row = 1
    start_col = 3
    end_row = len(df)
    end_cold = 6

    # Apply a conditional format to the cell range.
    worksheet.conditional_format(start_row, start_col, end_row, end_cold,
                                 {'type': '3_color_scale',
                                  # 'criteria': '>',
                                  # 'value': 20,
                                  'format': format1})

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
    # df.to_excel('/Users/lee/Documents/VBx-Version1/VBx/exp/asxwr.xlsx')



