import csv
import random

def pentasky(x, y, dens, boundaries=True):
    """Randomly creates tiles based on specified densities.

    Args:
        x: total number of tiles on x axis.
        y: total number of tiles on y axis.
        dens: dict of densities for each type type: {"rock": .1, etc}.

    Returns:
        results: list of result tiles.
    """
    empty_tile = "-"
    boundary = "X"
    if (sum(dens.values()) >= 1):
        raise Exception("ERROR: total densities >= 1; (sum = %s)" % sum(dens.values()))
    results = []
    rowed_results = []
    desired_amount = x * y
    keys = dens.keys()
    for key in keys:
        number_reps = int(dens[key] * desired_amount)
        for i in range(number_reps):
            results.append(key)
    current_amount = len(results)
    for unspecified_tile in range(desired_amount - current_amount):
        results.append(empty_tile)
    random.shuffle(results)
    if boundaries == True:
        for x_boundary_cell in range(x):
            results[x_boundary_cell] = boundary # Top
            results[-x_boundary_cell] = boundary # Bottom
        for y_boundary_cell in range(y):
            x_pad = x * y_boundary_cell
            results[x_pad] = boundary # Left side
            results[x_pad + x - 1] = boundary # Right side
    for i in range(y):
        row = []
        for j in range(x):
            index = i * y + j
            row.append(results[index])
        rowed_results.append(row)
    return rowed_results


def write_to_tsv(filename, data):
    """Writes data passed through args to tab separated file.

    Args:
        filename: name of file (example: 'forest_dat.csv')
        data: list of data you want inside file (example: ['stump', 'poop', 'burrito] )
    """
    with open(filename, 'w') as csvfile:
        tasker = csv.writer(csvfile, delimiter='\t', lineterminator = '\n')
        for row in data:
            tasker.writerow(row)

def main():
    x = 100
    y = 100
    d =  {'R':.01, 'T':.01, 'V':.01}

    results = pentasky(x, y, d)
    write_to_tsv('desert_entities.tsv', results)




if __name__ == "__main__":
    main()
