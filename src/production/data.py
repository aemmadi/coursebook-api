import sys
import json
import re


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
        head[i] = head[i].lower()
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

# Adds element data to array


def add_elements_to_array(elem):
    data = []
    for obj in elem:
        data.append(obj.text)
    return data

# Converts raw coursebook data into API output


def scrape_data(course, course_head):

    # Dumps all data into a list
    course_data = add_elements_to_array(course)
    head_data = add_elements_to_array(course_head)

    # Formats all data for neater API output
    course_data = simpleFormatting(course_data)
    head_data = simpleFormattingHead(head_data)

    course_info = final_obj(head_data, course_data)

    if course_info["instructor"] != "-Staff-":
        course_info["instructor"][1] = course_info["instructor"][1].replace(
            "  email: ", "")
    return course_info

# Converts given string to dictionary format


def string_to_dict(val):
    val = val.replace(': ', '" :"')
    val = val.replace('" ', '"')
    val = f'{{"{val}"}}'
    return val

# Reformat into cleaner API output, converts arrays to object


def array_to_obj(course_info):
    inject = ["class_info", "schedule", "status"]  # List of arrays to convert
    temp = {}
    tmp = []
    obj = {}

    # Main loop
    for x in inject:
        length = len(course_info[x])  # Get length of array

        # Loop through array
        for i in range(length):
            if x == "class_info":
                # Loop through sub array
                for k in range(len(course_info[x][i])):
                    # Get elements and convert to obj
                    val = course_info[x][i][k]
                    val = string_to_dict(val)

                    # Add converted obj to temp obj
                    temp.update(json.loads(val))

            elif x == "schedule":
                if ": " in course_info[x][i]:
                    # Get elements and convert to obj
                    val = course_info[x][i]
                    val = string_to_dict(val)

                    # Add converted obj to temp obj
                    temp.update(json.loads(val))
                else:
                    # Add non obj elements into an array
                    tmp.append(course_info[x][i])

            else:
                # Get elements and convert to obj
                val = course_info[x][i]
                val = string_to_dict(val)

                # Add converted obj to temp obj
                temp.update(json.loads(val))

        # Format temp obj just like the rest of the API
        head = simpleFormattingHead(list(temp.keys()))
        data = list(temp.values())

        # If tmp array has any values
        if tmp:
            obj.update({"misc": tmp})  # Add array to object

        # Re-add all the formatted objs into one main obj
        for i in range(len(head)):
            obj.update({head[i]: data[i]})

        # Update main API with new obj
        course_info[x] = obj

        # Reset all temp variables
        temp = {}
        tmp = []
        obj = {}

    return course_info

# Converts course into an array seperating subject and number, math2413 -> [math, 2413]


def convert_course(course):
    num = re.findall('\d+', course)[0]
    subj = course.replace(f"{num}", "")
    return [subj, num]


# Converts term into expanded format, 18f -> Fall 2018


def convert_term(term):
    season = term[-1]
    term = f"20{term[:-1]}"

    if season == "f":
        season = "Fall"
    elif season == "s":
        season = "Spring"
    elif season == "u":
        season = "Summer"
    else:
        return -1

    return f"{season}%20{term}"
