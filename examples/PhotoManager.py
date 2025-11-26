import os
import json
from dataclasses import dataclass, field, asdict

@dataclass
class PhotoManager:
    displayedImages: list[str] = field(default_factory=list)
    remainingImages: list[str] = field(default_factory=list)

picPath = os.path.join(os.path.dirname(os.path.dirname(__file__)), "pic")
cachedPath = os.path.join(os.path.dirname(os.path.dirname(__file__)), "cached.json")
allImages = [f for f in os.listdir(picPath)
          if f.lower().endswith((".jpg", ".jpeg", ".png", ".bmp"))]

# Ensure file exists
if not os.path.exists(cachedPath):
    with open(cachedPath, "w") as f:
        f.write("")  # create empty JSON

# Create object
with open(cachedPath, "r+") as f:
    try:
        content = f.read()
        if content:  # only parse if not empty
            data = json.loads(content)
        else:
            data = {}
    except json.JSONDecodeError as error:
        data = {}
    cachedManager = PhotoManager(**data)

    # Reset if needed
    if len(cachedManager.remainingImages) == 0:
        cachedManager.remainingImages = allImages
        cachedManager.displayedImages = []

    indexedImages = cachedManager.displayedImages + cachedManager.remainingImages
    newImages = []

    # Insert new images
    for image in allImages:
        if not indexedImages.__contains__(image):
            newImages.append(image)
    cachedManager.remainingImages = newImages + cachedManager.remainingImages

    # Display first image in remaining images
    imageToDisplay = cachedManager.remainingImages.pop(0)
    cachedManager.displayedImages.append(imageToDisplay)

    # Write current index to cached
    f.seek(0)
    json.dump(asdict(cachedManager), f, indent=2)
    f.truncate()