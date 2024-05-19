import os

# Define your alphabet data
alphabets = [
    {"letter": "അ", "name": "A"},
    {"letter": "ആ", "name": "AA"},
    {"letter": "ഇ", "name": "I"},
    {"letter": "ഈ", "name": "II"},
    {"letter": "ഉ", "name": "U"},
    {"letter": "ഊ", "name": "UU"},
    {"letter": "ഋ", "name": "R"},
    {"letter": "എ", "name": "E"},
    {"letter": "ഏ", "name": "EE"},
    {"letter": "ഐ", "name": "AI"},
    {"letter": "ഒ", "name": "O"},
    {"letter": "ഓ", "name": "OO"},
    {"letter": "ഔ", "name": "AU"},
    {"letter": "ക", "name": "KA"},
    {"letter": "ഖ", "name": "KHA"},
    {"letter": "ഗ", "name": "GA"},
    {"letter": "ഘ", "name": "GHA"},
    {"letter": "ങ", "name": "NGA"},
    {"letter": "ച", "name": "CHA"},
    {"letter": "ഛ", "name": "CHHA"},
    {"letter": "ജ", "name": "JA"},
    {"letter": "ഝ", "name": "JHA"},
    {"letter": "ഞ", "name": "NYA"},
    {"letter": "ട", "name": "TA"},
    {"letter": "ഠ", "name": "THA"},
    {"letter": "ഡ", "name": "DA"},
    {"letter": "ഢ", "name": "DHA"},
    {"letter": "ണ", "name": "NA"},
    {"letter": "ത", "name": "THA"},
    {"letter": "ഥ", "name": "THHA"},
    {"letter": "ദ", "name": "DA"},
    {"letter": "ധ", "name": "DHHA"},
    {"letter": "ന", "name": "NA"},
    {"letter": "പ", "name": "PA"},
    {"letter": "ഫ", "name": "PHA"},
    {"letter": "ബ", "name": "BA"},
    {"letter": "ഭ", "name": "BHA"},
    {"letter": "മ", "name": "MA"},
    {"letter": "യ", "name": "YA"},
    {"letter": "ര", "name": "RA"},
    {"letter": "ല", "name": "LA"},
    {"letter": "ള", "name": "LLA"},
    {"letter": "വ", "name": "VA"},
    {"letter": "ശ", "name": "SHA"},
    {"letter": "ഷ", "name": "SSHA"},
    {"letter": "സ", "name": "SA"},
    {"letter": "ഹ", "name": "HA"},
    {"letter": "ള", "name": "LLA"},
    {"letter": "ഴ", "name": "LLA"},
    {"letter": "റ", "name": "RA"},
    {"letter": "റ", "name": "RA"},
    {"letter": "റ", "name": "RA"}
]
# HTML template for each alphabet file
alphabet_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Learn Malayalam Alphabet: {letter}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #FFF;
            margin: 0;
            padding: 0;
            color: #660000;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}
        .navbar {{
            background-color: #ffffff;
            display: flex;
            align-items: center;
            width: 100%;
            padding: 10px 20px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }}
        .navbar .logo {{
            max-width: 50px;
            max-height: 50px;
            margin-right: 50px;
        }}
        .navbar nav {{
            margin-left: auto;
            display: flex;
            gap: 20px;
        }}
        .navbar nav a {{
            text-decoration: none;
            color: #660000;
            font-weight: bold;
        }}
        .container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 20px;
            padding: 20px;
            width: 100%;
            max-width: 1200px;
            box-sizing: border-box;
        }}
        .alphabet {{
            background-color: #fff;
            border: 2px solid #cc0000;
            border-radius: 10px;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 100%;
            max-width: 400px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }}
        .alphabet img {{
            max-width: 150px;
            margin-bottom: 10px;
            border: 2px solid #cc0000;
            border-radius: 10px;
        }}
        .alphabet audio {{
            margin-bottom: 10px;
        }}
        .canvas-container {{
            display: flex;
            flex-direction: column;
            align-items: center;
        }}
        canvas {{
            border: 2px solid #cc0000;
            border-radius: 10px;
            background-color: #ffe6e6;
            margin-top: 10px;
            width: 100%;
            max-width: 300px;
        }}
        button {{
            margin-top: 10px;
            padding: 10px 20px;
            background-color: #cc0000;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }}
        button:hover {{
            background-color: #a30000;
        }}
        @media screen and (min-width: 600px) {{
            .container {{
                flex-direction: row;
                flex-wrap: wrap;
            }}
        }}
    </style>
</head>
<body>

    <div class="navbar">
        <img src="logo.png" alt="Logo" class="logo">
        <nav>
            <a href="index.html">Home</a>
            <a href="#">Alphabets</a>
            <a href="#">About</a>
            <a href="#">Contact</a>
        </nav>
    </div>

    <div class="container">
        <div class="alphabet">
            <h2>Letter: {letter} ({name})</h2>
            <img src="Gif/{letter}.gif" alt="{letter} GIF">
            <div>
                <audio controls>
                    <source src="Audio/{letter}.mp3" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </div>
            <div class="canvas-container">
                <h3>Trace the alphabet:</h3>
                <canvas id="canvas{letter}" width="300" height="300"></canvas>
                <button onclick="clearCanvas('canvas{letter}')">Clear</button>
            </div>
        </div>
    </div>

    <script>
        function initCanvas(canvasId) {{
            const canvas = document.getElementById(canvasId);
            const ctx = canvas.getContext('2d');
            let drawing = false;

            function startDrawing(event) {{
                drawing = true;
                ctx.beginPath();
                draw(event);
            }}

            function stopDrawing() {{
                drawing = false;
                ctx.beginPath();
            }}

            function draw(event) {{
                if (!drawing) return;
                
                let clientX, clientY;
                if (event.touches) {{
                    clientX = event.touches[0].clientX;
                    clientY = event.touches[0].clientY;
                }} else {{
                    clientX = event.clientX;
                    clientY = event.clientY;
                }}

                const rect = canvas.getBoundingClientRect();
                ctx.lineTo(clientX - rect.left, clientY - rect.top);
                ctx.stroke();
            }}

            canvas.addEventListener('mousedown', startDrawing);
            canvas.addEventListener('mousemove', draw);
            canvas.addEventListener('mouseup', stopDrawing);
            canvas.addEventListener('mouseout', stopDrawing);

            canvas.addEventListener('touchstart', (event) => {{
                event.preventDefault();
                startDrawing(event);
            }}, {{ passive: false }});
            canvas.addEventListener('touchmove', (event) => {{
                event.preventDefault();
                draw(event);
            }}, {{ passive: false }});
            canvas.addEventListener('touchend', (event) => {{
                event.preventDefault();
                stopDrawing();
            }});
        }}

        function clearCanvas(canvasId) {{
            const canvas = document.getElementById(canvasId);
            const ctx = canvas.getContext('2d');
            ctx.clearRect(0, 0, canvas.width, canvas.height);
        }}

        // Initialize canvas
        document.addEventListener('DOMContentLoaded', () => {{
            initCanvas('canvas{letter}');
        }});
    </script>
    
    {next_button}
</body>
</html>
"""

# Create the output directory if it doesn't exist
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Generate HTML files for each alphabet
for i, alphabet in enumerate(alphabets):
    letter = alphabet["letter"]
    name = alphabet["name"]
    next_button = ""
    
    if i < len(alphabets) - 1:
        next_letter = alphabets[i + 1]["letter"]
        next_button = f'<button onclick="location.href=\'{next_letter}.html\'">Next</button>'
    
    html_content = alphabet_template.format(letter=letter, name=name, next_button=next_button)
    
    with open(os.path.join(output_dir, f"{letter}.html"), "w", encoding="utf-8") as file:
        file.write(html_content)

print("HTML files generated successfully!")
