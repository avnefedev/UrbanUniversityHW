calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(val):
    count_calls()
    return {len(val), val.upper(), val.lower()}

def is_contains(val, dict_val):
    count_calls()
    for i in dict_val:
        if val.lower() == i.lower():
            return True
        else:
            continue
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
