from PIL import Image
import numpy as np

class Commands:
    def _scale(self, num, min, max):
        return num % ( max - min + 1) + min

    def _unique_count_app(self, a):
        a = np.asarray(a)
        colors, count = np.unique(a.reshape(-1,a.shape[-1]), axis=0, return_counts=True)
        return colors[count.argmax()]

    def ratemypic(self, img):
        color = self._unique_count_app(Image.open(img))
        sum = 0

        for i in color:
            sum += i

        return self._scale(sum, 0, 100)