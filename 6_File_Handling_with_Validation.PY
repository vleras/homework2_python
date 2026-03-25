# Requirements
# Write a script that:
# •	Reads a file 
# •	Finds: 
# o	total number of lines 
# o	longest line 
# •	Handles: 
# o	file not found error 
# o	empty file 

def analyze_file(file_path):
    try:
        with open(file_path, "r") as file:
            line_count = 0
            max_len = 0
            longest_line = ""

            for line in file:
                line_count += 1
                l = len(line)

                if l > max_len:
                    max_len = l
                    longest_line = line

            if line_count == 0:
                return "File is empty"

            return f"Total lines: {line_count}, Longest line: {longest_line.strip()}"

    except FileNotFoundError:
        return "File not found"
    
print(analyze_file("test.txt"))

