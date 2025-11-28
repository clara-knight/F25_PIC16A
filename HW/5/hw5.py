import numpy as np


def clean_data(data):
    cleaned_data = data.copy()

    units_sold = cleaned_data[:, 1]
    unit_price = cleaned_data[:, 2]
    discount_rate = cleaned_data[:, 3]

    units_mask = units_sold != -1
    price_mask = unit_price > 0
    discount_mask = discount_rate < 1

    median_units = np.median(cleaned_data[units_mask, 1])
    mean_prices = np.mean(cleaned_data[price_mask, 2])
    mean_discount = np.mean(cleaned_data[discount_mask, 3])

    cleaned_data[~units_mask, 1] = median_units
    cleaned_data[~price_mask, 2] = mean_prices
    cleaned_data[~discount_mask, 3] = mean_discount

    return cleaned_data


def filter_high_value(data, min_total=100):

    units_sold = data[:, 1]
    unit_price = data[:, 2]
    discount_rate = 1 - data[:, 3]

    revenue_mask = (units_sold * unit_price * discount_rate) >= min_total

    return data[revenue_mask, :]


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


def adjust_prices(data):
    adjusted_data = data.copy()

    prices = adjusted_data[:, 2]
    discount_rate = adjusted_data[:, 3]
    regions = adjusted_data[:, 4]

    region_mask = regions <= 1
    discount_mask = discount_rate > 0.2

    prices[region_mask] *= 1.05
    prices[discount_mask] *= 0.9

    return adjusted_data


class GradeSystem:

    def __init__(self, hw, exam, hw_weight, exam_weights):
        if sum(exam_weights) + hw_weight != 1:
            raise ValueError("The sum of weights should be 1")
        if exam.shape[1] != exam_weights.shape[0]:
            raise ValueError(
                "The number of exams and the number of weights do not match"
            )
        else:
            self.hw = hw
            self.exam = exam
            self.hw_weight = hw_weight
            self.exam_weights = exam_weights

    def hw_average_drop_lowest(self):
        sorted_hw = np.sort(self.hw, axis=1)[:, 1:]
        return np.mean(sorted_hw, axis=1)

    def total_score(self):
        homework_points = self.hw_average_drop_lowest() * self.hw_weight
        exam_points = np.sum(self.exam * self.exam_weights, axis=1)
        total_points = exam_points + homework_points
        return total_points

    def letter_grade(self):
        grades = self.total_score()
        grading_scheme = [
            grades >= 90,
            grades >= 80,
            grades >= 70,
            grades >= 60,
            grades < 60,
        ]
        letters = ["A", "B", "C", "D", "F"]
        return np.select(grading_scheme, letters)
