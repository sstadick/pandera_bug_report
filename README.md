# pandera_bug_report

https://github.com/unionai-oss/pandera/issues/922

To reproduce:

```bash
poetry install
poetry run python main.py
...
pandera.errors.SchemaError: expected series 'counts' to have type int64, got float64
```

Expected behavior:

pandera should allow an empty list in this context an not assume an implicity type.

