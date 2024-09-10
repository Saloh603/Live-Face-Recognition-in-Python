import face_recognition
import os
import asyncio

# Folder containing known images for verification
KNOWN_IMAGES_DIR = "./known_faces"

async def load_and_compare(target_image_path):
    # Load target image
    target_image = face_recognition.load_image_file(target_image_path)
    target_encodings = face_recognition.face_encodings(target_image)

    if len(target_encodings) == 0:
        return False  # No faces detected

    target_encoding = target_encodings[0]

    # List all known images asynchronously
    for filename in os.listdir(KNOWN_IMAGES_DIR):
        known_image_path = os.path.join(KNOWN_IMAGES_DIR, filename)
        await asyncio.sleep(0)  # Yield control to event loop

        known_image = face_recognition.load_image_file(known_image_path)
        known_encodings = face_recognition.face_encodings(known_image)

        if len(known_encodings) > 0:
            known_encoding = known_encodings[0]

            # Compare faces
            match = face_recognition.compare_faces([known_encoding], target_encoding)
            if match[0]:
                return True

    return False
