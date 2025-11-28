import pandas as pd


def apply_scheme(
    filelin,
    num_stu,
    num_HWs,
    HW_tot,
    mid_tot,
    fin_tot,
    scheme1={"HW": 35, "Midterm": 30, "Final": 35},
    scheme2={"HW": 35, "Midterm": 0, "Final": 65},
):

    cols_to_skip = ["Status", "ID", "SIS Login ID", "Section"]
    rows_to_skip = [1, 2, num_stu + 3]
    dtype_dict = {"SIS User ID": int, "Student": str}
    na_values_list = ["", " ", "  "]

    grades = pd.read_csv(
        filelin,
        header=0,
        index_col="Student",
        na_values=na_values_list,
        usecols=lambda col: col not in cols_to_skip,
        dtype=dtype_dict,
        skiprows=rows_to_skip,
    ).fillna(0)

    grades.rename(columns={"SIS User ID": "UID"}, inplace=True)

    HW_index_offset = num_HWs + 1

    grades.iloc[:, 1:HW_index_offset] /= HW_tot
    HWA = grades.iloc[:, 1:HW_index_offset].sum(axis=1) / 8
    grades.insert(loc=HW_index_offset, column="HWA", value=HWA)

    HW_slice = grades.iloc[:, 1:HW_index_offset]
    adjusted_HWA = (HW_slice.sum(axis=1) - HW_slice.min(axis=1) / 2) / (num_HWs - 0.5)
    grades.insert(loc=HW_index_offset + 1, column="adjusted HWA", value=adjusted_HWA)

    grades["Midterm"] /= mid_tot
    grades["Final"] /= fin_tot

    grades.iloc[:, 1:] *= 100

    grades["Scheme 1"] = (
        (grades["adjusted HWA"] * scheme1["HW"])
        + (grades["Midterm"] * scheme1["Midterm"])
        + (grades["Final"] * scheme1["Final"])
    ) / 100

    grades["Scheme 2"] = (
        (grades["adjusted HWA"] * scheme2["HW"])
        + (grades["Midterm"] * scheme2["Midterm"])
        + (grades["Final"] * scheme2["Final"])
    ) / 100

    grades["Best"] = grades.iloc[:, -2:].max(axis=1)

    return grades.sort_values(by=["Best"], ascending=False)
