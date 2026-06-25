#!/usr/bin/env python3
"""Lightning Address Validator - Validate LUD-16 Lightning Addresses"""
import re
import sys

def validate_lightning_address(addr: str) -> dict:
    """Validate a Lightning Address (LUD-16)."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(pattern, addr):
        return {"valid": False, "error": "Invalid format"}
    
    user, domain = addr.split("@", 1)
    
    return {
        "valid": True,
        "user": user,
        "domain": domain,
        "lnurl": f"https://{domain}/.well-known/lnurlp/{user}",
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ln_address_validator.py <lightning_address>")
        sys.exit(1)
    
    result = validate_lightning_address(sys.argv[1])
    for k, v in result.items():
        print(f"{k}: {v}")
