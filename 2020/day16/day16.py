import copy


def part1(properties, nearby_tickets):
    ticket_scanning_error_rate = 0

    for ticket in nearby_tickets:
        for value in ticket:
            invalid = True
            for ticket_prop in properties.values():
                if ticket_prop[0] <= value <= ticket_prop[1] or ticket_prop[2] <= value <= ticket_prop[3]:
                    invalid = False
            if invalid:
                ticket_scanning_error_rate += value

    print('Part 1:', ticket_scanning_error_rate)


def part2(properties, my_ticket, nearby_tickets):
    for ticket in copy.deepcopy(nearby_tickets):
        for value in ticket:
            invalid = True
            for ticket_prop in properties.values():
                if ticket_prop[0] <= value <= ticket_prop[1] or ticket_prop[2] <= value <= ticket_prop[3]:
                    invalid = False
            if invalid:
                nearby_tickets.remove(ticket)
                break

    valid_properties = []
    for i in range(len(properties)):
        valid_properties.append(list())
        for ticket in nearby_tickets:
            ticket_valid_props = []
            for ticket_prop in properties:
                if properties[ticket_prop][0] <= ticket[i] <= properties[ticket_prop][1] or \
                        properties[ticket_prop][2] <= ticket[i] <= properties[ticket_prop][3]:
                    ticket_valid_props.append(ticket_prop)
            if len(valid_properties[i]) == 0:
                valid_properties[i] = ticket_valid_props
            valid_properties[i] = [vp for vp in valid_properties[i] if vp in ticket_valid_props]

    idx = 0
    props_order = dict()
    for props in valid_properties:
        props_smaller = []
        for vp in valid_properties:
            if vp != props and len(vp) == len(props) - 1:
                props_smaller = vp
        diff = list(set(props) - set(props_smaller))[0]
        props_order[idx] = diff
        idx += 1

    props_order = list(props_order.values())

    product = 1
    for i in range(len(props_order)):
        if props_order[i].startswith('departure'):
            product *= my_ticket[i]

    print('Part 2:', product)


def main():
    with open('in.txt') as file:
        lines = [line for line in file.read().split('\n\n')]

    properties = lines[0].splitlines()
    properties = [prop.split(':') for prop in properties]

    for i in range(len(properties)):
        prop = properties[i]
        value = prop[1].strip()
        ranges = value.split(' or ')
        list_ranges = []
        for r in ranges:
            min_range = int(r.split('-')[0])
            max_range = int(r.split('-')[1])
            list_ranges.append(min_range)
            list_ranges.append(max_range)
        properties[i][1] = list_ranges

    properties = {prop[0]: prop[1] for prop in properties}

    my_ticket = [int(nr) for nr in lines[1].splitlines()[1].split(',')]
    nearby_tickets = [[int(t) for t in ticket.split(',')] for ticket in lines[2].splitlines()[1:]]

    part1(properties, nearby_tickets)
    part2(properties, my_ticket, nearby_tickets)


if __name__ == '__main__':
    main()
