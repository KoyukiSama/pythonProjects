import os
import time

def display_ascii_animation(folder_path, frame_rate=0.1):
    """
    Display ASCII art animation from a series of text files in a specified folder.
    
    :param folder_path: Path to the folder containing ASCII text files.
    :param frame_rate: Delay between frames in seconds.
    """

    print("Script started. Expanding folder path...")  # Initial debug statement

    # Expand the user's home directory symbol
    folder_path = os.path.expanduser(folder_path)
    print("Loading files from:", folder_path)  # Check if the path expands correctly

    try:
        files = sorted(os.listdir(folder_path))
        print("Files found:", files)  # Check what files are found
    except Exception as e:
        print("Failed to list directory:", e)  # Catch and print any errors reading the directory
        return  # Exit the function if directory listing fails

    frames = []  # List to store the contents of each frame file

    # Read each file and append its content to the frames list
    for file_name in files:
        if file_name.endswith('.txt'):
            try:
                with open(os.path.join(folder_path, file_name), 'r') as file:
                    frames.append(file.read())
                print(f"Loaded frame from {file_name}")  # Confirm each file is loaded
            except Exception as e:
                print(f"Failed to read {file_name}: {e}")  # Catch and print any file reading errors

    print(f"Total frames loaded: {len(frames)}")  # Show total frames loaded

    # Try to display each frame in a loop, handling KeyboardInterrupt to stop the animation
    try:
        while True:
            for frame in frames:
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen command for Windows and Unix
                print(frame)
                time.sleep(frame_rate)
    except KeyboardInterrupt:
        print("Stopped by user.")

# Call the function with the appropriate path
if __name__ == "__main__":
    display_ascii_animation('~/txt-files/')