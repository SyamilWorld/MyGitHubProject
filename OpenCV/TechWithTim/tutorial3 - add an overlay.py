# Add an overlay
import cv2 as cv

file = 'assets/messi.jpg'
img = cv.imread(file, cv.IMREAD_COLOR)

text = f'file name: {file}\n\
        width: {img.shape[1]}\n\
        height: {img.shape[0]}\n\
        channels: {img.shape[2]}'

cv.imshow('window', img)
#cv.displayOverlay('window', f'file name: {file}')
#cv.displayOverlay('window', f'file name: {file}', 0)
#cv.displayOverlay('window', 'line 1\nline 2\nline 3')
cv.displayOverlay('window', text)


cv.waitKey(0)
cv.destroyAllWindows()