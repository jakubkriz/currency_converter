# Currency Converter
- A program that converts a given amount from one currency to one or more output currencies.

## Prerequisites
- Python2.7

## Parameters
- --amount - amount which we want to convert - float, required
- --input_currency - input currency - 3 letters name or currency symbol, required
- --output_currency - requested/output currency - 3 letters name or currency symbol, optional
- if output currency is not specified, all known currencies are used instead

## Run Tests
```bash
python -m unittest discover
```

## Examples
```bash
python currency_converter.py --amount 100.00 --input_currency EUR --output_currency CZK
{
    "input": {
        "currency": "EUR",
        "amount": 100.0
    },
    "output": {
        "CZK": "2613.20"
    }
}
```

```bash
python currency_converter.py --amount 5.00 --input_currency € --output_currency $
{
    "input": {
        "currency": "EUR",
        "amount": 5.0
    },
    "output": {
        "USD": "5.68"
    }
}
```

```bash
python currency_converter.py --amount 5.00 --input_currency HRK
{{
    "input": {
        "currency": "HRK",
        "amount": 5.0
    },
    "output": {
        "EUR": "0.67",
        "USD": "0.77",
        "AUD": "1.01",
        "CHF": "0.74",
        "IDR": "10230.00",
        "KRW": "881.55",
        "BGN": "1.32",
        "CNY": "5.21",
        "TRY": "2.72",
        "ILS": "2.69",
        "GBP": "0.59",
        "NZD": "1.05",
        "THB": "26.03",
        "CAD": "0.99",
        "MXN": "13.94",
        "HUF": "207.85",
        "RON": "3.09",
        "NOK": "6.39",
        "RUB": "45.40",
        "ZAR": "10.12",
        "MYR": "3.29",
        "INR": "49.55",
        "DKK": "5.01",
        "JPY": "86.68",
        "CZK": "17.62",
        "BRL": "2.53",
        "PLN": "2.86",
        "PHP": "38.66",
        "SEK": "6.52",
        "SGD": "1.06",
        "HKD": "5.98"
    }
}
```