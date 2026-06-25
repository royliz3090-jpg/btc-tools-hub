#!/usr/bin/env python3
"""Lightning Invoice Decoder - Decode BOLT11 invoices"""
import sys
import hashlib
import bech32

def decode_bolt11(invoice: str) -> dict:
    """Decode a BOLT11 Lightning invoice."""
    if invoice.lower().startswith("ln"):
        # Remove prefix
        hrp = "ln"
        data_part = invoice[2:]
        
        # Find the separator
        for i, c in enumerate(data_part):
            if c.isdigit():
                continue
            elif c.isalpha():
                # This is part of the amount/unit
                hrp += c
            else:
                break
        
        # Simple decode for display
        return {
            "type": "BOLT11",
            "prefix": hrp,
            "length": len(invoice),
            "raw": invoice[:50] + "..." + invoice[-20:],
        }
    return {"type": "unknown"}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python bolt11_decoder.py <lightning_invoice>")
        sys.exit(1)
    
    result = decode_bolt11(sys.argv[1])
    for k, v in result.items():
        print(f"{k}: {v}")
