def simpleFormatting(data):
    for i in range(len(data)):
        if '\n' in data[i]:
            data[i] = data[i].split('\n')  # Create sub list
        if '    ' in data[i]:
            data[i] = data[i].split("    ")  # Create sub list
        if '   ' in data[i]:
            data[i] = data[i].split("   ")  # Create sub list

    # Hardcoded sub lists (Guaranteed in every scrape)
    data[1][0] = data[1][0].split(" Instruction ")
    data[1][1] = data[1][1].split(" Activity ")
    data[1][2] = data[1][2].split(" Class/")
    data[1][3] = data[1][3].split(" Session ")
    data[1][4] = data[1][4].split(" Orion ")

    return data

# Converts the raw data into a neat API output


def simpleFormattingHead(head):
    for i in range(len(head)):
        if ':' in head[i]:
            head[i] = head[i].replace(':', '')
        if '(s)' in head[i]:
            head[i] = head[i].replace('(s)', '')
        if ' ' in head[i]:
            head[i] = head[i].replace(' ', '_')
    return head

# Combines two parallel arrays into a single object


def final_obj(head, data):
    final = {}
    for i in range(len(head)):
        final.update({head[i].lower(): data[i]})
    return final


def add_elements_to_array(elem):
    data = []
    for obj in elem:
        data.append(obj.text)
    return data
