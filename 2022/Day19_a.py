
blue_prints = dict()

with open("files/input_19.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        title, costs = line.split(":")
        blueprint_id = int(title.split(" ")[1])

        ore_robot, clay_robot, obsidian_robot, geode_robot = costs.split(". ")

        ore_parts = ore_robot.split(" ")
        ore_robot_cost = int(ore_parts[-2])

        clay_parts = clay_robot.split(" ")
        clay_robot_cost = int(clay_parts[-2])

        obsidian_parts = obsidian_robot.split(" ")
        obsidian_ore = int(obsidian_parts[4])
        obsidian_clay = int(obsidian_parts[7])

        geode_parts = geode_robot.split(" ")
        geode_ore = int(geode_parts[4])
        geode_obsidian = int(geode_parts[7])

        blue_prints[blueprint_id] = {
            'ore': {'ore': ore_robot_cost},
            'clay': {'ore': clay_robot_cost},
            'obsidian': {'ore': obsidian_ore, 'clay': obsidian_clay},
            'geode': {'ore': geode_ore, 'obsidian': geode_obsidian},
        }


def create_key(resources, robots, minute):
    res = ','.join([str(r) for r in resources.values()])
    rob = ','.join([str(r) for r in robots.values()])
    return f"{res}:{rob}:{minute}"


memo = dict()


def max_geodes(resources, robots, minute, r_costs):
    if minute == 24:
        # Return geodes
        return resources['geode']
    max_option = 0
    # create robot if able
    for robot, cost in r_costs.items():
        if all(cost[mat] <= resources[mat] for mat in cost.keys()):
            new_resources = {key: resources[key] - cost[key] if key in cost.keys() else resources[key] for key in resources.keys()}
            new_robots = robots.copy()
            new_robots[robot] += 1
            for rbt in robots.keys():
                new_resources[rbt] += robots[rbt]
            memo_key = create_key(new_resources, new_robots, minute+1)
            if memo_key in memo.keys():
                max_option = max(max_option, memo[memo_key])
            else:
                memo[memo_key] = max_geodes(new_resources, new_robots, minute+1, r_costs)
                max_option = max(max_option, memo[memo_key])
    # don't create robot
    new_resources_2 = resources.copy()
    for rbt in robots.keys():
        new_resources_2[rbt] += robots[rbt]
    memo_key = create_key(new_resources_2, robots, minute+1)
    if memo_key in memo.keys():
        max_option = max(max_option, memo[memo_key])
    else:
        memo[memo_key] = max_geodes(new_resources_2, robots, minute+1, r_costs)
    max_option = max(max_option, memo[memo_key])
    return max_option


total = 0
for b_id, costs in blue_prints.items():
    memo = dict()
    start_resources = {'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0}
    start_robots = {'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0}
    answer = max_geodes(start_resources, start_robots, 0, costs)
    print(answer)
    total += (answer * b_id)
print(total)
