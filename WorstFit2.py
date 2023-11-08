def WorstFit(block_sizes, num_blocks, process_sizes, num_processes):
    allocate = [-1] * num_processes

    for i in range(num_processes):
        worst_fit_index = -1
        for j in range(num_blocks):
            if block_sizes[j] >= process_sizes[i]:
                if worst_fit_index == -1 or block_sizes[j] > block_sizes[worst_fit_index]:
                    worst_fit_index = j

        if worst_fit_index != -1:
            allocate[i] = worst_fit_index
            block_sizes[worst_fit_index] -= process_sizes[i]

    print("Process No. Process Size Block No.")

    for i in range(num_processes):
        print(f"{i + 1}\t\t\t{process_sizes[i]}\t\t\t", end=" ")

        if allocate[i] != -1:
            print(f"{allocate[i] + 1}")
        else:
            print("Not Allocated")

# Variable & Driver:
block_Sizeoriginal = [100, 50, 30, 120, 35]
block_Size = [100, 50, 30, 120, 35]
process_Size = [20, 60, 70, 40]
m = len(block_Size)
n = len(process_Size)

print("Worst Fit Variant:")
WorstFit(block_Size, m, process_Size, n)