class SalesData:
    def __init__(self, sales):
        self.__sales = sales

    def get_sales(self):
        return self.__sales

    def set_sales(self, sales):
        self.__sales = sales


class SalesPredictor(SalesData):
    def __init__(self, sales, growth_rate):
        SalesData.__init__(self, sales)
        self.__growth_rate = growth_rate

    def get_growth_rate(self):
        return self.__growth_rate

    def set_growth_rate(self, growth_rate):
        self.__growth_rate = growth_rate

    def predict_sales(self, years):
        predicted_sales = self.get_sales()
        for i in range(years):
            predicted_sales *= (1 + self.__growth_rate)
        return predicted_sales


class LinearSalesPredictor(SalesPredictor):
    def __init__(self, sales, growth_rate):
        SalesPredictor.__init__(self, sales, growth_rate)

    def predict_sales(self, years):
        return self.get_sales() + (self.get_growth_rate() * years)


class ExponentialSalesPredictor(SalesPredictor):
    def __init__(self, sales, growth_rate):
        SalesPredictor.__init__(self, sales, growth_rate)

    def predict_sales(self, years):
        return self.get_sales() * (1 + self.get_growth_rate()) ** years


def main():
    # Create a LinearSalesPredictor object
    linear_predictor = LinearSalesPredictor(100, 0.1)
    print("Linear prediction:", linear_predictor.predict_sales(10))

    # Create an ExponentialSalesPredictor object
    exponential_predictor = ExponentialSalesPredictor(100, 0.1)
    print("Exponential prediction:", exponential_predictor.predict_sales(10))


if __name__ == "__main__":
    main()
