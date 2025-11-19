import numpy as np

np.set_printoptions(precision=2, suppress=True)

#   0: product id
#   1: units sold
#   2: unit price
#   3: discount rate
#   4: region code

data = np.array(
    [
        [101, 5, 10.0, 0.1, 0],
        [102, -1, 12.5, 0.2, 1],
        [103, 8, 0.0, 0.15, 2],
        [104, 10, 9.8, 1.2, 1],
        [105, 6, 11.2, 0.05, 0],
        [106, 3, 10.5, 0.0, 4],
        [107, 4, 8.8, 0.25, 3],
        [108, 7, 0.0, 0.10, 2],
        [109, 9, 13.5, 0.3, 4],
    ]
)


# 1
def clean_data(data):
    cleaned_data = data.copy()

    units_mask = cleaned_data[:, 1] != -1
    price_mask = cleaned_data[:, 2] > 0
    discount_mask = cleaned_data[:, 3] < 1

    median_units = np.median(cleaned_data[units_mask, 1])
    mean_prices = np.mean(cleaned_data[price_mask, 2])
    mean_discount = np.mean(cleaned_data[discount_mask, 3])

    cleaned_data[~units_mask, 1] = median_units
    cleaned_data[~price_mask, 2] = mean_prices
    cleaned_data[~discount_mask, 3] = mean_discount

    return cleaned_data


cleaned = clean_data(data)


# 2
def filter_high_value(data, min_total=100):

    units_sold = data[:, 1]
    unit_price = data[:, 2]
    discount_rate = 1 - data[:, 3]

    revenue_mask = (units_sold * unit_price * discount_rate) >= min_total

    return data[revenue_mask, :]


# 3
def region_summary(data):
    units_sold = data[:, 1]
    unit_price = data[:, 2]
    discount_rate = data[:, 3]
    regions = data[:, 4]

    unique_regions = np.unique(regions)
    region_mask = regions == unique_regions[:, np.newaxis]

    sales_pr = np.sum(region_mask, axis=1)
    discount_pr = np.sum(discount_rate * region_mask, axis=1) / sales_pr
    revenue_pr = np.sum(units_sold * unit_price * discount_rate * region_mask, axis=1)
    vals = np.array([revenue_pr, discount_pr, sales_pr])

    return dict(zip(unique_regions, zip(*vals)))


summary = region_summary(cleaned)

# 4
