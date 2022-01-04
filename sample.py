import random
import sys
random.seed(100)

# for given txt files, generate samples
def main():
    filename = sys.argv[1]
    all_lines = open(filename).readlines()
    N = len(all_lines)
    sample_size = 95
    sample_idx = random.sample(list(range(N)), sample_size)
    for idx in sample_idx:
        print(all_lines[idx].strip())

if __name__ == '__main__':
    main()
