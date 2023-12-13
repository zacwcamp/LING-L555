# Pitch Listing and copy it to the clipboard

# Open the audio file, shown is my filepath as example and testing; modify for your file path
sound = Read from file: "/Users/zachcampbell/LING-L555/project/ExampleToneAudio.wav"

# Pitch object
pitch = To Pitch: 0.05, 75, 600

# Extract Pitch Listing
pitchList = Extract pitch: 0, 0, "no", "yes", 0.03, 600

# Save Pitch Listing to txt file
Write pitchList to text file: "/Users/zachcampbell/LING-L555/project/PitchListing1.txt"

# Copy to the clipboard
Read aloud from file: "/Users/zachcampbell/LING-L555/project/PitchListing1.txt"
editor.selectAll
editor.copy