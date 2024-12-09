class Span:
    def __init__(self, index: int, sector: int, size: int):
        self.index = index
        self.sector = sector
        self.size = size


def checksum(file_spans: list[Span]) -> int:
    return sum(
        (span.sector + offset) * span.index
        for span in file_spans
        for offset in range(span.size)
    )


def parse_input_for_part1(data: str) -> tuple[list[Span], list[Span]]:
    current_sector = 0
    file_spans = []
    free_spans = []
    span_lists = [file_spans, free_spans]

    for char_index, char in enumerate(data):
        if char.isdigit():
            size = int(char)
            span_lists[char_index % 2].extend(
                [Span(index=char_index // 2, sector=current_sector + offset, size=1) for offset in range(size)])
            current_sector += size
    return file_spans, free_spans


def parse_input_for_part2(data: str) -> tuple[list[Span], list[Span]]:
    current_sector = 0
    file_spans = []
    free_spans = []
    span_lists = [file_spans, free_spans]

    for char_index, char in enumerate(data):
        if char.isdigit():
            size = int(char)
            span_lists[char_index % 2].append(Span(index=char_index // 2, sector=current_sector, size=size))
            current_sector += size
    return file_spans, free_spans


def part1(data: str) -> int:
    file_spans, free_spans = parse_input_for_part1(data)
    left_pointer = 0
    right_pointer = len(file_spans) - 1

    while left_pointer < len(free_spans) and free_spans[left_pointer].sector < file_spans[right_pointer].sector:
        for offset in range(free_spans[left_pointer].size):
            file_spans[right_pointer - offset].sector = free_spans[left_pointer].sector
        right_pointer -= free_spans[left_pointer].size
        left_pointer += 1

    return checksum(file_spans)


def part2(data: str) -> int:
    file_spans, free_spans = parse_input_for_part2(data)

    for file_span in reversed(file_spans):
        candidate_free_span = next(
            (free_span for free_span in free_spans if
             free_span.sector < file_span.sector and free_span.size >= file_span.size),
            None
        )
        if candidate_free_span:
            file_span.sector = candidate_free_span.sector
            candidate_free_span.sector += file_span.size
            candidate_free_span.size -= file_span.size

    return checksum(file_spans)


if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    disk_map = lines[0]

    print("Part 1:", part1(disk_map))
    print("Part 2:", part2(disk_map))
