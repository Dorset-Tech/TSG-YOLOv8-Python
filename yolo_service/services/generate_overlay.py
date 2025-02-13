import cv2
import numpy as np
from image_registration import cross_correlation_shifts

from yolo_service.services.config import base_frame_weight, fps_percentage
from yolo_service.services.draw_ball import draw_ball_curve


def generate_overlay(video_frames, width, height, fps, outputPath):
    print("Saving overlay result to", outputPath)

    out = cv2.VideoWriter(
        outputPath,
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps * fps_percentage,
        (width, height),
    )

    frame_lists = sorted(video_frames, key=len, reverse=True)
    balls_in_curves = [[] for i in range(len(frame_lists))]
    shifts = {}

    # Assume the distance of 8 meters is represented by the width of the video
    pixel_to_meter = 22 / width

    # Take the longest frames as background
    for idx, base_frame in enumerate(frame_lists[0]):
        # Overlay frames
        background_frame = base_frame.frame.copy()
        for list_idx, frameList in enumerate(frame_lists[1:]):
            if idx < len(frameList):
                overlay_frame = frameList[idx]
            else:
                overlay_frame = frameList[len(frameList) - 1]

            alpha = 1.0 / (list_idx + 2)
            beta = 1.0 - alpha
            corrected_frame = image_registration(
                background_frame, overlay_frame, shifts, list_idx, width, height
            )
            background_frame = cv2.addWeighted(
                corrected_frame, alpha, background_frame, beta, 0
            )

            # Prepare balls to draw
            if overlay_frame.ball_in_frame:
                balls_in_curves[list_idx + 1].append(
                    [
                        overlay_frame.ball[0],
                        overlay_frame.ball[1],
                        overlay_frame.ball_color,
                        overlay_frame.laatu,
                    ]
                )

        if base_frame.ball_in_frame:
            balls_in_curves[0].append(
                [
                    base_frame.ball[0],
                    base_frame.ball[1],
                    base_frame.ball_color,
                    base_frame.laatu,
                ]
            )

        # Emphasize base frame
        background_frame = cv2.addWeighted(
            base_frame.frame,
            base_frame_weight,
            background_frame,
            1 - base_frame_weight,
            0,
        )

        # Draw transparent curve and non-transparent balls
        for trajectory in balls_in_curves:
            background_frame = draw_ball_curve(background_frame, trajectory)

        out.write(background_frame)
        if cv2.waitKey(120) & 0xFF == ord("q"):
            break

    # Calculate and print ball speeds
    average_speeds = []
    for trajectory in balls_in_curves:
        ball_positions = [(point[0], point[1]) for point in trajectory]
        speeds, average_speed = calculate_speed(ball_positions, fps, pixel_to_meter)
        for i, speed in enumerate(speeds):
            print(f"Speed between frame {i} and {i+1}: {speed:.2f} km/h")
        average_speeds.append(average_speed)

    out.release()
    print("Overlay generation complete")
    return f"{average_speeds[0]:.2f} km/h" if average_speeds else "0.00 km/h"


def image_registration(ref_image, offset_image, shifts, list_idx, width, height):
    # The shift is calculated once for each video and stored
    if list_idx not in shifts:
        xoff, yoff = cross_correlation_shifts(
            ref_image[:, :, 0], offset_image.frame[:, :, 0]
        )
        shifts[list_idx] = (xoff, yoff)
    else:
        xoff, yoff = shifts[list_idx]

    offset_image.ball = tuple(
        [offset_image.ball[0] - int(xoff), offset_image.ball[1] - int(yoff)]
    )
    matrix = np.float32([[1, 0, -xoff], [0, 1, -yoff]])
    corrected_image = cv2.warpAffine(offset_image.frame, matrix, (width, height))

    return corrected_image


def calculate_speed(ball_positions, fps, pixel_to_meter):
    speeds = []
    for i in range(1, len(ball_positions)):
        x1, y1 = ball_positions[i - 1]
        x2, y2 = ball_positions[i]

        # Ensure the coordinates are on the CPU and converted to NumPy
        if not isinstance(x1, int):
            x1 = x1.cpu().item()
        if not isinstance(y1, int):
            y1 = y1.cpu().item()
        if not isinstance(x2, int):
            x2 = x2.cpu().item()
        if not isinstance(y2, int):
            y2 = y2.cpu().item()

        distance_pixels = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        distance_meters = distance_pixels * pixel_to_meter
        speed_mps = distance_meters * fps  # meters per second
        speed_kph = speed_mps * 3.6  # convert to kilometers per hour
        speeds.append(speed_kph)

    average_speed = np.mean(speeds) if speeds else 0
    return speeds, average_speed


def calculate_speed(ball_positions, fps, pixel_to_meter):
    speeds = []
    for i in range(1, len(ball_positions)):
        x1, y1 = ball_positions[i - 1]
        x2, y2 = ball_positions[i]

        # Ensure the coordinates are on the CPU and converted to NumPy
        if not isinstance(x1, int):
            x1 = x1.cpu().item()
        if not isinstance(y1, int):
            y1 = y1.cpu().item()
        if not isinstance(x2, int):
            x2 = x2.cpu().item()
        if not isinstance(y2, int):
            y2 = y2.cpu().item()

        distance_pixels = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        distance_meters = distance_pixels * pixel_to_meter
        speed_mps = distance_meters * fps  # meters per second
        speed_kph = speed_mps * 3.6  # convert to kilometers per hour
        speeds.append(speed_kph)

    average_speed = np.mean(speeds) if speeds else 0
    return speeds, average_speed


# Average of the highest Y-axis peak
# def calculate_speed(ball_positions, fps, pixel_to_meter):
#     speeds = []
#     highest_y_index = 0
#     highest_y = float("inf")

#     # Find the highest peak of the Y-axis
#     for i, (x, y) in enumerate(ball_positions):
#         if y < highest_y:
#             highest_y = y
#             highest_y_index = i

#     # Calculate speeds starting from the highest peak
#     for i in range(highest_y_index + 1, len(ball_positions)):
#         x1, y1 = ball_positions[i - 1]
#         x2, y2 = ball_positions[i]

#         # Ensure the coordinates are on the CPU and converted to NumPy
#         if not isinstance(x1, int):
#             x1 = x1.cpu().item()
#         if not isinstance(y1, int):
#             y1 = y1.cpu().item()
#         if not isinstance(x2, int):
#             x2 = x2.cpu().item()
#         if not isinstance(y2, int):
#             y2 = y2.cpu().item()

#         distance_pixels = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
#         distance_meters = distance_pixels * pixel_to_meter
#         speed_mps = distance_meters * fps  # meters per second
#         speed_kph = speed_mps * 3.6  # convert to kilometers per hour
#         speeds.append(speed_kph)

#     average_speed = np.mean(speeds) if speeds else 0
#     return speeds, average_speed
