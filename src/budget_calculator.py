def calculate_budget(crew_fee, equipment_fee, other_costs, production_fee_rate=0.15, tax_rate=0.06):
    subtotal = crew_fee + equipment_fee + other_costs
    production_fee = subtotal * production_fee_rate
    tax = (subtotal + production_fee) * tax_rate
    total = subtotal + production_fee + tax
    return {
        "subtotal": round(subtotal, 2),
        "production_fee": round(production_fee, 2),
        "tax": round(tax, 2),
        "total": round(total, 2)
    }

if __name__ == "__main__":
    result = calculate_budget(7000, 3000, 2000)
    print(result)
