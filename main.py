import abc
import csv
from enum import Enum, auto
from pathlib import Path
from typing import Tuple, Optional, Dict, Iterator, Any


class Operation(Enum):
    CREATE = auto()
    UPDATE = auto()
    DELETE = auto()


class ProductStreamProcessor(metaclass=abc.ABCMeta):
    # Note the methods of this ProductStreamProcessor class should not be adjusted
    # as this is a hypothetical base class shared with other programs.

    def __init__(self, path_to_before_csv: str, path_to_after_csv: str):
        self.path_to_before_csv = path_to_before_csv
        self.path_to_after_csv = path_to_after_csv

    @abc.abstractmethod
    def main(self) -> Iterator[Tuple[Operation, str, Optional[Dict[str, Any]]]]:
        """
        Creates a stream of operations based for products in the form of tuples
        where the first element is the operation, the second element is the id
        for the product, and the third is a dictionary with all data for a
        product. The latter is None for DELETE operations.
        """
        ...


class ProductDiffer(ProductStreamProcessor):
    """
    Implement this class to create a simple product differ.
    """

    def main(self) -> Iterator[Tuple[Operation, str, Optional[Dict[str, Any]]]]:
        """
        Compare two CSV files and determine the CREATE, UPDATE, DELETE operations.
        """
        existing_products = self.load_csv(self.path_to_before_csv)
        products = self.load_csv(self.path_to_after_csv)

        # Determine the UPDATE and CREATE operations.
        for product_id, data in products.items():
            existing_product = existing_products.pop(product_id, None)
            operation_type = Operation.UPDATE if existing_product else Operation.CREATE
            yield operation_type, product_id, data

        # Determine the DELETE operations.
        for product_id, data in existing_products.items():
            yield Operation.DELETE, product_id, data

    @staticmethod
    def load_csv(path) -> Dict[str, Dict]:
        """
        Load CSV file into a dictionary with the product ID as key.
        :param path: The path of the CSV file.
        """
        with open(path) as f:
            reader = csv.DictReader(f)
            return {row.pop('id'): row for row in reader}


if __name__ == "__main__":
    path_to_before_csv = Path(__file__).parent / "product_inventory_before.csv"
    path_to_after_csv = Path(__file__).parent / "product_inventory_after.csv"

    for operation in ProductDiffer(path_to_before_csv, path_to_after_csv).main():
        print(operation)
