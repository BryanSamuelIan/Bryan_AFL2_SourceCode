def FirstFit(block_Size, m, process_Size, n):
    # code to store the block id of the block that needs to be allocated to a process
    allocate = [-1] * n

    # Any process is assigned with the memory at the initial stage

    # find a suitable block for each process
    # the blocks are allocated as per their size

    for i in range(n):
        for j in range(m):
            if block_Size[j] >= process_Size[i]:
                # assign the block j to p[i] process
                allocate[i] = j

                # available block memory is reduced
                block_Size[j] -= process_Size[i]
                break

    print("Process No. Process Size Block No.")

    for i in range(n):
        print(str(i + 1) + "\t\t\t" + str(process_Size[i]) + "\t\t\t", end=" ")

        if allocate[i] != -1:
            print(allocate[i] + 1)
        else:
            print("Not Allocated")


# Driver code
block_Sizeoriginal = [100, 50, 30, 120, 35]
block_Size = [100, 50, 30, 120, 35]
process_Size = [20, 60, 70, 40]
m = len(block_Size)
n = len(process_Size)

print("First Fit Variant:")
FirstFit(block_Size, m, process_Size, n)   