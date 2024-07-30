calls = 0 # global

def count_calls ():
    global calls
    calls = calls + 1

def string_info ( string ):
    count_calls()
    str_len = len(str( string ))
    upper_str = str( string ).upper()
    lower_str = str( string ).lower()
    cortesh = (str_len, upper_str, lower_str)
    return cortesh

def is_contains ( string, list_to_search ):
    count_calls()
    string = str(string).upper().lower()
    find_complit = False
    for search in list_to_search:
        if str(search).upper().lower().find(string) >= 0:
            find_complit = True
            break
    return find_complit

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)