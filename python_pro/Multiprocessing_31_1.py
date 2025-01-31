#multiprocess for multiplication
import multiprocessing

def multiply_by_two(number):
    print(f"{number} multiplied by 2 is {number * 2}")

if __name__ == "__main__":
    user_input = int(input("Enter a number to multiply all numbers from 1 to that number by 2: "))

    #Create and start a process for each number from 1 to user_input
    processes = []
    for number in range(1, user_input + 1):
        p = multiprocessing.Process(target=multiply_by_two, args=(number,))
        processes.append(p)
        p.start()

    #Wait for all processes to finish
    for p in processes:
        p.join()
    print("All processes have finished.")