import numpy as np

class Array:

    def stack_it(self):
        to_stack  = np.array(self.values)
        if not np.array_equal(to_stack, self.pile[-1]):
            self.pile = np.vstack((self.pile, np.array(self.values)))
            
    def __init__(self, values, lower_index=0):
        self.lower_index = lower_index
        self.values = list(values)
        
        self.pile = np.array(self.values)
        Array.full_array = list(values)

    def swap(self, index1, index2):
        self.values[index2], self.values[index1] = self.values[index1], self.values[index2]
        Array.full_array[self.lower_index + index2], Array.full_array[self.lower_index + index1] = Array.full_array[self.lower_index + index1], Array.full_array[self.lower_index + index2]
        self.stack_it()

    def get_len(self):
        return len(self.values)

def bubble_sort(nums):  # n^2
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(nums.get_len() - 1):
            if nums.values[i] > nums.values[i + 1]:
                # Swap the elements
                nums.swap(i, i + 1)
                # Set the flag to True so we'll loop again
                swapped = True

# A function to sort the given list using Gnome sort
def gnome_sort(nums):
    idx = 0
    while idx < nums.get_len():
        if idx == 0 or nums.values[idx] > nums.values[idx-1]:
            idx += 1
        else:
            nums.swap(idx, idx-1)
            idx -= 1