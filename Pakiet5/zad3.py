global_variable = 10

def function_with_global_variable():
    global global_variable
    global_variable += 1
    print("Wartość zmiennej globalnej wewnątrz funkcji:", global_variable)

def function_with_local_variable():
    local_variable = 5
    print("Wartość zmiennej lokalnej:", local_variable)

function_with_global_variable()
function_with_local_variable()

print("Wartość zmiennej globalnej po wywołaniu funkcji:", global_variable)


