import pandera as pa
from pandera.typing import DataFrame, Series


class Example(pa.SchemaModel):
    counts: Series[int]
    values: Series[int]


def main():
    ex = DataFrame[Example]({"counts": [], "values": []})
    print(ex)

if __name__ == '__main__':
    main()
