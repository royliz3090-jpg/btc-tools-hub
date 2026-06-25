#!/usr/bin/env python3
"""Satoshi Converter - Convert between BTC, sats, and fiat"""
import sys

BTC_PRICE_USD = 60653  # Update as needed

def convert(value: float, from_unit: str) -> dict:
    conversions = {}
    
    if from_unit == "btc":
        conversions["sats"] = value * 100_000_000
        conversions["usd"] = value * BTC_PRICE_USD
    elif from_unit == "sats":
        conversions["btc"] = value / 100_000_000
        conversions["usd"] = (value / 100_000_000) * BTC_PRICE_USD
    elif from_unit == "usd":
        conversions["btc"] = value / BTC_PRICE_USD
        conversions["sats"] = (value / BTC_PRICE_USD) * 100_000_000
    
    conversions["from"] = f"{value} {from_unit.upper()}"
    conversions["btc_price_usd"] = BTC_PRICE_USD
    return conversions

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python sat_converter.py <value> <btc|sats|usd>")
        sys.exit(1)
    
    result = convert(float(sys.argv[1]), sys.argv[2])
    for k, v in result.items():
        if k == "sats":
            print(f"{k}: {v:,.0f}")
        elif k == "btc":
            print(f"{k}: {v:.8f}")
        elif k == "usd":
            print(f"{k}: ${v:,.2f}")
        else:
            print(f"{k}: {v}")
