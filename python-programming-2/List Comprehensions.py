## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]
for i,row in enumerate(ships):
    print(row)
    print(cars[i])

## 3. Adding Columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]
for i,row in enumerate(things):
    row.append(trees[i])

## 4. List Comprehensions ##

apple_prices = [100, 101, 102, 105]
apple_prices_doubled = [2*row for row in apple_prices]
apple_prices_lowered = [row-100 for row in apple_prices]

## 5. Counting Female Names ##

name_counts = {}
for row in legislators:
    if row[3] == 'F' and row[7] > 1940:
        name = row[1]
        if name in name_counts:
            name_counts[name]+=1
        else:
            name_counts[name] = 1

## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = []
checks = [row is not None and row > 30 for row in values]

## 8. Highest Female Name Count ##

max_value = None
for row in name_counts:
    count = name_counts[row]
    if max_value is None or count > max_value:
        max_value = count

## 9. The Items Method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}
for row1, row2 in plant_types.items():
    print(row1)
    print(row2)

## 10. Finding the Most Common Female Names ##

top_female_names = []
for row in name_counts:
    if name_counts[row] == 2:
        top_female_names.append(row)