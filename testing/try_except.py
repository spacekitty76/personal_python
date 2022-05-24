def test(item="stuff"):
    number = 5
    tries = 0
    while tries < number:
        try:
            if item == "stuff":
                return "done"
        except:
            print("exception")
            tries += 1
        else:
            print("else")
            tries += 1
        finally:
            print(f"item result: {item}")

# print(test(item="mate"))
print(test(item="stuff"))