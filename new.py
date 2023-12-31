import cv2
import numpy as np
def order_points(pts):
    '''Rearrange coordinates to order:
      top-left, top-right, bottom-right, bottom-left'''
    rect = np.zeros((4, 2), dtype='float32')
    pts = np.array(pts)
    s = pts.sum(axis=1)
    # Top-left point will have the smallest sum.
    rect[0] = pts[np.argmin(s)]
    # Bottom-right point will have the largest sum.
    rect[2] = pts[np.argmax(s)]
 
    diff = np.diff(pts, axis=1)
    # Top-right point will have the smallest difference.
    rect[1] = pts[np.argmin(diff)]
    # Bottom-left will have the largest difference.
    rect[3] = pts[np.argmax(diff)]
    # Return the ordered coordinates.
    return rect.astype('int').tolist()

def find_dest(pts):
    (tl, tr, br, bl) = pts
    # Finding the maximum width.
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    # Finding the maximum height.
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))
    # Final destination co-ordinates.
    destination_corners = [[0, 0], [maxWidth, 0], [maxWidth, maxHeight], [0, maxHeight]]

    return order_points(destination_corners)
def generate_output(image: np.array, corners: list, scale: tuple = None, resize_shape: int = 640):
    corners = order_points(corners)

    if scale is not None:
        print(np.array(corners).shape, scale)
        corners = np.multiply(corners, scale)

    destination_corners = find_dest(corners)
    M = cv2.getPerspectiveTransform(np.float32(corners), np.float32(destination_corners))
    out = cv2.warpPerspective(image, M, (destination_corners[2][0], destination_corners[2][1]), flags=cv2.INTER_LANCZOS4)
    # print("corners", corners)
    # print("destination_corners", destination_corners)
    out = np.clip(out, a_min=0, a_max=255)
    out = out.astype(np.uint8)
    return out, destination_corners
def scan():
  og_image = cv2.imread("./n8.jpg")
  # height, width, channels = og_image.shape
  # print("Chiều cao:", height)
  # print("Chiều rộng:", width)
  # cv2.imshow("n8", og_image)
  # cv2.waitKey(0)


  orig_img = og_image.copy()
  # Repeated Closing operation to remove text from the document.
  kernel = np.ones((5, 5), np.uint8)
  og_image = cv2.morphologyEx(og_image, cv2.MORPH_CLOSE, kernel, iterations=3)
  # GrabCut
  mask = np.zeros(og_image.shape[:2], np.uint8)
  bgdModel = np.zeros((1, 65), np.float64)
  fgdModel = np.zeros((1, 65), np.float64)
  rect = (20, 20, og_image.shape[1] - 20, og_image.shape[0] - 20)
  cv2.grabCut(og_image, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
  mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")
  og_image = og_image * mask2[:, :, np.newaxis]
  gray = cv2.cvtColor(og_image, cv2.COLOR_BGR2GRAY)
  gray = cv2.GaussianBlur(gray, (11, 11), 0)
  # Edge Detection.
  canny = cv2.Canny(gray, 0, 200)
  canny = cv2.dilate(canny, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))


  # con = np.zeros_like(og_image)
  # Finding contours for the detected edges.
  contours, hierarchy = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
  # Keeping only the largest detected contour.
  page = sorted(contours, key=cv2.contourArea, reverse=True)[:5]
  # con = cv2.drawContours(con, page, -1, (0, 255, 255), 3)

  con = np.zeros_like(og_image)
  # Loop over the contours.
  for c in page:
    # Approximate the contour.
    epsilon = 0.02 * cv2.arcLength(c, True)
    corners = cv2.approxPolyDP(c, epsilon, True)
    # If our approximated contour has four points
    if len(corners) == 4:
        break
  cv2.drawContours(con, c, -1, (0, 255, 255), 3)
  cv2.drawContours(con, corners, -1, (0, 255, 0), 10)
  # Sorting the corners and converting them to desired shape.
  corners = sorted(np.concatenate(corners).tolist())
  output, destination_corners = generate_output(orig_img, corners)
  
  # Displaying the corners.
  for index, c in enumerate(corners):
    character = chr(65 + index)
    cv2.putText(con, character, tuple(c), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 255), 2, cv2.LINE_AA)
  height, width, channels = output.shape
  print("height, width, channels ", height, width, channels )
  # print(output.shape)
  output = cv2.rotate(output, cv2.ROTATE_90_CLOCKWISE)
  height, width, channels = output.shape
  print("height, width, channels ", height, width, channels )
  # print(output.shape)

  # for index, c in enumerate(corners):
  #   character = chr(65 + index)
  #   cv2.putText(output, character, tuple(c), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 255), 2, cv2.LINE_AA)
  resized_image = cv2.resize(con, (528, 750))
  cv2.imshow("a", resized_image)
  cv2.waitKey(0)
  output = cv2.resize(output, (1000, 750))
  cv2.imshow("b", output)
  cv2.waitKey(0)

scan()
