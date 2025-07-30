'''
finger_exer_powers.py -- script that returns root & power based on integer entered
by user -- 1 < pwr < 6
'''
def get_root_and_power(exp: int):
    for guess in range(exp):
        for power in range(2, 6):
            if guess**power == exp:
                return [guess, power]
    print("No matches found")
    return None 



if __name__ == "__main__":
    print(get_root_and_power(6))
