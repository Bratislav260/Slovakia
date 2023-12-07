class Home:
    def new(n):
        try:
            a = int(n)
        except ValueError:
            print("ValueError")
