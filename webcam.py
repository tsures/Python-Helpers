import cv2
from pyzbar import pyzbar

# Known real-world size of the QR code (e.g., 0.2 meters)
REAL_QR_CODE_WIDTH = 0.02  # in meters

# Known focal length of the camera (obtained from calibration)
FOCAL_LENGTH = 1875  # adjust this value based on your camera calibration

def calculate_distance(known_width, focal_length, perceived_width):
    # Calculate the distance using the known size, focal length, and perceived size in the image
    if perceived_width > 0:
        return (known_width * focal_length) / perceived_width
    return -1  # return -1 if perceived width is invalid

def read_qr_code(frame):
    # Decode the QR codes from the frame
    qr_codes = pyzbar.decode(frame)

    for qr_code in qr_codes:
        # Extract the bounding box of the QR code
        (x, y, w, h) = qr_code.rect
        # Draw a rectangle around the QR code
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Decode the QR code data and convert it to string
        qr_data = qr_code.data.decode('utf-8')
        qr_type = qr_code.type

        # Calculate distance based on the width of the bounding box
        distance = calculate_distance(REAL_QR_CODE_WIDTH, FOCAL_LENGTH, w)

        # Display the decoded QR code data and its type
        text = f"{qr_data} ({qr_type})"
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Display telemetry (location of QR code and distance)
        telemetry = f"Location: x={x}, y={y}, w={w}, h={h}, Distance: {distance:.2f} meters"
        cv2.putText(frame, telemetry, (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Print telemetry data in the terminal
        print(f"QR Code detected: {qr_data}")
        print(f"Telemetry: x={x}, y={y}, width={w}, height={h}, Distance: {distance:.2f} meters")
    
    return frame

def main():
    # Initialize webcam capture
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Press 'q' to exit.")

    while True:
        # Capture frame-by-frame from the webcam
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture image.")
            break

        # Process the frame and read QR codes
        frame = read_qr_code(frame)

        # Display the frame with QR code detection
        cv2.imshow('QR Code Scanner with Distance', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
