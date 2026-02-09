def who_are_you_and_hello():
    while True:
        s = input()
        ok = s.isalpha() and (
            (len(s) == 1 and s.isupper()) or
            (len(s) > 1 and s[0].isupper() and s[1:].islower())
        )
        if ok:
            print(f"Привет, {s}!")
            return
