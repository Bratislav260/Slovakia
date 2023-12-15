class Home:
    def new(n):
        try:
            a = int(n)
            print("Это текст")
        except ValueError:
            print("ValueError")
