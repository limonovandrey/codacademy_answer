# Write your function below!
def fizz_count(x):
    count = 0
    for item in x:
        if item == "fizz":
            count = count + 1
    return count

lost = ["fizz","cat","fizz"]
small = fizz_count(lost)
print small
