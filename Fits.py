def FirstFit(block_Size, blocks, process_Size, proccesses):
    allocate = [-1] * proccesses
    occupied = [False] * blocks

    for i in range(proccesses):
        for j in range(blocks):
            if not occupied[j] and (block_Size[j] >= process_Size[i]):           
                allocate[i] = j
                occupied[j] = True
                break

    print("Process No. Process Size Block No.")

    for i in range(proccesses):
        print(str(i + 1) + "\t\t\t" + str(process_Size[i]) + "\t\t\t", end=" ")

        if allocate[i] != -1:
            print(allocate[i] + 1)
        else:
            print("Not Allocated")


def BestFit(block_sizes, num_blocks, process_sizes, num_processes):
    allocate = [-1] * num_processes
    occupied = [False] * num_blocks

    for i in range(num_processes):
        best_fit_index = -1
        for j in range(num_blocks):
            if not occupied[j] and block_sizes[j] >= process_sizes[i]:
                if best_fit_index == -1 or block_sizes[j] < block_sizes[best_fit_index]:
                    best_fit_index = j

        if best_fit_index != -1:
            allocate[i] = best_fit_index
            occupied[best_fit_index] = True

    print("Process No. Process Size Block No.")

    for i in range(num_processes):
        print(str(i + 1) + "\t\t\t" + str(process_sizes[i]) + "\t\t\t", end=" ")

        if allocate[i] != -1:
            print(allocate[i] + 1)
        else:
            print("Not Allocated")


def WorstFit(block_sizes, num_blocks, process_sizes, num_processes):
    allocate = [-1] * num_processes
    occupied = [False] * num_blocks

    for i in range(num_processes):
        worst_fit_index = -1
        for j in range(num_blocks):
            if not occupied[j] and block_sizes[j] >= process_sizes[i]:
                if worst_fit_index == -1 or block_sizes[j] > block_sizes[worst_fit_index]:
                    worst_fit_index = j

        if worst_fit_index != -1:
            allocate[i] = worst_fit_index
            occupied[worst_fit_index] = True

    print("Process No. Process Size Block No.")

    for i in range(num_processes):
        print(str(i + 1) + "\t\t\t" + str(process_sizes[i]) + "\t\t\t", end=" ")

        if allocate[i] != -1:
            print(allocate[i] + 1)
        else:
            print("Not Allocated")




#Variable & Driver:

block_Size = [100, 50, 30, 120, 35]
process_Size = [20, 60, 70, 40]
m = len(block_Size)
n = len(process_Size)

print("First Fit:")
FirstFit(block_Size, m, process_Size, n)
print('')
print("Best Fit:")
BestFit(block_Size, m, process_Size, n)
print('')
print("Worst Fit:")
WorstFit(block_Size, m, process_Size, n)



