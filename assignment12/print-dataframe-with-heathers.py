#Task 5
import pandas as pd

class DFPlus(pd.DataFrame):
    @property
    def _constructor(self):
        return DFPlus

    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)

    def print_with_headers(self):
        rows_per_page = 10
        total_rows = len(self)
        for start in range(0, total_rows, rows_per_page):
            end = start + rows_per_page
            print(self.iloc[start:end])
            print("-" * 40)  # Just a separator between chunks


# Usage
if __name__ == "__main__":
    dfp = DFPlus.from_csv("../csv/products.csv")
    dfp.print_with_headers()