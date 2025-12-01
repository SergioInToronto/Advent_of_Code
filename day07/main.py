import re


FILE_ENTRY = re.compile('(\d+) ([a-z\.]+)')


lines = open('input.txt').read().strip().split('\n')

# filesystem = {
#     "total_size": None,
#     "files": [],
#     "directories": [],
# }
sizes = {'/': None}
current_path = ['']


def pushd(dir_name):
    current_path.append(dir_name)


def popd():
    current_path.pop()


def record_dir(dir_name):
    path = '/'.join([*current_path, dir_name, ''])
    sizes[path] = None


def record_file(file_name):
    size, file_name = match.groups()
    path = '/'.join([*current_path, file_name])
    sizes[path] = int(size)


for line in lines:
    # match line:
    #     case 'cd /' | 'ls':
    #         pass
    #     case 
    #     case _:
    #         raise ValueError(f"Unhandled line: {line}")
    if line in ('$ cd /', '$ ls'):
        continue
    elif line == '$ cd ..':
        popd()
    elif line.startswith('$ cd '):
        _, _, dir_name = line.split(" ");
        pushd(dir_name)
    elif line.startswith('dir '):
        _, dir_name = line.split()
        record_dir(dir_name)
    elif match := re.match(FILE_ENTRY, line):
        record_file(match)
    else:
        raise ValueError(f"Could not handle: {line}")

print("All Loaded!")
# print(sizes)

# fill-in sizes for directories
# This could be more effecient if I went deepest-first to last. But this is faster to build.
for dir_path in (k for k in sizes.keys() if k.endswith('/')):
    total = 0
    for path, size in sizes.items():
        if path.startswith(dir_path) and not path.endswith('/'): # files in directory or subdirectories
            total += size
    assert sizes[dir_path] is None
    print(f"Size of {dir_path} is {total}")
    sizes[dir_path] = total

print("Finished computing directory sizes")

directories = {k:v for (k, v) in sizes.items() if k.endswith('/')}
print(f"Directories: {len(directories)}")
small_directory_sizes = [v for v in directories.values() if v < 100_000]
print(f"Small directories: {len(small_directory_sizes)}")
print(f"Sum of small directory sizes: {sum(small_directory_sizes)}")

# Part 2

total_space = 70_000_000
space_needed_for_update = 30_000_000
current_free_space = total_space - sizes['/']
additional_free_space_needed = space_needed_for_update - current_free_space
print(f"/ has size: {sizes['/']}")
print(f"Additional free space needed: {additional_free_space_needed}")

delete_candidates = list(directories.values())
delete_candidates.sort()
print(f"Sorted sizes: {delete_candidates}")
dir_size_to_delete = next(v for v in delete_candidates if v >= additional_free_space_needed)
print(f"We should delete the directory of size {dir_size_to_delete}")