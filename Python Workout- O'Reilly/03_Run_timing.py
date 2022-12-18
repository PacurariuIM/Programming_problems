

def run_timing():
    number_runs = 0
    total_time = 0

    while True:
        one_run = input("Enter run duration: ")

        if not one_run:
            break

        number_runs += 1
        total_time += float(one_run)
        average_time = total_time / number_runs
        print(f"Average time {average_time} for {number_runs} of runs")


run_timing()