

def run(distinct_chars=4):
    data = open('input.txt').read().strip()
    first_marker = None
    for start_idx in range(0, len(data) - distinct_chars):
        slice = data[start_idx:start_idx+distinct_chars]
        # print(f"Slice: {slice}")
        if len(set(c for c in slice)) == distinct_chars:
            pos = start_idx + distinct_chars
            print(f"Found marker after {pos} characters")
            return pos

    if first_marker is None:
        raise ValueError("marker not found")

# run()
run(14)
