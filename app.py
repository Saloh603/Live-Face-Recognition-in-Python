import asyncio
from flask import Flask, request, jsonify
import aiofiles
from face_verification import load_and_compare

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
async def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image = request.files['image']
    if image.filename == '':
        return jsonify({'error': 'No image selected'}), 400

    # Asynchronous saving of image to a local folder
    save_path = f"./uploads/{image.filename}"
    async with aiofiles.open(save_path, 'wb') as f:
        await f.write(image.read())

    # Run face verification asynchronously
    is_verified = await load_and_compare(save_path)

    return jsonify({'verified': is_verified}), 200

if __name__ == '__main__':
    app.run(debug=True)
