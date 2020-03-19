src_file_path = "gitlog"
extension = ".txt"

file_name = "{}{}".format(src_file_path, extension)

print("LOG PROCESSOR!!!")

with open(file_name) as f:
  content = f.readlines()

content = [x.strip() for x in content]

new_content = []
for line in content:
  if not (line.startswith("commit") or line.startswith("Author:")):
    if line.startswith("Date:"):
      new_line = line.replace("Date:  ", "###")
      new_content.append("-----------------------")
      new_content.append(new_line)
    elif line.startswith("["):
      new_content.append("### {}".format(line))
    else:
      new_content.append("\n")
      new_content.append(line)

for new_line in new_content:
  print(new_line)