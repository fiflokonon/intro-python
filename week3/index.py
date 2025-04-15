def calculate_discount(price, discount_percent):
    """
    Calculates the discounted price if discount_percent is 20 or more.
    Otherwise, returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

def main():
    print("Discount Calculator")

    try:
        price = float(input("Enter the original price: "))
        discount_percent = float(input("Enter the discount percentage: "))

        final_price = calculate_discount(price, discount_percent)

        if discount_percent >= 20:
            print(f"Discount applied! Final price: {final_price:.2f}")
        else:
            print(f"No discount applied. Price remains: {final_price:.2f}")
    except ValueError:
        print("Error: Please enter valid numerical values.")

if __name__ == "__main__":
    main()
