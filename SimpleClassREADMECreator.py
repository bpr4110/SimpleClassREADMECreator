import re


def nameToAnchor(name):
    try:
        res = nameToAnchor.symbolPattern.\
            sub("", name).replace(" ", "-").lower()
        if res in nameToAnchor.nameDict:
            nameToAnchor.nameDict[res] += 1
            res += f"-{nameToAnchor.nameDict[res]}"
        else:
            nameToAnchor.nameDict[res] = 0
        return res
    except AttributeError:
        nameToAnchor.nameDict = {}
        nameToAnchor.symbolPattern = re.compile(r"[^a-zA-Z0-9\s]")
        return nameToAnchor(name)


def writeTableItem(f, name, depth):
    anchor = nameToAnchor(name)
    f.write('\t'*(depth))
    f.write(f"- [{name}](#{anchor})\n")


def writeHeader(f, name, depth):
    if depth == 3:
        f.write("- ")
    f.write('#' * (depth + 1))
    f.write(f" {name}\n")


className = input("Enter Class Name: ")

with open(f"{className}.md", "w") as f:
    title = f"{className} API Documentation"
    f.write(title)
    f.write("\n")
    f.write(f"{'=' * max(3, len(title))}")
    f.write("\n\n")
    f.write("# Table of contents\n")
    writeTableItem(f, f"Class: {className}", 0)
    constructorArgs = input("Enter constructor args: ")
    writeTableItem(f, f"Constructor({constructorArgs})", 1)
    properties = {"Public": [], "Protected": [], "Private": []}
    methods = {"Public": [], "Protected": [], "Private": []}
    for scope in properties:
        print(f"{scope} properties:")
        while True:
            name = input()
            if name == "":
                break
            properties[scope].append(name)
    for scope in methods:
        print(f"{scope} methods:")
        while True:
            name = input()
            if name == "":
                break
            methods[scope].append(name)
    writeTableItem(f, "Properties", 1)
    for scope in properties:
        if len(properties[scope]) > 0:
            writeTableItem(f, scope, 2)
            for field in properties[scope]:
                writeTableItem(f, field, 3)
    writeTableItem(f, "Methods", 1)
    for scope in methods:
        if len(methods[scope]) > 0:
            writeTableItem(f, scope, 2)
            for field in methods[scope]:
                writeTableItem(f, field, 3)
    writeTableItem(f, "Source", 1)
    f.write("\n")
    writeHeader(f, f"Class: {className}", 0)
    writeHeader(f, f"Constructor({constructorArgs})", 1)
    f.write("\n")
    writeHeader(f, "Properties", 1)
    for index in range(3):
        scope = [*properties][index]
        if len(properties[scope]) > 0:
            if index > 0:
                f.write("\n")
            writeHeader(f, scope, 2)
            for field in properties[scope]:
                writeHeader(f, field, 3)
    f.write("\n")
    writeHeader(f, "Methods", 1)
    for index in range(3):
        scope = [*methods][index]
        if len(methods[scope]) > 0:
            if index > 0:
                f.write("\n")
            writeHeader(f, scope, 2)
            for field in methods[scope]:
                writeHeader(f, field, 3)
    f.write("\n")
    writeHeader(f, "Source", 1)
