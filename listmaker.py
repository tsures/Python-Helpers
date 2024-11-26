import re

def process_ingredient_list(input_text):
    # Split the input text into lines
    lines = input_text.strip().split('\n')
    
    # Process each line
    processed_lines = []
    for line in lines:
        # Skip completely empty lines
        if not line.strip():
            continue
        
        # Split the line by both / and spaces, removing empty strings
        parts = [part for part in re.split(r'[/\s]+', line) if part.strip()]
        
        # Reconstruct the line, keeping original groupings
        processed_line = []
        current_group = []
        for part in parts:
            current_group.append(part)
            
            # If we have a potential grouping (marked by /)
            if '/' in line and line.count(part + '/') > 0:
                continue
            
            # Add the processed group
            processed_lines.append(' '.join(current_group))
            current_group = []
    
    return processed_lines

def create_html_list(processed_lines):
    # Create an HTML unordered list, filtering out any empty lines
    html = "<ul>\n"
    for line in processed_lines:
        # Only add non-empty lines
        if line.strip():
            html += f"  <li>{line}</li>\n"
    html += "</ul>"
    return html

# Example usage
input_text = '''

שווארמה מן הצומח     

רכיבים: מים /חלבון סויה צימחי/ירקות מייבשים/מלח/ 

סוכר/תבלינים/חומרי טעם וריח                                                              

בצל 

עמבה 

מלח/קארי 

תבלין שווארמה 

שמן זית 
'''

# Process the input
processed_lines = process_ingredient_list(input_text)

# Print processed lines
print("Processed Lines:")
for line in processed_lines:
    print(line)

# Generate HTML list
html_list = create_html_list(processed_lines)
print("\nHTML List:")
print(html_list)

# Optional: Write to an HTML file
with open('ingredient_list.html', 'w', encoding='utf-8') as f:
    f.write(html_list)