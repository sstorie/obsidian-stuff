import pyperclip

def format_text(text):
    # Split the text into lines
    lines = text.split('\n')
    
    # Initialize variables
    formatted_lines = []
    processing = False
    
    # Iterate over each line
    for line in lines:
        # Start processing when the meeting summary starts
        if line.startswith('Meeting summary for'):
            processing = True
            formatted_lines.append('## ' + line)
        elif processing:
            # Format headers based on the line content
            if line.startswith('Quick recap') or line.startswith('Summary'):
                formatted_lines.append('### ' + line)
            elif len(line) < 80 and not line.startswith('•') and line.strip():
                formatted_lines.append('\n#### ' + line)
            elif line.startswith('•'):
                formatted_lines.append('- ' + line[1:].strip())
            else:
                formatted_lines.append(line)
        
        # Stop processing when AI-generated content starts
        if line.startswith('AI-generated content'):
            break
    
    # Join the formatted lines
    return '\n'.join(formatted_lines)

# Read text from clipboard
clipboard_text = pyperclip.paste()

# Format the text
formatted_text = format_text(clipboard_text)

# Write the result back to the clipboard
pyperclip.copy(formatted_text)
