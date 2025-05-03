import random

def flip_coin():
    return random.choice(['Heads', 'Tails'])

def simulate_flips(num_flips):
    heads = tails = 0
    for _ in range(num_flips):
        result = flip_coin()
        if result == 'Heads':
            heads += 1
        else:
            tails += 1
    return heads, tails

def show_results(heads, tails):
    total = heads + tails
    print("\n--- Results ---")
    print(f"Heads: {heads} ({(heads/total)*100:.2f}%)")
    print(f"Tails: {tails} ({(tails/total)*100:.2f}%)")

def main():
    print("🪙 Welcome to the Virtual Coin Toss Simulator 🪙")
    while True:
        try:
            flips = int(input("Enter the number of times to flip the coin: "))
            if flips <= 0:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        heads, tails = simulate_flips(flips)
        show_results(heads, tails)

        again = input("\nDo you want to try again? (y/n): ").lower()
        if again != 'y':
            print("Thank you for using the Coin Toss Simulator!")
            break

if __name__ == "__main__":
    main()
