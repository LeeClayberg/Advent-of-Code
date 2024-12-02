
# Read in stuff
with open("files/day02.txt", "r") as file_stream:
    lines = file_stream.readlines()
    reports = [[int(i) for i in line[:-1].split(" ")] for line in lines]

    total = 0
    for idx, static_report in enumerate(reports):
        for x in range(0, len(static_report)):
            report = static_report[:x] + static_report[x+1:]
            increasing = None
            failed = False
            dampener = True
            i = 1
            while i < len(report):
                a, b = report[i-1], report[i]
                if a == b:
                    failed = True
                    break
                if increasing is not None:
                    if a < b and not increasing:
                        failed = True
                        break
                    if a > b and increasing:
                        failed = True
                        break
                if abs(a - b) > 3:
                    failed = True
                    break
                increasing = a < b
                i += 1
            if not failed:
                total += 1
                break
    print(total)



