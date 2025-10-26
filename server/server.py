import os, io, json, base64, tempfile, mimetypes, glob
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from PIL import Image
from asyncio.subprocess import create_subprocess_exec, PIPE
from google import genai

client = genai.Client(api_key="AIzaSyCAalnkqZ6pbj3mUVpzNw_DOUG58fxO0EY")

PHOTO_DIR = os.getenv("PHOTO_DB_DIR", "./data/photos")
CSV_PATH = os.getenv("CSV_PATH", "./public/SuitData.csv")

app = Flask(__name__)
CORS(app, resources={r"/process": {"origins": ["http://localhost:8080", "http://127.0.0.1:8080"]}})

def encode_file(path):
    with open(path, "rb") as f:
        data = f.read()
    mime = mimetypes.guess_type(path)[0] or "application/octet-stream"
    return {"mime_type": mime, "data": data}

def encode_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes))
    out = io.BytesIO()
    img.save(out, format=img.format or "PNG")
    mime = Image.MIME.get(img.format, "image/png")
    return {"mime_type": mime, "data": out.getvalue()}

async def run_pose(image_bytes):
    with tempfile.NamedTemporaryFile(suffix=".docx", delete=False) as tmp:
        tmp.write(image_bytes)
        path = tmp.name
    proc = await create_subprocess_exec("bash", "-c", f"python getPose.py {path} 2>/dev/null", stdout=PIPE)
    out, _ = await proc.communicate()
    return float(out.decode().strip())

def gemini(prompt, user_image, db_images, csv_part):
    parts = [
        {"text": prompt},
        {"inline_data": user_image},
        {"inline_data": csv_part},
    ]
    for p in db_images[:5]:
        parts.append({"inline_data": p})

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[{"role": "user", "parts": parts}],
    )

    text = response.text.strip()
    ids = [int(x.strip()) for x in text.replace("\n", " ").split(",") if x.strip().isdigit()][:4]
    return ids

@app.route("/process", methods=["POST"])
def process():
    sentence = (request.form.get("sentence") or "").strip()
    file = request.files.get("image")

    image_bytes = file.read()
    import asyncio
    chest = asyncio.run(run_pose(image_bytes))
    chest = round(chest * 39.3700787)
    user_image = encode_image(image_bytes)
    db_files = sorted(glob.glob(os.path.join(PHOTO_DIR, "**", "*.*"), recursive=True))
    db_images = [encode_file(p) for p in db_files]
    with open(CSV_PATH, "rb") as f:
        csv_data = f.read()
    csv_part = {"mime_type": "text/csv", "data": csv_data}

    prompt = (
        "You are a stylist. You will receive: 1) an uploaded person photo, 2) a chest size estimate, "
        "3) a suit photo database, 4) a CSV of IDs and attributes, 5) a user sentence.\n\n"
        f"Chest size: {chest}\nUser sentence: {sentence}\n\n"
        "Respond with four comma-separated suit IDs, no extra words."
        "Check the chest size estimate, then only display suits that have the corresponding chest size with a yes in the stock attribute."
    )

    ids = gemini(prompt, user_image, db_images, csv_part)
    url = f"http://localhost:8080/#/results?chest={chest}&ids={ids}"
    resp = jsonify({"redirect": url})
    resp.headers.add("Access-Control-Allow-Origin", "http://localhost:8080")
    resp.headers.add("Access-Control-Allow-Headers", "Content-Type")
    resp.headers.add("Access-Control-Allow-Methods", "POST")
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True, threaded=True)
