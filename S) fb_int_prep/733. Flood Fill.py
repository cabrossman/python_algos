
### BACKTRACKING
def flood_fill(image, sr, sc, newColor):
    if not image:
        return []
    rows, cols = len(image), len(image[0])
    startColor = image[sr][sc]
    # If the color of the pixel at (sr, sc) is the same as newColor, we don't need to do anything
    if startColor == newColor:
        return image
    # Use a queue to keep track of pixels to process
    queue = [(sr, sc)]

    while queue:
        r, c = queue.pop(0)  # dequeue a pixel
        # Check if the current pixel's color is the starting color
        if image[r][c] == startColor:
            # Change the color
            image[r][c] = newColor
            # Add the 4-directional neighbors to the queue if they are valid
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    queue.append((nr, nc))

    return image

input_img = [[1,1,1],[1,1,0],[1,0,1]]
output_img = [[2,2,2],[2,2,0],[2,0,1]]
assert flood_fill(image = input_img, sr = 1, sc = 1, newColor = 2) == output_img

input_img = [[0,0,0],[0,0,0]]
output_img = [[0,0,0],[0,0,0]]
assert flood_fill(image = input_img, sr = 0, sc = 0, color = 0) == output_img