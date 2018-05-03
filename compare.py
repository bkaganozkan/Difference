text_dict = {}
text_2_dict = {}

compare_result = []
f_object = ""

f_text, s_text = "", ""


def set_first_object(obj_no):
    global f_object
    f_object = obj_no


def joinText(text, obNo=""):
    global f_object
    global f_text, s_text
    if obNo is f_object:
        f_text = text
    else:
        s_text = text


def readFiles(f_file_path, s_file_path):
    try:
        with open(f_file_path, mode='r', encoding="utf-8") as read_file:
            f_text = read_file.readlines()
    except:
        print("First File Didn't Read")
    try:
        with open(s_file_path, mode='r', encoding="utf-8") as read_file:
            s_text = read_file.readlines()
    except:
        print("Second File Didn't Read")
    try:
        return f_text, s_text
    except:
        print("Return Nothing")


def clearText(f_text, s_text):
    first, second = "", ""
    # First Text
    for index, text in enumerate(f_text):
        if text is "\n":
            if f_text[index - 1] is "\n":
                pass
            else:
                first += text
        else:
            first += text
    f_text = first

    # Second Text
    for index, text in enumerate(s_text):
        if text is '\n':
            if s_text[index - 1] is "\n":
                pass
            else:
                second += text
        else:
            second += text
    s_text = second
    return f_text, s_text


def compareTexts(f_text, s_text):
    global text_dict, text_2_dict
    text_dict, text_2_dict = {}, {}
    f, s = clearText(f_text, s_text)
    compare_results = []
    compare_2_results = []

    # First Text divided to lines
    line = ""
    line_count = 0
    for index, text in enumerate(f):
        if text is "\n":
            line = ""
            line_count += 1
        else:
            line += text
        text_dict[line_count] = line

    # Second text divided to lines
    line = ""
    line_count = 0
    for index, text in enumerate(s):
        if text is "\n":
            line = ""
            line_count += 1
        else:
            line += text
        text_2_dict[line_count] = line

    # Comparing lines and letters
    for ind in range(0, len(text_dict)):
        try:
            for index, latter in enumerate(text_dict[ind]):
                if text_dict[ind][index] is text_2_dict[ind][index]:
                    pass
                else:
                    compare_results.append([ind, index])
        except:
            compare_results.append([ind, index])

    # Comparing for second lines and letters

    for ind in range(0, len(text_2_dict)):
        try:
            for index, latter in enumerate(text_dict[ind]):
                if text_2_dict[ind][index] is text_dict[ind][index]:
                    pass
                else:
                    compare_2_results.append([ind, index])
        except:
            compare_2_results.append([ind, index])

    for res in compare_2_results:
        if res in compare_results:
            pass
        else:
            compare_results.append(res)

    # for res in compare_result:
    #     if res in compare_2_results:
    #         pass
    #     else:
    #         compare_result.append(res)
    # print(compare_result)
    return compare_results


def retResult():
    global compare_result
    global f_text, s_text
    try:
        result = compareTexts(f_text, s_text)
        compare_result = result
        return result
    except:
        # print("olmadı")
        pass
