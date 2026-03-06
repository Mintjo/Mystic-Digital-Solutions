import os
import re

base_dir = r"c:\Users\ADMIN\Desktop\Mystic Digital Solutions"
css_file = os.path.join(base_dir, "css", "style.css")
js_file = os.path.join(base_dir, "js", "main.js")
css_min_file = os.path.join(base_dir, "css", "style.min.css")
js_min_file = os.path.join(base_dir, "js", "main.min.js")

def minify_css(css):
    # Remove CSS comments
    css = re.sub(r'/\*[\s\S]*?\*/', '', css)
    # Remove newlines and tabs
    css = css.replace('\n', '').replace('\r', '').replace('\t', '')
    # Remove multiple spaces
    css = re.sub(r'\s+', ' ', css)
    # Remove space around standard CSS separators
    css = re.sub(r'\s*([\{\}\:\;\,\>\+\~])\s*', r'\1', css)
    # Remove trailing semicolons in blocks
    css = re.sub(r';\}', '}', css)
    return css.strip()

def minify_js(js):
    # Remove multi-line comments
    js = re.sub(r'/\*[\s\S]*?\*/', '', js)
    # Remove single-line comments (simple approach, might fail if // is inside string)
    js = re.sub(r'//.*', '', js)
    # Remove newlines and tabs
    js = js.replace('\n', '').replace('\r', '').replace('\t', '')
    # Remove multiple spaces
    js = re.sub(r'\s+', ' ', js)
    # Remove space around standard JS separators
    js = re.sub(r'\s*([\{\}\(\)\[\]\:\;\,\=\+\-\*\/\!\<\>\&\|])\s*', r'\1', js)
    # simple fix for missing space before words after operators if needed, but above usually suffices for simple JS
    return js.strip()

# Minify CSS
if os.path.exists(css_file):
    with open(css_file, 'r', encoding='utf-8') as f:
        css_content = f.read()
    minified_css = minify_css(css_content)
    with open(css_min_file, 'w', encoding='utf-8') as f:
        f.write(minified_css)
    print(f"Minified {css_file} -> {css_min_file}")
    
# Minify JS
if os.path.exists(js_file):
    with open(js_file, 'r', encoding='utf-8') as f:
        js_content = f.read()
    minified_js = minify_js(js_content)
    with open(js_min_file, 'w', encoding='utf-8') as f:
        f.write(minified_js)
    print(f"Minified {js_file} -> {js_min_file}")

# Update HTML files to use minified versions
def update_html_links(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace css link
        content = re.sub(r'href="(\.\./)?css/style\.css"', r'href="\1css/style.min.css"', content)
        # Replace js script
        content = re.sub(r'src="(\.\./)?js/main\.js"', r'src="\1js/main.min.js"', content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated HTML: {os.path.basename(filepath)}")
    except Exception as e:
        print(f"Error on {filepath}: {e}")

# Process files in root
for f in os.listdir(base_dir):
    if f.endswith(".html"):
        update_html_links(os.path.join(base_dir, f))

# Process files in secteurs directory
secteurs_dir = os.path.join(base_dir, "secteurs")
if os.path.exists(secteurs_dir):
    for f in os.listdir(secteurs_dir):
        if f.endswith(".html"):
            update_html_links(os.path.join(secteurs_dir, f))

print("Minification and HTML updates complete.")
