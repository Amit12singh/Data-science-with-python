def check_discount(purchase_amount, is_member, has_coupon):
    if purchase_amount > 1000 and (is_member or has_coupon):
        return "Congratulations! You get a discount!"
    else:
        return "Sorry, you're not eligible for a discount."

def main():
    amount = float(input("enter total purchase amount:"))
    member_input = input("Are you a registered member? (yes/no):").lower()
    coupon_input = input("Do you have a discount coupon? (yes/no): ").lower()


    is_member = member_input == "yes"
    has_coupon = coupon_input =="yes"

    message = check_discount(amount, is_member, has_coupon)
    print(message)

if __name__ == "__main__":
    main()